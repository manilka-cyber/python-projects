lst = [0,1,2,3]

lst[1:3] = [8,9]

print(lst)

numbers = [1,2,3,4]

print(numbers[::-1])

total = 0

for i in range (1,6):

    if i % 2 == 0 :

        total += i

    else :
        total -= i

print(total)

for i in range (11):
    total += i 
    print(i)

for i in range (1,6):
    print(i)
'''
sum     = 0
count   = 0
average = 0 


while count <10:

    num = int(input('enter a number:'))

    

    sum   += num
    count += 1

average = sum/10

print('thesum:',sum)

print('the average:',average)'''

'''sum     = 0
count   = 1
average = 0 

while True:

    num = int(input('enter a number:'))

    if num < 0 :
        break

    sum   += num
    count += 1

average = sum/count

print('thesum:',sum)

print('the average:',average)'''


'''i = 1

sum = 0 

while i<= 10:

    sum = sum +i
    i = i+1

    print("sum:",sum)


i = 1

sum = 0 
n = int(input('enter a number:'))
while i<= n:

    sum = sum +i
    i = i+1

    print("sum:",sum)'''

'''def add (n1,n2):
    return (n1*n2)

ans = add(4,7)
print(ans)

x = 20  # This is a global variable

def my_function(): 
    local_var = 20  # This is a local variable
    print("Inside the function:", local_var)  # This works

my_function()  # Output: Inside the function: 20

# Trying to access the local variable outside the function
# This will raise a NameError because local_var is not defined in this scope
print(local_var)  # Uncommenting this line will cause an error'''

'''mark = int(input("Enter student's mark: "))

if mark > 65 and mark < 75:
    print("Grade: B")
else:
    print("Grade not in B range.")

group1_attended = True   # Set to True if attended, False otherwise
group2_attended = False
group3_attended = False

if group1_attended or group2_attended or group3_attended:
    print("CA passed")
else:
    print("CA not passed")'''

'''import numpy as np
print(np.__version__)
print('\n')
import numpy as np
print(np.__version__)

import numpy as np
E = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
F = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print("Matrix E:\n", E)
print("Shape of E:", E.shape)
print("Size of E:", E.size)

print("\nMatrix F:\n", F)
print("Shape of F:", F.shape)
print("Size of F:", F.size)


print(E[0,1])

arr2 = np.array([
    [45, 10, 19],
    [23, 45, 64],
    [12, 67, 30]
])


print("Original array:")
print(arr2)

arr2[arr2 >= 45] = 100

print("Modified array:")
print(arr2)

# Ask user for the length of the array
array_length = int(input("Enter the length of the array: "))

# Initialize an empty list to store user inputs
user_array = []

# Collect each element from the user
for i in range(array_length):
    value = int(input(f"Enter value {i+1}: "))
    user_array.append(value)

# Convert the list to a NumPy array
arr_user = np.array(user_array)
print("Your array:", arr_user)'''

