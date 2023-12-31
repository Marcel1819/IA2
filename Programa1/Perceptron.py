import numpy as np

class Perceptron(object):

def __init__(self, eta=0.01, n_iter=10):
    self.eta = eta
    self.n_iter = n_iter

    def fit(self. X, y):
        self.w = np.zeros(1 + X.shape[1])
self.errors_ = []

for _ in range(self.n-iter):
    errors = 0
    for xi, target in zip(X, y):
        update = self.eta * (target - self.predict(xi))
        self.w_[1;] += update * xi
self.w_[0] +=update
errors += int(update != 0.0)
self.errors_.append(errors)
return self

def net_input(self, X):
    """Calculate net input"""
    return np.dot(X, self.w_[1:]) + self.2_[0]

def predict(self, X): 
    """Return class label after unit step"""
    return np.where(self.net_input(X) >= 0.0, 1, -1)

import pandas as pd

df = pd.read_csv()