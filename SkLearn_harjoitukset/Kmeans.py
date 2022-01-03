from sklearn.datasets import load_breast_cancer
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import scale
import pandas as pd

# Esimerkki datasetin lataus
bc = load_breast_cancer()

X = scale(bc.data)

y = bc.target
# Datan jako opetukseen ja testaukseen
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=6)

# Luodaan K-means-malli klusterointia varten.
malli = KMeans(n_clusters=2, random_state=0)

malli.fit(X_train)

# Ennustus test-datasta train-datan arvojen perusteella
predictions = malli.predict(X_test)
labels = malli.labels_

print('labels', labels)
print('predictions', predictions)
print('accuracy', accuracy_score(y_test, predictions))
print('actual', y_test)

print(pd.crosstab(y_train, labels))




