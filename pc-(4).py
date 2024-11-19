'''lengths = []

while True:
    length = int(input("Enter the length of the machine part (or -999 to stop): "))
    if length == -999:
        break
    lengths.append(length)

if lengths:
    # Initialize max, min, and total
    max_length = lengths[0]
    min_length = lengths[0]
    total = 0

    for length in lengths:
        if length > max_length:
            max_length = length
        if length < min_length:
            min_length = length
        total += length

    average_length = total / len(lengths)

    print(f"Maximum Length: {max_length}")
    print(f"Minimum Length: {min_length}")
    print(f"Average Length: {average_length:.2f}")
else:
    print("No lengths were entered.")

# Collecting book information
book_title = input("Enter the name of the book: ")
author = input("Enter the author of the book: ")
published_day = int(input("Day of Published: "))
published_month = input("Month? ")
published_year = int(input("Year? "))

# Display the collected information
print("\nBook Information:")
print(f"Book Title: {book_title}")
print(f"Author: {author}")
print(f"Published on: {published_day} {published_month} {published_year}")

# Collecting user name
name = input("Enter your name: ")

# Displaying the output with blank lines
print(f"\nHello, {name}!\n")
print("Welcome to the family\n")'''

'''start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

while start <= end:
    if start % 2 == 0:
        print(start)
    start += 1'''
'''i = 0
while i < 3:
    print(i)
    
# List of products and their stock levels
products = [("Laptop", 55), ("Mouse", 12), ("Keyboard", 30), ("Monitor", 3), ("Printer", 65)]

# Loop through each product and classify based on stock levels
for product, stock in products:
    # Check stock status and classify accordingly
    if stock >= 50:
        status = "Fully Stocked"
    elif 20 <= stock < 50:
        status = "Moderate Stock"
    elif 5 <= stock < 20:
        status = "Low Stock"
    else:  # stock < 5
        status = "Out of Stock"
    
    # Print the product name and its stock status
    print(product ,status)'''

# Creating a list of tuples for students and their grades
grades = [
    ('Kasun', 85),
    ('Nimal', 78),
    ('Sunil', 92),
    ('Ayesha', 88)
]

# Display the list of all students and their grades
print("Students and their Grades:")
for student in grades:
    print(student)

# Save the updated inventory to a file
with open('inventory_backup.txt', 'w') as file:
    for item in grades:
        file.write(f"{item}\n")  # Write each item on a new line

print("\nUpdated inventory saved to inventory_backup.txt")

a = 1234.56789
print(a)                     # Output: 1234.56789
print('%d' % a)              # Output: 1234 (rounds to integer)
print('%.2f' % a)            # Output: 1234.57 (2 decimal places)
print('%7.2f' % a)           # Output: 1234.57 (7 width, 2 decimals)
print('Price Rs. %.2f' % a)  # Output: Price Rs. 1234.57
print('%.2f and %.1f' % (a, 3.1415926))  # Output: 1234.57 and 3.1


n = 5 

for i in range (n):
    for j in range (i+1):
        print(n-j,end= " ")
    print()