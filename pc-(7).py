'''

# Getting user input for favorite singer and song
favorite_singer = input("Enter your favorite singer: ")
favorite_song = input("Enter your favorite song: ")

# Printing the message
print(f"Your favorite singer is {favorite_singer} and your favorite song is {favorite_song}.")

'''

'''


# Getting a number from the user
number = int(input("Enter a number: "))

# Checking if the number is even or odd
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
'''

'''

# Getting the number of study hours
hours = int(input("Enter the number of hours you studied: "))

# Assigning a grade based on the number of hours
if hours < 2:
    grade = "Poor"
elif 2 <= hours <= 4:
    grade = "Fair"
elif 5 <= hours <= 7:
    grade = "Good"
else:
    grade = "Excellent"

# Printing the grade
print("Your study efficiency grade is:", grade)

'''

'''
# Using a while loop to print numbers from 10 to 1
number = 10
while number > 0:
    print(number)
    number -= 1

'''

'''


# Initializing sum
total = 0

# Using a loop to add numbers until a negative number is entered
while True:
    number = int(input("Enter a positive number (negative to stop): "))
    if number < 0:
        break
    total += number

# Printing the total sum
print("The sum of all positive numbers entered is:", total)


'''

'''

# Initializing total marks
total_marks = 0

# Looping to get marks for 10 students
for i in range(10):
    marks = float(input(f"Enter marks for student {i+1}: "))
    total_marks += marks

# Calculating average
average_marks = total_marks / 10

# Printing the average marks
print("The average marks of the ten students is:", average_marks)

'''

'''

# Using a for loop to print numbers from 1 to 5
for i in range(1, 6):
    print(i)

'''

'''

# Getting a number from the user
number = int(input("Enter a number: "))

# Calculating the sum from 1 to the entered number
total_sum = sum(range(1, number + 1))

# Printing the total sum
print("The sum of numbers from 1 to", number, "is:", total_sum)

'''




# Defining the function
def multiply_numbers(x, y):
    return x * y

# Calling the function with arguments 4 and 7
result = multiply_numbers(4, 7)
print("The product of 4 and 7 is:", result)
