from sklearn.pipeline import Pipeline


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
                        
