from sklearn.metrics import mean_squared_error, f1_score
from sklearn.pipeline import Pipeline

from feature_preparation.core import FeatureLearningMethod
from model_generation.models import Model
import global_vars as gv


def make_grid_search_ready(pipeline:Pipeline, test=False):
    if "feature_learning__n_generations" in pipeline.get_params():
        n_gens = 15
        if test:
            n_gens = 1
        pipeline.set_params(feature_learning__n_generations=n_gens)
    return pipeline

def make_evaluation_ready(pipeline:Pipeline, csv_text='', test_data=None, test=False, on_budget=False):
    if "feature_learning__n_generations" in pipeline.get_params():
        n_gens = 500
        if test:
            n_gens = 15
        pipeline.set_params(feature_learning__n_generations=n_gens)
    if "feature_learning__save_to_csv" in pipeline.get_params():
        pipeline.set_params(feature_learning__save_to_csv=csv_text)
    if "feature_learning__test_data" in pipeline.get_params():
        pipeline.set_params(feature_learning__test_data=test_data)
    if "feature_learning__on_budget" in pipeline.get_params():
        pipeline.set_params(feature_learning__on_budget=on_budget)
    return pipeline
                        
def make_pipeline(feature_learning: FeatureLearningMethod, model: Model, seed: int, params=None):
    pipeline = Pipeline(steps=[('feature_learning', feature_learning.method(seed = seed)),
                                            ('model', model.evaluate(seed))])
    if params:
        pipeline.set_params(**params)
    return pipeline
    

def cv_time_series(
        feature_learning: FeatureLearningMethod,
        model: Model,
        seed: int,
        params,
        X,
        y,
        scoring = gv.SCORING,
        splits = gv.SPLITS,
        additional_text = '',
        test=False,
        on_budget=False,
    ):
    if scoring == 'f_score':
        scoring = f1_score
        preprocess_predictions = lambda x: int(x > 0.5)
    else:
        scoring = mean_squared_error
        preprocess_predictions = lambda x: x
    
    test_scores = list()
    train_scores = list()
    fittest_inds = list()
    
    for split in splits:
        cut = int(split * len(X))
        train_X = X[:cut]
        train_y = y[:cut]
        test_X = X[cut:]
        test_y = y[cut:]

        est = make_pipeline(feature_learning, model, seed, params)
        est = make_evaluation_ready(est, f"{additional_text}model={model}_split={split}", test_data=(test_X, test_y), test=test, on_budget=on_budget)
        
        est = est.fit(train_X,train_y)
        test_predictions = est.predict(test_X)
        train_predictions = est.predict(train_X)
        test_predictions = list(map(preprocess_predictions, test_predictions))
        train_predictions = list(map(preprocess_predictions, train_predictions))

        test_score = scoring(test_predictions,test_y)
        train_score = scoring(train_predictions,train_y)
        test_scores.append(test_score)
        train_scores.append(train_score)
        if hasattr(est.steps[0][1], "feature_mapping"):
            fittest_ind = str(est.steps[0][1].feature_mapping)
            fittest_inds.append(fittest_ind)
        
    return test_scores, train_scores, fittest_inds

