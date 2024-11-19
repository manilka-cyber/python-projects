

import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv("country_vaccinations_by_manufacturer.csv")

print(df)

df1 = df.head()

print(df1)

df2 = df.tail()

print(df2)

df3 = df.shape

print(df3)

df4 = df.dtypes

print(df4)

df5 = df.columns.values

print(df5)

print(df.isnull().sum())

print(df.fillna(0))

arr1 = df['location'].nunique()

print(arr1)

arr2 = df['location'].unique()

print(arr2)

total_vaccinations = df.groupby('location')['total_vaccinations'].sum().reset_index()

print(total_vaccinations)

vaccination_type = df.groupby(['location',"vaccine"])['total_vaccinations'].sum().reset_index()

print(vaccination_type)

plt.bar(total_vaccinations["location"],total_vaccinations["total_vaccinations"])

plt.xlabel('xaxis')

plt.ylabel('total_vaccinations')

plt.title('country_vaccination')

plt.xticks(rotation=90)

plt.show()

