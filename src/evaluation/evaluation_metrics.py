from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error


def cv_time_series(est, Xt, y, scoring = 'mean_squared_error', splits = [ 0.5, 0.66, 0.83 ]):
    if scoring == 'mean_squared_error':
        scoring = mean_squared_error
    else:
        scoring = mean_squared_error
    
    scores = list()
    
    for split in splits:
        cut = int(split * len(Xt))
        train_X = Xt[:cut]
        train_y = y[:cut]
        test_X = Xt[cut:]
        test_y = y[cut:]

        model = est.fit(train_X,train_y)
        predictions = model.predict(test_X)

        score = scoring(predictions,test_y)
        scores.append(score)
        
    return scores


def cv_score(classifier, X, y, cv_percent):
    scoring: str = 'neg_mean_squared_error'
    
    return cross_val_score(classifier, X, y , cv=cv_percent, scoring=scoring)

