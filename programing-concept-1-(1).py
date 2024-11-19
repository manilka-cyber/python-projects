#part 1

def add (n1, n2):

  print(n1 + n2)

add(5,3)

def mul(n1,n2):
  
  print(n1*n2)

mul(7,4)

def greeting(name):
  
  return "hello," + name

print(greeting("Manilka"))

def add(n1,n2):

  return(n1+n2)

ans =add (10,4)

print(ans)

def dif(n1,n2):

  return(n1-n2)

ans2 = dif(10,4)

print(ans2)

def prd (n1,n2):

  return(n1*n2)

ans3 = prd(10,4)

print(ans3)

def qut (n1,n2):

  return(n1/n2)

ans4 = qut(10,4)

print(ans4)

#Local variables are defined inside a function or block, whereas global variable is defined outside of all functions or blocks

counter = 0

def increment_counter():
   
   global counter

   counter += 1

increment_counter()
increment_counter()

print(f"The value of the global counter is now:{counter}")

#2a
num = 5


def change_value():
  
          global num

          num = 10

change_value()

print(f"the value of the global num is :{num}")

  
