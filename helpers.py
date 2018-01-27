"""
Convenience functions for kaggle house prices comp.
"""
import math

def get_info(query):
    """Convenience to return description"""
    f = open('data/data_description.txt', 'r')
    lines = f.readlines()
    for line in lines:
        if line.startswith(query):
            return(line.split(":")[-1].rstrip())


#A function to calculate Root Mean Squared Logarithmic Error (RMSLE)
def rmsle(y, y_pred):
    assert len(y) == len(y_pred)
    terms_to_sum = [(math.log(y_pred[i] + 1) - math.log(y[i] + 1)) ** 2.0 for i,pred in enumerate(y_pred)]
    return (sum(terms_to_sum) * (1.0/len(y))) ** 0.5
