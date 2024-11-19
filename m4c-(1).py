#Assignment 2

#part1

#a
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ClimateChangeData.csv")

print(df)

#237 records

#b

missing_values = df.isnull().values.any()

print(missing_values)

total_missing_values = df.isnull().sum().sum()

print(total_missing_values)

#c

handling_missing_values = df.fillna(0)

print(handling_missing_values)



#we can get mean,median,mode of each column

#d
# 74 countries

countries = ['africa','american','togo','st.lucia','cook islan','denmark','chile','anguilla','antigua and barbuda','armenia,rep.of',

'aruba,kindom of the netherland','azerbaijan','barbados','belarus','belgium','bosnia and herzegovina','british virgin island','burundi',

'cabo verde','cayman island','costa rica','croatia','czech','djibouti','dominica','equatorial guinea','eritria','estonia','ethiopia',

'falkland','geogia','guadeloupe','jamaica','kazakhstan','kiribati','kyrgyz','latvia','lithunia','luxembourg','maldives','marshall',

'mayotte','micronesia','moldova','montenegro','nauru','niue','norfolk','north macedonia','palau','pitcairn','puerto rico',

'russian federation','rwanda','samoa','sao tome and principe','serbia','singapore','slovak','slovenia','soloman','south sudan',

'st.kitts and nevis','sudan','tajikistan','timor-leste','tokelau','turkmenistan','turks and caicos island','tuvalu','ukraine',

'united states virgin island','uzbekistan','yemen']

print(countries)

#e

new_df = pd.DataFrame(handling_missing_values)

print(new_df)

#part2

#a

#237 countries

#b


new_df['mean_temp_change_each_country'] = new_df[['1961','1962','1963','1964','1965','1966','1967','1968','1969','1970'
,'1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985',
'1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000',
'2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016',
'2017','2018','2019','2020','2021','2022','2023']].mean(axis=1)

print(new_df)

#c


new_df['year'] = range(1961, 1961 + len(new_df))



print(new_df)


new_df_filled = new_df[['1961','1962','1963','1964','1965','1966','1967','1968','1969','1970'
,'1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985',
'1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000',
'2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016',
'2017','2018','2019','2020','2021','2022','2023']].fillna(0)  


new_df['mean_temp_change_each_year'] = new_df_filled.mean(axis=0)


print(new_df)


#part 3

#a

#1,2

all_countries = new_df['Country']

mean_temp_change_each_country = new_df['mean_temp_change_each_country'] 

plt.bar(all_countries,mean_temp_change_each_country)

plt.xticks(rotation=45)

plt.show()

#compare the each mean temp change

#b

year = new_df['year']

mean_temp_change_each_year = new_df['mean_temp_change_each_year']

plt.bar(year,mean_temp_change_each_year)

plt.show()

#c

#suriname , monaco ,australia,libia,europe

#d

top_countries = new_df.nlargest(5, 'mean_temp_change_each_country')

highest_mean_temp_countries = top_countries['Country']
mean_temp_change_each_country = top_countries['mean_temp_change_each_country']



plt.bar(highest_mean_temp_countries,mean_temp_change_each_country,color=['m','y','k','b','w'])

plt.legend(loc= 'upper left',title = 'yearly mean temp change',fontsize ='10',title_fontsize = '10')

plt.show()

#e

#comparison of historical and predicted future data

historical_data = new_df.loc[:, '1961':'2023'].mean(axis=0)
predicted_data = [2.5, 2.7, 2.9, 3.0, 3.2]  
future_years = [2024, 2025, 2026, 2027, 2028]

plt.bar(historical_data.index, historical_data, label='Historical')
plt.bar(future_years, predicted_data, label='Predicted', linestyle='--')
plt.title('Historical vs Predicted Temperature Change')
plt.xlabel('Year')
plt.ylabel('Temperature Change (°C)')
plt.legend(title='Data Type')
plt.show()



































