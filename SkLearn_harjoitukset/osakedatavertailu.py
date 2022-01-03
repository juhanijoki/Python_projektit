import pandas as pd
import numpy as np

df = pd.read_csv('osakedata.csv', sep=';', decimal=',')


yhtiolista = []
for yhtio in df['Yhtio']:
    yhtiolista.append(yhtio)
df = df.drop(columns='Yhtio')
#print(df.head())
#print(yhtiolista)

df['Osinkotuotto-%2'].describe()
# näyttää tilastot, jos matriisi olisi vain numeroita
df1 = df.groupby('Riskitaso')['Tavoitehinta'].describe().T
#print(df1.head())
# P/E luvun vertailu riskitason mukaan
df2 = df.pivot_table(values='P/E', index='Riskitaso', columns='Potentiaali')
#print(df2.head())

df3 = df.pivot_table(values='P/E', index='Riskitaso', aggfunc=[min, np.median, np.mean, max])
df3.index = ['Matala', 'Hieman matala', 'Hieman korkea', 'Korkea']
df3.columns = ['Pienin', 'Mediaani', 'Keskiarvo', 'Suurin']
print(df3.head())
