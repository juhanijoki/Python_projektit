from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()

X = iris.data
y = iris.target

classes = ['Setosa', 'Versicolour', 'Virginica']
#print(X)
#print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
#Mallin luominen
malli = svm.SVC()
malli.fit(X_train, y_train)
#Datan tarkistus
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
#ennustus
predictions = malli.predict(X_test)
acc = accuracy_score(y_test, predictions)

print('predictions:', predictions)
print('actual:', y_test)
print('accuracy:', acc)