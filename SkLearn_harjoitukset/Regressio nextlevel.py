import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_boston

boston_data = load_boston()

boston_data.keys()
#print(boston_data.DESCR)
#Data datafreimiin
df = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)

df['MEDV'] = boston_data.target

#print(df.head())
# Tarkistetaan puuttuuko datasta arvoja
#print(df.isnull().sum())
# Target muuttujan jakauma (selitettävä muuttuja)
#sns.distplot(df['MEDV'], bins=30)

# Korrelaatiokertoimet 2 desimaalin tarkkuudella
correlation_matrix = df.corr().round(2)

# Kuvio, jonka sisään korrelaatiomatriisi mahtuu
plt.figure(figsize=(12,9))

# Seaborn-kirjaston heatmap lisää värimuotoilun, etsitään korrelaatiot
sns.heatmap(data=correlation_matrix, annot=True)

# Muuttujat joilla korkeimmat korrelaatiokertoimet (PTRATIO lisätty parantamaan mallia)
features = ['LSTAT', 'RM', 'PTRATIO']

target = df['MEDV']

#Kuvio jonka sisään mahtuu kaksi hajontakaaviota
plt.figure(figsize=(15, 5))

# Enumerate-funktion avulla käydään lista läpi ja palauttaa jokaisesta
# listan alkiosta järjestysnumeron (alkaen nollasta) ja arvon
for i, feature in enumerate(features):
    plt.subplot(1, len(features), i + 1)
    plt.scatter(df[feature], target)
    plt.xlabel(feature)
    plt.ylabel('MEDV')
#plt.show()

# Valmistellaan data
X = df[features]
y = target

# Datan jako
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)
# Random statella saadaan eri kokeilukerroilla aina sama jako opetus-jatestidataan
"""
# Tarkistetaan datojen koot
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
"""
# Sovitetaan regressiomallin opetusdataan
from sklearn.linear_model import LinearRegression

malli = LinearRegression().fit(X_train, y_train)
print(malli.coef_)
print(malli.intercept_)

# Mallin luotettavuuden statistiikka
from sklearn.metrics import mean_absolute_error

y_train_predict = malli.predict(X_train)
mae = (mean_absolute_error(y_train, y_train_predict)) # keskim virhe
r2 = malli.score(X_train, y_train) # selityskerroin

print('Mallin sopivuus opetusdataan')
print()
print('Keskimääräinen virhe: {}'.format(mae))
print('Selityskerroin: {}'.format(r2))
print("\n")

y_test_predict = malli.predict(X_test)
mae = (mean_absolute_error(y_test, y_test_predict))
r2 = malli.score(X_test, y_test)

print('Mallin sopivuus testidataan')
print()
print('Keskimääräinen virhe: {}'.format(mae))
print('Selityskerroin: {}'.format(r2))

# Verrataan testidatan havaintoja mallin antamiin ennusteisiin
# Dataframen luonti
test = pd.DataFrame()
test['y_test'] = y_test
test['y_test_predict'] = y_test_predict