'''# Step 1: Create names and marks arrays
names = ["Harry", "Hermione", "Ronald", "Fred", "George"]
marks = [65, 99, 66, 82, 81]

# Display arrays
print("Names:", names)
print("Marks:", marks)

# Step 2 & 3: Display student name, mark, and grade

# Step 1: Create names and marks arrays


for i in range(len(names)):
    if names[i] == "Fred" or names[i] == "George":
        mark = 0
        grade = 'F'
    elif marks[i] > 85:
        grade = 'A'
        mark = marks[i]
    elif 70 <= marks[i] <= 84:
        grade = 'B'
        mark = marks[i]
    elif 55 <= marks[i] <= 69:
        grade = 'C'
        mark = marks[i]
    else:
        grade = 'F'
        mark = marks[i]
    
    # Printing formatted output in a single line
    print(f"{names[i]:<10} {mark:<5} {grade}")
import numpy as np
import matplotlib.pyplot as plt

# Example data (replace with actual data)
years = np.array([1896, 1900, 1904, 2000, 2020])  # Example years
swimming_athletes = np.array([10, 15, 20, 70, 100])  # Number of athletes in swimming
track_athletes = np.array([12, 18, 25, 80, 120])  # Number of athletes in track events

print("Year  | Swimming Athletes | Track Athletes")
print("-----------------------------------------")
for i in range(len(years)):
    print(f"{years[i]:<6} | {swimming_athletes[i]:<17} | {track_athletes[i]}")
plt.plot(years, swimming_athletes, label='Swimming Athletes', color='blue', marker='o')
plt.plot(years, track_athletes, label='Track Athletes', color='green', marker='s')

plt.title("Number of Athletes in Swimming and Track Events")
plt.xlabel("Year")
plt.ylabel("Number of Athletes")
plt.legend()
plt.show()

# Countries and number of athletes
countries = np.array(["USA", "China", "Japan", "Germany", "Australia", "France", "UK"])
athletes = np.array([500, 420, 350, 300, 275, 250, 225])

colors = ['royalblue', 'gold', 'red', 'green', 'purple', 'orange', 'brown']
plt.bar(countries, athletes, color=colors)

# Adding labels
plt.title("Number of Athletes from Top 7 Countries - Paris Olympics 2024")
plt.xlabel("Countries")
plt.ylabel("Number of Athletes")



# Adding legend with color representation for each country
for i, country in enumerate(countries):
    plt.bar(country, athletes[i], label=country, color=colors[i])
plt.legend(title="Countries")
plt.show()'''
'''
import numpy as np

# Create an array of birth months
birth_months = np.array([3, 12, 4])
print("Birthday Array:", birth_months)

# Find the most frequently occurring month
most_frequent_month = np.argmax(np.bincount(birth_months))
print("Most Frequently Occurring Month:", most_frequent_month)

# Mapping of months to alphabet letters
month_to_letter = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L'}

# Replace birth month numbers with corresponding letters
secret_code = [month_to_letter[month] for month in birth_months]
print("Secret Code:", ''.join(secret_code))

# Form a creative team name from the secret code
team_name = ''.join(secret_code) + " Team"
print("Team Name:", team_name)
import matplotlib.pyplot as plt

# Create a frequency count for each month
months, counts = np.unique(birth_months, return_counts=True)

# Plotting the data
plt.bar(months, counts, color='skyblue')
plt.xlabel("Birth Month")
plt.ylabel("Frequency")
plt.title("Frequency of Birth Months in Team")
plt.xticks(months)  # Set x-axis labels as month numbers
plt.show()

import numpy as np

# Define matrices A and B
A = np.array([[1, 5, 7], [4, 9, 2], [8, 6, 3]])
B = np.array([[2, 6, 4], [5, 3, 8], [7, 2, 1]])

# Task 1: Add the two matrices
C = A + B
print("Matrix C (A + B):\n", C)

# Flatten matrix C to a 1D array
C_flat = C.flatten()
print("1D Array from Matrix C:", C_flat)

# Apply conditions to matrix C
for i in range(C.shape[0]):
    for j in range(C.shape[1]):
        if C[i, j] > 10:
            C[i, j] = 0
        else:
            C[i, j] += 5

print("Modified Matrix C:\n", C)


# Convert to list to allow element removal and replacement
C_list = C_flat.tolist()

# Remove elements at indices 2, 3, and 5
del C_list[5]
del C_list[3]
del C_list[2]

# Assign values to F, C, and M as specified
C_list[0] = 11  # Assign 11 to F
C_list[1] = 6   # Assign 6 to C
C_list[2] = 12  # Assign 12 to M

print("Final List after modifications:", C_list)'''

