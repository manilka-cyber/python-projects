import numpy as np

#1

# Unbiased die roll simulation (10 rolls)
unbiased_rolls = np.random.randint(1, 7, size=10)
print("Unbiased Die Rolls:", unbiased_rolls)

#2

# Biased die roll simulation (10 rolls with 40% chance for number 5)
biased_rolls = np.random.choice([1, 2, 3, 4, 5, 6], size=10, p=[0.1, 0.1, 0.1, 0.1, 0.4, 0.2])
print("Biased Die Rolls:", biased_rolls)

#3

# Mean for unbiased die
mean_unbiased = np.mean(unbiased_rolls)
print("Mean of Unbiased Rolls:", mean_unbiased)


# Mean for biased die
mean_biased = np.mean(biased_rolls)
print("Mean of Biased Rolls:", mean_biased)

#4

# Median for unbiased die
median_unbiased = np.median(unbiased_rolls)
print("Median of Unbiased Rolls:", median_unbiased)

# Median for biased die
median_biased = np.median(biased_rolls)
print("Median of Biased Rolls:", median_biased)

#5

from scipy import stats

# Mode for unbiased die
mode_unbiased = stats.mode(unbiased_rolls, keepdims=True).mode[0]  # keepdims ensures it returns a numpy array
print("Mode of Unbiased Rolls:", mode_unbiased)

# Mode for biased die
mode_biased = stats.mode(biased_rolls, keepdims=True).mode[0]  # keepdims ensures it returns a numpy array
print("Mode of Biased Rolls:", mode_biased)


#6) Outcome Comparison between Unbiased and Biased Dice
#Here, we will compare the results and discuss how the outcomes differ between the unbiased and biased dice. Based on the mode and probabilities, we expect that the biased die will favor the number 5 more often.

#7) Explanation of Differences in Mean, Median, and Mode
#The mean, median, and mode might differ for the biased die because the probability distribution is skewed towards the number 5. This affects the average (mean), the middle value (median), and the most frequent number (mode).

#Activity 2

#1

#Write a Python program using NumPy to create an array of numbers from 1 to 10.

#2

# Create two NumPy arrays: one with numbers from 1 to 5 and another with numbers from 6 to 10. Perform element-wise addition of the two arrays and display the result.

#3

# Create an array with the values [4, 8, 15, 16, 23, 42]. Calculate and display the mean (average) of the array.

#4

#Create a NumPy array with 12 elements (values from 1 to 12). Reshape it into a 3x4 matrix and display the result.

