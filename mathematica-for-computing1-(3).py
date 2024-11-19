import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Part 01
# 1
player_names = np.array(['Pathum Nissanka', 'Kusal Mendis', 'Charith Asalanka', 'Dasun Shanaka', 'Chamika Karunaratne'])
runs_scored = np.array([137, 87, 6, 0, 0])


df = pd.DataFrame({'Player Name': player_names, 'Runs Scored': runs_scored})

# 2
mean_runs = np.mean(runs_scored)

print(f"Mean of runs scored: {mean_runs}")

# 3


df_sorted = df.sort_values(by='Runs Scored')

print(df_sorted)

median_runs = np.median(runs_scored)

print(f"Median of runs scored: {median_runs}")

# 4
mode_runs = stats.mode(runs_scored)

print(f"Mode of runs scored: {mode_runs}")


# Part 02
# 6
plt.figure(figsize=(8,5))
plt.hist(runs_scored, bins=5, color='lightblue', edgecolor='black')
plt.title('Histogram of Runs Scored by Sri Lankan Players')
plt.xlabel('Runs Scored')
plt.ylabel('Frequency')

# 7
# Bins divide the range of data into intervals, helping to visualize how many data points fall into each range.

# 8
# The histogram shows that most players scored very low runs (0), with only one player scoring very high (137), indicating a skewed distribution.

plt.show()

# 9
plt.figure(figsize=(8,5))
plt.bar(player_names, runs_scored, color='green')
plt.title('Runs Scored by Each Player in the ODI Match')
plt.xlabel('Player Name')
plt.ylabel('Runs Scored')
plt.show()

#10
# - Bar chart: Compares discrete categories (player names) and their values (runs scored).
# - Histogram: Displays the distribution of continuous data by grouping values into bins and showing frequencies.