'''import pandas as pd

# Define the data as a dictionary
data = {
    'First name': ['Harry', 'Hermione', 'Sam', 'Dean', 'Ronald', 'Lucifer'],
    'Last name': ['Potter', 'Granger', 'Winchester', 'Winchester', 'Weasley', 'Morningstar'],
    'Programme': ['Software Eng.', 'Data Sci.', 'Cyber Sec.', 'Data Sci.', 'Data Sci.', 'Software Eng.'],
    'Curr. GPA': [2.65, 4.00, 3.30, 2.20, 2.70, 4.00]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
'''
'''import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data from the table
data = {
    "Country": ["United States", "India", "China", "Russia", "Brazil", "Germany", "Japan", "United Kingdom", "France", "Mexico"],
    "Continent": ["North America", "Asia", "Asia", "Europe/Asia", "South America", "Europe", "Asia", "Europe", "Europe", "North America"],
    "Heart Attacks 2024": [1700000, 1300000, 1100000, 850000, 750000, 650000, 520000, 480000, 420000, 370000],
    "Fatal Heart Attacks": [500000, 400000, 350000, 300000, 250000, 200000, 150000, 140000, 130000, 120000],
    "Avg. Age of Death": [67, 55, 60, 61, 63, 66, 71, 69, 65, 60],
    "Avg. Age of Attack": [65, 53, 57, 59, 61, 64, 69, 67, 63, 58]
}

# Create DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Sort the DataFrame by 'Heart Attacks 2024' in ascending order
df_sorted = df.sort_values(by="Heart Attacks 2024", ascending=True)
print("\nDataFrame Sorted by Heart Attacks 2024:")
print(df_sorted)

# Find the min, max, and mean for the specified columns
columns = ["Heart Attacks 2024", "Fatal Heart Attacks", "Avg. Age of Death", "Avg. Age of Attack"]

for col in columns:
    min_val = df[col].min()
    max_val = df[col].max()
    mean_val = df[col].mean()
    print(f"\nColumn: {col}")
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")
    print(f"Mean: {mean_val:.2f}")
# Group by 'Continent' and display the groups
df_grouped = df.groupby("Continent")

# Display each continent's group
for continent, group in df_grouped:
    print(f"\nContinent: {continent}")
    print(group)

# Sum heart attacks and fatal heart attacks per continent
continent_data = df.groupby("Continent")[["Heart Attacks 2024", "Fatal Heart Attacks"]].sum()

# Plotting
continent_data.plot(kind="bar", figsize=(10, 6), color=["blue", "red"])
plt.title("Total Heart Attacks and Fatal Heart Attacks by Continent (2024)")
plt.xlabel("Continent")
plt.ylabel("Number of Cases")
plt.legend(["Total Heart Attacks", "Fatal Heart Attacks"])
plt.show()'''

import numpy as np

import matplotlib.pyplot as plt
'''# Define the function
def f2(x):
    return x**2 / (x**2 - 1)

# Define the x range avoiding the discontinuities
x2 = np.linspace(-3, 3, 400)
y2 = f2(x2)

# Filter out values where the function is undefined
y2[np.abs(y2) > 10] = np.nan

# Plotting the function
plt.figure(figsize=(10, 6))
plt.plot(x2, y2, label='f(x) = x^2/(x^2 - 1)', color='green')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.title('Graph of f(x) = x^2/(x^2 - 1)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.ylim(-10, 10)
plt.xlim(-3, 3)
plt.grid()
plt.legend()
plt.show()
'''
'''
# Define the function
def g(x):
    return x**4 - 4*x**3 + 10

# Define the x range
x3 = np.linspace(-1, 5, 400)
y3 = g(x3)

# Plotting the function
plt.figure(figsize=(10, 6))
plt.plot(x3, y3, label='g(x) = x^4 - 4x^3 + 10', color='purple')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.title('Graph of g(x) = x^4 - 4x^3 + 10')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.grid()
plt.legend()
plt.show()'''

'''
import pandas as pd

# Data for players and their runs scored
data = {
    'Player Name': ['Pathum Nissanka', 'Kusal Mendis', 'Charith Asalanka', 'Dasun Shanaka', 'Chamika Karunaratne'],
    'Runs Scored': [137, 87, 6, 0, 0]
}

# Create DataFrame
df = pd.DataFrame(data)
print(df)

# Mode calculation
mode_runs = df['Runs Scored'].mode()[0] # Using [0] to get the first mode if there are multiple
print("Mode of runs scored:", mode_runs)

import matplotlib.pyplot as plt

# Histogram for runs scored
plt.hist(df['Runs Scored'], bins=35, color='skyblue', edgecolor='black')
plt.xlabel('Runs Scored')
plt.ylabel('Frequency')
plt.title('Histogram of Runs Scored by Players')
plt.show()

import pandas as pd

data = {'Runs Scored': [5, 7, 5, 8, 7, 8]}
df = pd.DataFrame(data)

mode_values = df['Runs Scored'].mode()
print("All modes:", mode_values)


import numpy as np
from scipy import stats
import random

# Rolling an unbiased die 10 times
unbiased_rolls = [random.randint(1, 6) for _ in range(10)]
print("Unbiased die rolls:", unbiased_rolls)

# Define probabilities for biased die (5 has 40%, others have 12% each)
probabilities = [0.12, 0.12, 0.12, 0.12, 0.40, 0.12]
outcomes = [1, 2, 3, 4, 5, 6]

# Rolling a biased die 10 times
biased_rolls = np.random.choice(outcomes, 10, p=probabilities)
print("Biased die rolls:", biased_rolls)

# Mean of unbiased die rolls
mean_unbiased = np.mean(unbiased_rolls)
print("Mean of unbiased die rolls:", mean_unbiased)

# Mean of biased die rolls
mean_biased = np.mean(biased_rolls)
print("Mean of biased die rolls:", mean_biased)

# Mode of unbiased die rolls
mode_unbiased = stats.mode(unbiased_rolls)[0]
print("Mode of unbiased die rolls:", mode_unbiased)

# Mode of biased die rolls
mode_biased = stats.mode(biased_rolls)[0]
print("Mode of biased die rolls:", mode_biased)'''

