Colour = input(' Enter your favourite color is : ')

total_sum = 0 

while True :
     number = int(input( " enter a positive integer (enter a negative number to stop): "))
     if number < 0 :
         break
     total_sum += number
#print(  f"The average marks of the ten students is {total_sum }")

total_marks = 0
for i in range (1,11):
       marks = float(input("Enter the marks for students {i + 1}: "))
       total_marks += marks
average_marks = total_marks/10
#print( f"The average marks of the ten students is :{average_marks}")

for number in range (1,6):
      print (number) 
n = int(input("Enter a number : "))
total_sum = 0
for i in range (1,n +1) :
      total_sum += i
print(f"The sum of numbers from 1 to {n} is: {total_sum}")

def multiply_numbers(x,y) :
     return x * y
result = multiply_numbers(4,7)
print( f"The product of 4 and 7 is : {result}")   
