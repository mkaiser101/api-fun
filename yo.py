import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score

df_train = pd.read_csv('http://cmci.colorado.edu/classes/INFO-4604/data/tweet_predictions_cv.csv', header=None)
df_test = pd.read_csv('http://cmci.colorado.edu/classes/INFO-4604/data/tweet_predictions_test.csv', header=None)

Y_train = df_train.iloc[0:, 0].values
X_train = df_train.iloc[0:, 1:].values

Y_test = df_test.iloc[0:, 0].values
X_test = df_test.iloc[0:, 1:].values

from sklearn.decomposition import PCA
from sklearn import decomposition
from sklearn.metrics import accuracy_score


train_arr =list()
test_arr =list()
R = [1,2,10,20,30,40,50,100,200]

pca = decomposition.PCA(n_components=1, random_state=123)
pca.fit(X_train)

X_train = pca.transform(X_train)
X_test = pca.transform(X_test)

params = [{'C': [0.01, 0.1,.2,.3,.4, 0.5,.6,.7,.8,.9, 1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2, 2.5, 5.0, 10.0, 50.0,]}]
gs_classifier = GridSearchCV(base_classifier, params, cv=5)
gs_classifier.fit(X_train, Y_train)
trainscore = gs_classifier.best_score_
testscore = accuracy_score(Y_test, gs_classifier.predict(X_test)
