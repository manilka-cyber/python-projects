import pandas as pd
import matplotlib.pyplot as plt

# Create a sample DataFrame
data = {
    'units': [1, 2, 3, 4, 5],
    'price': [7, 12, 8, 13, 16]
}

# Create a DataFrame df
df = pd.DataFrame(data)

# Plot with kind specified as 'line'
df.plot(x='units', y='price', kind='line', marker='o', title='Price vs Units')

# Add grid to the p

# Labeling axes
plt.xlabel('Units')
plt.ylabel('Price')

# Show the plot
plt.show()
 
import numpy as np

x = np.random.rand(0,5)

print(x)

# Division of 3 by 1.2
A = 3 / 1.2

# Print the result
print(A)  # This will print: 2.5

height = [140,145,130]

print(height.sort())

print(height)

import matplotlib.pyplot as plt
import numpy as np

# Simulate rolling a 6-sided die 20 times
np.random.seed(0)  # For reproducibility
rolls = np.random.randint(1, 7, size=20)  # Roll the die 20 times

# Count the frequency of each outcome
outcomes, counts = np.unique(rolls, return_counts=True)

# Create a bar chart
plt.figure(figsize=(2, 2))  # Set the figure size
plt.bar(outcomes, counts, color='skyblue', edgecolor='black')
plt.title('Frequency of Outcomes for 20 Rolls of a 6-Sided Die')
plt.xlabel('Die Face')
plt.ylabel('Frequency')
plt.xticks(outcomes)  # Ensure all die faces are shown on the x-axis
plt.grid(axis='y')  # Add grid lines for better readability
plt.show()
