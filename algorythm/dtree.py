from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import  train_test_split
from sklearn.datasets import load_iris

import numpy as np
import pandas as pd

class DTree:
    def __init__(self):
        pass
    def breast_cancer(self):
        cancer =load_breast_cancer
        X_train,X_test,y_train,y_test = train_test_split(
            cancer.data, cancer.target, stratify=cancer.target, random_state=42
        )
        tree =DecisionTreeClassifier()
        tree.fi(X_train,y_train)
        print('훈련세트이 정확도 : {: .3f}'.format(tree.score(X_train,y_train)))
        print('테스트세트이 정확도 : {: .3f}'.format(tree.score(X_train, y_train)))

    def iris(self):
        np.random.seed(0)
        iris = load_iris()
        df = pd.DataFrame(iris.data, columns= iris.feature_names)
        print(df.head())
