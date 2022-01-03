from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

boston = datasets.load_boston()

X = boston.data
y = boston.target
"""
print('X')
print(X)
print(X.shape)
print('y')
print(y)
print(y.shape)
"""
l_reg = linear_model.LinearRegression()

plt.scatter(X.T[5], y)
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#Train
malli = l_reg.fit(X_train, y_train)
predictions = malli.predict(X_test)

print('Predictions:', predictions)
print('R^2 value:', l_reg.score(X, y))

print('coedd:', l_reg.coef_)
print('Intercept:', l_reg.intercept_)

