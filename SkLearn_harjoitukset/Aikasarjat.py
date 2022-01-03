import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

cc = pd.read_csv('KO.csv', sep=',', decimal='.')

cc.index = pd.to_datetime(cc['Date'], format= '%Y-%m-%d')
cc = cc.drop('Date', axis=1)
cc = cc.drop('Adj Close', axis=1)
cc = cc.drop('Volume', axis=1)
print(cc.head())
#cc.plot()
#cc['Close'].resample('M').mean().plot()
#plt.show()
# Luo trendikäyrän
from statsmodels.tsa.api import seasonal_decompose
#seasonal_decompose(cc['Close']).plot()
#plt.show()
# Luodaan malliolio joka tekee ennustamisen
from statsmodels.tsa.api import ExponentialSmoothing
malli = ExponentialSmoothing(cc['Close'], trend='add', seasonal='mul', seasonal_periods=4).fit()

cc['Ennuste'] = malli.fittedvalues
cc.plot()
#plt.show()
cc['Ennustevirhe'] = malli.resid
print(cc.head())
# Virheen määrittäminen
from sklearn.metrics import mean_squared_error, mean_absolute_error
print('Mean squared error', mean_squared_error(cc['Close'], cc['Ennustevirhe']))
print('Mean absolute error', mean_absolute_error(cc['Close'], cc['Ennustevirhe']))
#cc['Ennustevirhe'].plot()
#plt.ylabel('Ennustevirhe')
#plt.show()
"""
plt.scatter(x=cc['Ennuste'], y=cc['Close'])
plt.xlabel('Ennuste')
plt.ylabel('Toteutunut Close')
plt.show()
"""
# Ennusteen tekeminen
index = pd.date_range('2021-01-01', periods=4, freq='D')
ennusteet = malli.forecast(4)
# Luodaan datafreimi joka sisältää ennusteen arvot (ei jostain syystä palauttanut numeroita)
cc_ennuste = pd.DataFrame(data=ennusteet, index=index, columns=['Ennuste'])
print(cc_ennuste.head())
cc['Close'].plot()
cc_ennuste['Ennuste'].plot()
plt.show()
