from sklearn.model_selection import cross_val_score





def cv_score(classifier, X, y, cv_percent):
    
    return cross_val_score(classifier, X, y , cv=cv_percent, scoring='neg_mean_squared_error')

