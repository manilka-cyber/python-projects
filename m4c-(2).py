#Tutorial 11

import pandas as pd
import matplotlib.pyplot as plt 
import statistics


#part1

#1

data = {"player_names":["pathum","kusal","charith","dasun","chamika"],"run_scored":[137,87,6,0,0]}

df = pd.DataFrame(data)

print(df)

#2

mean = df['run_scored'].mean()

print(mean)

#3
sorted = df['run_scored'].sort_values()

print(sorted)

median = df['run_scored'].median()

print(median)

#4

mode = statistics.mode(df['run_scored'])

print(mode)

#5

#Mean is total of all data and devide by number of values

#Median is middle value in sorted list

#Mode is most repeated value

#median is represent best performance because it's middle value

#part 2
#6

plt.hist(df['run_scored'],bins =7)

plt.show()


#7

#devided range into intervals

#8

#range of 0-20  get 3 values,1 value get 80-100 and 120-140

#9

plt.bar(df['player_names'],df['run_scored'])

plt.xlabel('players_name')

plt.ylabel('run_scored')

plt.title('RunsS cored')

plt.show()

#10

#bar chart shows variables and values
#histrogram shows range of values