'''
import pandas as pd

# Prepare the data
data = {
    'Flower': ['Rose', 'Tulip', 'Sunflower', 'Daisy'],
    'Color': ['Red', 'Yellow', 'Yellow', 'White'],
    'Size': ['Medium', 'Medium', 'Big', 'Small']
}

# Create the DataFrame
flowers_df = pd.DataFrame(data)

# Display the DataFrame
print(flowers_df)

# Extract flowers that are Yellow
yellow_flowers_df = flowers_df[flowers_df['Color'] == 'Yellow']

# Display the extracted DataFrame
print(yellow_flowers_df)


# Sort the DataFrame by the 'Color' column
sorted_flowers_df = flowers_df.sort_values(by='Color')

# Display the sorted DataFrame
print(sorted_flowers_df)
'''
'''# Import the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Part I - Creating the DataFrame
# Load the CSV file
df = pd.read_csv('country_vaccinations_by_manufacturer.csv')

# (a) Print the DataFrame
print("DataFrame:")
print(df)

# (b) Print .head() and .tail()
print("\nFirst 5 rows of the DataFrame:")
print(df.head())
print("\nLast 5 rows of the DataFrame:")
print(df.tail())

# (c) Print .shape, .dtypes, .columns.values
print("\nShape of DataFrame:", df.shape)  # (rows, columns)
print("Data Types:\n", df.dtypes)        # Data type of each column
print("Column Names:", df.columns.values) # Column names

# Part II - Data Cleaning
# (a) Check for missing values
missing_values = df.isnull().sum()
print("\nMissing values in each column:\n", missing_values)

# (b) Handle missing values (example: dropping rows with any missing values)
df_cleaned = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_cleaned)

# Part III - Handling DataFrames and Extracting Information
# (3) Count of different countries
unique_countries = df['location'].nunique()
print("\nNumber of unique countries:", unique_countries)

# (4) Create an array of unique country names
country_names = df['location'].unique()
print("Array of unique country names:\n", country_names)

# (5) Create a DataFrame with the total number of vaccinations for each country
total_vaccinations_per_country = df.groupby('location')['total_vaccinations'].sum().reset_index()
print("\nTotal vaccinations for each country:\n", total_vaccinations_per_country)

# (6) Create a DataFrame with the type of vaccinations and their respective counts for each country
manufacturer_counts = df.groupby(['location', 'vaccine'])['total_vaccinations'].sum().reset_index()
print("\nVaccination counts by manufacturer and country:\n", manufacturer_counts)

# Part IV - Data Visualization
# (7) Visualize the total number of vaccinations for each country
plt.figure(figsize=(12, 6))
plt.bar(total_vaccinations_per_country['location'], total_vaccinations_per_country['total_vaccinations'], color='skyblue')
plt.xlabel("Country")
plt.ylabel("Total Vaccinations")
plt.title("Total Number of Vaccinations for Each Country")
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.tight_layout()       # Adjust layout to fit labels
plt.show()

'''
'''
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Part I - Data Cleaning
# 1. Load the dataset
df = pd.read_csv('ClimateChangeData.csv')

# (a) Check the number of records
print("Number of records:", df.shape[0])

# (b) Check for missing values
missing_values = df.isnull().sum().sum()
print("Total missing values:", missing_values)

# (c) Plan for handling missing values - here filling with mean as an example
df_filled = df.fillna(df.mean())

# (d) List of countries with missing values
countries_with_missing = df[df.isnull().any(axis=1)]['Country'].unique()
print("Countries with missing values:", countries_with_missing)

# Part II - Overview of Dataset
# (a) Count of unique countries
unique_countries = df_filled['Country'].nunique()
print("Number of unique countries:", unique_countries)

# (b) Add a column for "Mean Temp. Change" per country
df_filled['Mean Temp. Change'] = df_filled.groupby('Country')['Temperature Change'].transform('mean')

# (c) Create a new DataFrame for yearly mean temperature change
yearly_means = df_filled.groupby('Year')['Temperature Change'].mean().reset_index()
yearly_means.columns = ['Year', 'Mean Temp. Change']

# Part III - Visualization
# 1. Past decade temperature change per country
past_decade_data = df_filled[df_filled['Year'] >= 2013]
plt.figure(figsize=(12, 8))
past_decade_means = past_decade_data.groupby('Country')['Temperature Change'].mean()
past_decade_means.plot(kind='bar', color='skyblue')
plt.xticks(rotation=45)
plt.xlabel("Country")
plt.ylabel("Mean Temperature Change (°C)")
plt.title("Mean Temperature Change Over the Past Decade by Country")
plt.show()

# 2. Global yearly temperature change trend
plt.figure(figsize=(12, 6))
plt.plot(yearly_means['Year'], yearly_means['Mean Temp. Change'], marker='o')
plt.xlabel("Year")
plt.ylabel("Mean Temperature Change (°C)")
plt.title("Global Average Temperature Change (1967-2023)")
plt.grid(True)
plt.show()

# 3. Top 5 countries with the highest mean temperature change
top_countries = df_filled.groupby('Country')['Mean Temp. Change'].mean().nlargest(5)
print("Top 5 countries with the highest mean temperature change:\n", top_countries)

# 4. Temperature change over time for the top 5 countries
plt.figure(figsize=(12, 8))
for country in top_countries.index:
    country_data = df_filled[df_filled['Country'] == country]
    plt.plot(country_data['Year'], country_data['Temperature Change'], label=country)

plt.xlabel("Year")
plt.ylabel("Temperature Change (°C)")
plt.title("Temperature Change Over Time for Top 5 Countries")
plt.legend()
plt.show()

# Part IV - Additional Analysis (Optional)
# Example: Decadal comparison for the top 5 countries
df_filled['Decade'] = (df_filled['Year'] // 10) * 10
top5_decade_means = df_filled[df_filled['Country'].isin(top_countries.index)].groupby(['Country', 'Decade'])['Temperature Change'].mean().unstack()
top5_decade_means.T.plot(kind='bar', figsize=(12, 8))
plt.xlabel("Decade")
plt.ylabel("Mean Temperature Change (°C)")
plt.title("Mean Temperature Change per Decade for Top 5 Countries")
plt.xticks(rotation=45)
plt.legend(title="Country")
plt.show()

'''
'''
import numpy as np

A = np.zeros((1, 5))
print("Array A:")
print(A)

B = np.ones((3, 4), dtype=int)
print("\nArray B:")
print(B)

C = np.array([
    [0, 0, 0],
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1],
    [0, 0, 0]
], dtype=int)
print("\nArray C (representing 'I'):")
print(C)

print("\nSizes and shapes:")
print("A:", A.size, "Shape:", A.shape)
print("B:", B.size, "Shape:", B.shape)
print("C:", C.size, "Shape:", C.shape)

B_transposed = B.T
print("\nTransposed Array B:")
print(B_transposed)

B_transposed[:, 1] = 1 - B_transposed[:, 1]
print("\nB_transposed with second column values inverted:")
print(B_transposed)

# Adjust `B_transposed` to be of size 4x5 by padding with 1s for correct alignment
B_transposed_adjusted = np.pad(B_transposed, ((0, 0), (1, 1)), constant_values=1)
T = np.vstack((A, B_transposed_adjusted))
print("\nCombined Array representing the letter 'T':")
print(T)

# Create a space (column of 1s) between "I" and "T"
space = np.ones((C.shape[0], 1), dtype=int)
IT = np.hstack((C, space, T))
print("\nCombined Array representing 'IT':")
print(IT)

# Display the combined array
import matplotlib.pyplot as plt

plt.imshow(IT, cmap='gray', vmin=0, vmax=1)
plt.axis('off')
plt.show()

'''
'''

a = 28
b = 15

print(a)
print(a,b)
print(a, b, sep=',')
print(str(a) + ',' + str(b))  # Corrected to avoid error
print()
print('SLTC')
print()
print('Programming Concepts')
'''
'''
for i in range(1, 6):
    print("*" * (2 * i - 1))

    
for i in range(1, 6):
    print("*" * i)
for i in range(4, 0, -1):
    print("*" * i)
'''
'''
for i in range(1, 6):
    print(str(i) * i)


for i in range(1, 6):
    print(" " + str(i) * i)
'''
'''
for i in range(5, 0, -1):
    print(str(i) * i)


i = 0
while i < 3:
    print(i)
    i += 1
'''
'''
n = int(input("Enter a starting number: "))
while n > 0:
    print(n)
    n -= 1
    print("Liftoff!")
'''

