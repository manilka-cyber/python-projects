import pandas as pd
#1
df = pd.read_csv("ClimateChangeData.csv")

print(df)

#part 1

#a

num_records = df.shape[0]

num_coloumns = df.shape[1]

print(f"number of records:{num_records}")

print(f"number of coloumns :{num_coloumns}")

#b

missing_value = df.isnull().sum()

print("missing values per coloumn :")

print(missing_value)

total_missing = df.isnull().sum().sum()

print(f"total missing values in the dataset:{total_missing}")

#c

df_cleaned = df.fillna(0)

print(df_cleaned)

#d

countries_with_missing_values = df[df.isnull().any(axis = 1)]["Country"].unique()

print(f"countries with missing values :{countries_with_missing_values}")

#e

df_cleaned.to_csv("cleaned_dataset.csv" ,index = False)

print(df_cleaned.head())

#part 2

#a

unique_countries = df_cleaned["Country"].nunique()

print(f"number of different countries : {unique_countries}")

#b

temp_columns = [col for col in df_cleaned.columns if col.startswith("Temp_")]

df_cleaned["mean temp.change"] = df_cleaned[temp_columns].mean(axis=1)

print(df_cleaned["mean temp.change"])

#c

yearly_temp_change = {
    year: df_cleaned[f'Temp_{year}'].mean() 
    for year in range(1967, 2023+1) 
    if f'Temp_{year}' in df_cleaned.columns
}

df_yearly_temp_change = pd.DataFrame(list(yearly_temp_change.items()), columns=['Year', 'Mean Temp. Change'])

print(df_yearly_temp_change)

# part 3

#a

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('ClimateChangeData.csv')


decade_years = [str(year) for year in range(2013, 2024)]
df_decade = df[['Country'] + decade_years].copy()


df_decade[decade_years] = df_decade[decade_years].apply(pd.to_numeric, errors='coerce')


df_decade['Mean Decade Temp Change'] = df_decade[decade_years].mean(axis=1)


plt.figure(figsize=(12, 6))
plt.bar(df_decade['Country'], df_decade['Mean Decade Temp Change'])
plt.xticks(rotation=45)
plt.title('Mean Temperature Change in the Last Decade (2013-2023) by Country')
plt.ylabel('Mean Temperature Change (°C)')
plt.xlabel('Country')
plt.show()

#b


years = df.columns[1:]  


mean_temp_changes = df[years].apply(pd.to_numeric, errors='coerce').mean()


year_values = pd.to_numeric(years, errors='coerce')


plt.figure(figsize=(10, 6))
plt.plot(year_values, mean_temp_changes, marker='o', color='blue')
plt.title('Global Average Temperature Change (1967-2023)')
plt.xlabel('Year')
plt.ylabel('Mean Temperature Change (°C)')
plt.grid(True)
plt.show()

# c


top_5_countries = df_decade.nlargest(5, 'Mean Decade Temp Change')[['Country', 'Mean Decade Temp Change']]
print(top_5_countries)

# d

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('ClimateChangeData.csv')


df_melted = pd.melt(df, id_vars=['Country'], var_name='Year', value_name='Temp Change')


df_melted['Year'] = pd.to_numeric(df_melted['Year'], errors='coerce')


df_melted['Temp Change'] = pd.to_numeric(df_melted['Temp Change'], errors='coerce')


df_melted = df_melted.dropna(subset=['Year', 'Temp Change'])


top_5_countries = df[['Country'] + [str(year) for year in range(2013, 2024)]].copy()
top_5_countries.iloc[:, 1:] = top_5_countries.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')
top_5_countries['Mean Decade Temp Change'] = top_5_countries.iloc[:, 1:].mean(axis=1)
top_5_countries = top_5_countries.nlargest(5, 'Mean Decade Temp Change')['Country'].tolist()


plt.figure(figsize=(10, 6))
for country in top_5_countries:
    country_data = df_melted[df_melted['Country'] == country]
    plt.plot(country_data['Year'], country_data['Temp Change'], label=country)


plt.title('Temperature Change for Top 5 Countries with the Highest Mean Temperature Change (1967-2023)')
plt.xlabel('Year')
plt.ylabel('Temperature Change (°C)')
plt.legend(title='Country')
plt.grid(True)
plt.show()

# e


region_mapping = {
    'USA': 'North America',
    'Canada': 'North America',
    'Germany': 'Europe',
    'France': 'Europe',
    
}


df['Region'] = df['Country'].map(region_mapping)


df_decade['Region'] = df['Region']
df_region = df_decade.groupby('Region')['Mean Decade Temp Change'].mean().reset_index()


plt.figure(figsize=(10, 6))
plt.bar(df_region['Region'], df_region['Mean Decade Temp Change'], color='lightcoral')
plt.title('Mean Temperature Change by Region (2013-2023)')
plt.xlabel('Region')
plt.ylabel('Mean Temperature Change (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
