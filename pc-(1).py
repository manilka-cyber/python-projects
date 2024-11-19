# PART I - Grocery Store Inventory Management

# 1. A list in Python is an ordered collection of items, which can be changed or modified (mutable).
#    A tuple is similar to a list, but it is immutable (cannot be changed after creation).

# 2. Create a list of tuples where each tuple contains the item name, price, and quantity.
inventory = [
    ('apple', 50, 10),
    ('banana', 30, 20),
    ('orange', 25, 15)
]

# Display the list of all items
print("Grocery Store Inventory:")
for item in inventory:
    print(item)

# 3. A customer buys 3 apples, write a function to update the quantity of apples by reducing it by 3.
def update_quantity(item_name, quantity_purchased, inventory):
    updated_inventory = []
    for item in inventory:
        name, price, quantity = item
        if name == item_name:
            quantity -= quantity_purchased  # Reduce the quantity by the purchased amount
        updated_inventory.append((name, price, quantity))
    return updated_inventory

inventory = update_quantity('apple', 3, inventory)

# Display the updated inventory
print("\nUpdated Inventory:")
for item in inventory:
    print(item)

# 4. After updating the inventory, save the updated list into a text file called inventory_backup.txt
with open("inventory_backup.txt", "w") as file:
    for item in inventory:
        file.write(f"{item}\n")

print("\nInventory saved to inventory_backup.txt")


# PART II - Student Grades Management

# 1. A tuple in Python is an ordered collection of elements, similar to a list, but immutable.
#    Real-world example: A tuple can represent an (x, y) coordinate on a 2D plane, where the values can't be changed.

# 2. Create a list of tuples where each tuple contains a student's name and their grade.
student_grades = [
    ('Kasun', 85),
    ('Nimal', 78),
    ('Sunil', 92)
]

# Display the list of all students and their grades
print("\nStudent Grades:")
for student in student_grades:
    print(student)

# 3. A student named Kasun improves his grade by 5 points. Write a function to update his grade.
def update_grade(student_name, grade_increase, student_grades):
    updated_grades = []
    for student in student_grades:
        name, grade = student
        if name == student_name:
            grade += grade_increase  # Increase the grade by the specified points
        updated_grades.append((name, grade))
    return updated_grades

student_grades = update_grade('Kasun', 5, student_grades)

# Display the updated list of students and their grades
print("\nUpdated Student Grades:")
for student in student_grades:
    print(student)

# 4. Save the updated list of students and their grades into a text file called grades_backup.txt
with open("grades_backup.txt", "w") as file:
    for student in student_grades:
        file.write(f"{student}\n")

print("\nGrades saved to grades_backup.txt")