'''
total = 0
count = 10
i = 0
while i < count:
    marks = float(input(f"Enter marks for student {i+1}: "))
    total += marks
    i += 1

average = total / count
print("Average marks:", average)
'''

'''
# Initialize a variable to store the sum
secret_code = 0

# Loop through numbers from 1 to 20
for number in range(1, 21):
    # Check if the number is even
    if number % 2 == 0:
        # Add the even number to the sum
        secret_code += number

# Print the final sum
print(f"The secret numeric code is: {secret_code}")
'''

'''
# List of numbers
code = [3, 1, 20]

# Initialize an empty list to store letters
letters = []

# Using a for loop to convert numbers to letters
for num in code:
    letter = chr(num + 64)  # Convert number to letter (A=1, B=2, ..., Z=26)
    letters.append(letter)

# Print the result
print("Message with for loop:", "".join(letters))

# List of numbers
code = [3, 1, 20]

# Initialize an empty list to store letters
letters = []
index = 0

# Using a while loop to convert numbers to letters
while index < len(code):
    num = code[index]
    letter = chr(num + 64)  # Convert number to letter
    letters.append(letter)
    index += 1  # Move to the next index

# Print the result
print("Message with while loop:", "".join(letters))

'''
'''
# List of products with stock levels
products = [("Laptop", 55), ("Mouse", 12), ("Keyboard", 30), ("Monitor", 3), ("Printer", 65)]

# Loop through each product
for product, stock in products:
    # Categorize based on stock quantity
    if stock >= 50:
        status = "Fully Stocked"
    elif 20 <= stock < 50:
        status = "Moderate Stock"
    elif 5 <= stock < 20:
        status = "Low Stock"
    else:
        status = "Out of Stock"
    
    # Print the result for each product
    print(f"Product: {product}, Stock Level: {stock}, Status: {status}")
'''
'''
n = int(input('Input a number: '))  # Get input from user

for i in range(n):  # Loop from 0 to n-1
    print(i)  # Print the current value of i
    if i > 9:  # Check if i is greater than 9
        break  # Exit the loop if i is greater than 9

print('done')  # Print 'done' after exiting the loop
'''
'''
total = 0  # Initialize the total sum

for i in range(1, 11):  # Loop from 1 to 10
    print(i)  # Print the current value of i
    if i % 2 == 0:  # Check if i is even
        continue  # Skip the rest of the loop for even numbers
    
    total = total + i  # Add the odd numbers to the total

print(f'Total: {total}')  # Print the total sum of odd numbers
'''
'''
import math

# Example: Cosine of 0 radians
result = math.cos(0)
print(result)  # Output: 1.0

'''
'''
from turtle import *

#speed(0)
# Outer loop runs 120 times
for i in range(120):
    # Inner loop to draw a square
    for j in range(4):
        forward(100)  # Move forward by 100 units
        left(90)      # Turn left by 90 degrees (right angle)

    left(3)  # Turn left by 3 degrees after drawing each square

'''
'''
# Open a file for writing
file = open('test.txt', 'w')  # 'w' mode opens the file for writing, creating it if it doesn’t exist
file.write('SLTC Research University\n')
file.write('Meepe\n')
file.close()  # Close the file to save changes

# Open an existing file in append mode
file = open('test.txt', 'a')  # 'a' mode opens the file to add content at the end
file.write('Padukka\n')
file.write('Sri Lanka\n')
file.close()  # Close the file to save changes

# Open file for reading
file = open('test.txt', 'r')  # 'r' mode opens the file for reading
# Reading the file line by line
for line in file:
    print(line, end='')  # Print each line with end='' to avoid double line spacing
file.close()  # Close the file after reading

# Open file for reading
file = open('test.txt', 'r')
while True:
    line = file.readline()  # Read the next line
    if len(line) == 0:  # If the line is empty, end of file is reached
        break
    print(line, end='')  # Print the line
file.close()  # Close the file after reading

'''
'''
# Creating a list with a set of numbers
numberList = [11, 2, 23, 45, 15]

# Print the list
print("Initial list:", numberList)

# Print each item in the list
print("Items in the list:")
for i in numberList:
    print(i)

# Length of the list
print("Length of the list:", len(numberList))

# Access the first item of the list
print("First item of the list:", numberList[0])

# Adding an item to the end of the list
numberList.append(29)
print("List after appending 29:", numberList)

# Adding an item at a specific position in the list
numberList.insert(1, 20)  # Add 20 as the second item (index 1)
print("List after inserting 20 at index 1:", numberList)

# Changing values in the list
numberList[1] = 100  # Change the second item to 100
print("List after changing the second item to 100:", numberList)

# Sorting the list in ascending order
numberList.sort()
print("List sorted in ascending order:", numberList)

# Sorting the list in descending order
numberList.sort(reverse=True)
print("List sorted in descending order:", numberList)

# Removing an item based on its index
del numberList[0]  # Remove the first item
print("List after removing the first item:", numberList)

# Removing an item based on its value
# If the value does not exist in the list, it will raise a ValueError.
# To avoid this, we can check if the value is in the list before removing it.
value_to_remove = 100
if value_to_remove in numberList:
    numberList.remove(value_to_remove)  # Remove the item with value 100
    print(f"List after removing {value_to_remove}:", numberList)
else:
    print(f"Value {value_to_remove} not found in the list.")

# Removing the entire list
del numberList
# Trying to print numberList after deletion will raise a NameError, as the list no longer exists.
# Uncomment the next line to see the error:
# print(numberList)
'''
'''
# Creating a tuple with a set of numbers
numberTuple = (11, 2, 23, 45, 15)

# Print the tuple
print("Initial tuple:", numberTuple)

# Print each item in the tuple
print("Items in the tuple:")
for i in numberTuple:
    print(i)

# Length of the tuple
print("Length of the tuple:", len(numberTuple))

# Access the first item of the tuple
print("First item of the tuple:", numberTuple[0])

# Delete the tuple
del numberTuple

# Trying to print numberTuple after deletion will raise a NameError, as the tuple no longer exists.
# Uncomment the next line to see the error:
# print(numberTuple)
'''
'''
# Creating a set with a set of numbers
numberSet = {11, 2, 23, 45, 15}

# Print the set
print("Initial set:", numberSet)

# Print each item in the set
print("Items in the set:")
for i in numberSet:
    print(i)

# Length of the set
print("Length of the set:", len(numberSet))

# Add an item to the set
numberSet.add(6)
print("Set after adding 6:", numberSet)

# Add multiple items to the set
numberSet.update([6, 7, 8])  # Adds 6, 7, and 8 to the set
print("Set after adding multiple items [6, 7, 8]:", numberSet)

# Remove an item from the set using remove() - raises error if item doesn't exist
numberSet.remove(2)
print("Set after removing 2:", numberSet)

# Remove an item from the set using discard() - no error if item doesn't exist
numberSet.discard(2)  # 2 has already been removed, so discard() will do nothing here
print("Set after discarding 2:", numberSet)

# Delete the entire set
del numberSet

# Trying to print numberSet after deletion will raise a NameError, as the set no longer exists.
# Uncomment the next line to see the error:
# print(numberSet)
'''

