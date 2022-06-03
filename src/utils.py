from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline

from src.feature_preparation.core import FeatureLearningMethod
from src.model_generation.models import Model
import src.global_vars as gv


def make_grid_search_ready(pipeline:Pipeline):
    if "feature_learning__n_generations" in pipeline.get_params():
        pipeline.set_params(feature_learning__n_generations=25)
    return pipeline

def make_evaluation_ready(pipeline:Pipeline, csv_text=''):
    if "feature_learning__n_generations" in pipeline.get_params():
        pipeline.set_params(feature_learning__n_generations=500)
    if "feature_learning__save_to_csv" in pipeline.get_params():
        pipeline.set_params(feature_learning__save_to_csv=csv_text)
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
        Xt,
        y,
        scoring = 'mean_squared_error',
        splits = gv.SPLITS,
        additional_text = '',
    ):
    if scoring == 'mean_squared_error':
        scoring = mean_squared_error
    else:
        scoring = mean_squared_error
    
    scores = list()
    
    for split in splits:
        est = make_pipeline(feature_learning, model, seed, params)
        est = make_evaluation_ready(est, f"{additional_text}model={model}_split={split}")
        
        cut = int(split * len(Xt))
        train_X = Xt[:cut]
        train_y = y[:cut]
        test_X = Xt[cut:]
        test_y = y[cut:]

        est = est.fit(train_X,train_y)
        predictions = est.predict(test_X)

        score = scoring(predictions,test_y)
        scores.append(score)
        
    return scores