'''
# Creating a set with numbers in ascending order
numbers_set = {1, 3, 5, 7, 9}
print(numbers_set)

'''
'''
# Step 1: Create a dictionary
numberDict = {
    'one': 'ichi',
    'two': 'ni',
    'three': 'san'
}

# Step 2: Print the dictionary
print(numberDict)

# Step 3: Print keys in the dictionary
for i in numberDict:
    print(i)

# Step 4: Print values in the dictionary
for i in numberDict.values():
    print(i)

# Step 5: Print items in the dictionary
for i in numberDict.items():
    print(i)

# Step 6: Length of the dictionary
print(len(numberDict))

# Step 7: Access key 'one'
print(numberDict['one'])
print(numberDict.get('one'))

# Step 8: Add new item
numberDict['four'] = 'yon'

# Step 9: Change value for key 'four'
numberDict['four'] = 'shi'

# Step 10: Remove key 'two'
del numberDict['two']

# Final dictionary
print(numberDict)

'''
'''
# Step 1: Create a dictionary
numberDict = {
    'one': 'ichi',
    'two': 'ni',
    'three': 'san'
}

# Step 2: Print the dictionary
print(numberDict)

# Step 3: Print keys in the dictionary
for i in numberDict:
    print(i)

# Step 4: Print values in the dictionary
for i in numberDict.values():
    print(i)

# Step 5: Print items in the dictionary
for i in numberDict.items():
    print(i)

# Step 6: Length of the dictionary
print(len(numberDict))

# Step 7: Access key 'one'
print(numberDict['one'])
print(numberDict.get('one'))

# Step 8: Add new item
numberDict['four'] = 'yon'

# Step 9: Change value for key 'four'
numberDict['four'] = 'shi'

# Step 10: Remove key 'two'
del numberDict['two']

# Final dictionary
print(numberDict)


# Sorting dictionary by keys (ascending)
for key in sorted(numberDict):
    print(f"{key}: {numberDict[key]}")

# Sorting dictionary by keys (descending)
for key in sorted(numberDict, reverse=True):
    print(f"{key}: {numberDict[key]}")
'''

'''
inventory = [('apple', 50, 10), ('banana', 30, 20), ('orange', 40, 15)]
print(inventory)

inventory[0] = ('apple', 50, inventory[0][2] - 3)  # Reduces apple quantity by 3
print(inventory)

with open('inventory_backup.txt', 'w') as file:
    for item in inventory:
        file.write(f"{item[0]}, {item[1]}, {item[2]}\n")
'''

'''
students_grades = [('Kasun', 85), ('Nimal', 78), ('Sunil', 92)]
print(students_grades)

students_grades[0] = ('Kasun', students_grades[0][1] + 5)  # Adds 5 points to Kasun's grade
print(students_grades)

with open('grades_backup.txt', 'w') as file:
    for student in students_grades:
        file.write(f"{student[0]}, {student[1]}\n")
'''
'''
tasks = ["Wake up", "Brush teeth", "Eat breakfast", "Go to work"]

print(tasks)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(days)

'''
'''
def addNumbers(a, b):
    return a + b

# Call the function with arguments 5 and 3
result = addNumbers(5, 3)
print(result)  # Output: 8
'''
'''
# Number of rows
rows = 4

for i in range(1, rows + 1):
    # Print leading spaces for alignment
    print(" " * (rows - i), end="")
    # Print the number 'i' repeated (2 * i - 1) times
    print(str(i) * (2 * i - 1))

# Number of rows
rows = 3

for i in range(rows, 0, -1):
    # Print leading spaces for alignment
    print(" " * (rows - i), end="")
    # Print the number 'i' repeated (2 * i - 1) times
    print(str(i) * (2 * i - 1))
'''
'''
def calculate(num1, num2):
    return num1 + num2, num1 - num2, num1 * num2

# Call the function with 10 and 4
result = calculate(10, 4)

print(result)

def calculate(num1, num2):
    return {
        "sum": num1 + num2,
        "difference": num1 - num2,
        "product": num1 * num2,
        "quotient": num1 / num2 if num2 != 0 else "undefined"
    }

# Call the function with the numbers 8 and 5
results = calculate(8, 5)
print("Results:")
for key, value in results.items():
    print(f"{key.capitalize()}: {value}")
# Output:
# Sum: 13
# Difference: 3
# Product: 40
# Quotient: 1.6
'''
'''
# Get input from the user
number = int(input("Enter a number: "))

# Initialize sum for even numbers
even_sum = 0

# Loop through numbers from 1 to the entered number
print("Even numbers from 1 to", number, "are:")
for i in range(1, number + 1):
    if i % 2 == 0:
        print(i)
        even_sum += i

# Print the sum of all even numbers
print("Sum of even numbers:", even_sum)

'''
'''
print("Multiples of 3 from 1 to 30:")
for i in range(3, 31, 3):
    print(i)

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
            return False
    return True

print("Multiples of 3 that are also prime numbers:")
for i in range(3, 31, 3):
    if is_prime(i):
        print(i)
'''
'''
# Check for prime multiples of 3
print("Multiples of 3 that are also prime numbers:")
for i in range(3, 31, 3):
    if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1)):
        print(i)
'''
'''
# Loop through numbers from 1 to 15
for i in range(1, 16):
    print(i)
    if i % 6 == 0:
        continue
'''

'''
number = int(input("Enter a number: "))
total_sum = sum(range(1, number + 1))
print(f"The sum of numbers from 1 to {number} is: {total_sum}")
'''



s = 'Dialog'

print(s[3:6:2])   # Output: 'l'

print(s[3:len(s):2])   # Output: 'lg'

import os

# Specify the directory containing the files
directory = "C:\\Users\\rlnag\\OneDrive\\Desktop\\tutorial 3"

for filename in os.listdir(directory):
    # Build the old and new file paths
    old_file = os.path.join(directory, filename)
    if os.path.isfile(old_file):
        # Replace spaces with hyphens and convert to lowercase
        new_filename = filename.replace(" ", "-").lower()
        new_file = os.path.join(directory, new_filename)
        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed: {filename} -> {new_filename}")
