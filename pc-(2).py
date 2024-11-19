#Tutorial 8

#part1
#1
def add(n1,n2):
    return(n1+n2)

ans = add(5,3)

print(ans)

#1#a

def prd(n1,n2):
    return(n1*n2)

ans = prd(7,4)

print(ans)

#2

def greet (name):
    return('hello,'+name)

print(greet('guest'))


def greet (name):
    return('hello,'+name)

print(greet('Manilka'))

#3
def cal (n1,n2):
    sum = n1 + n2
    dif = n1 - n2
    prd = n1*n2
    return sum,dif,prd

result =cal(10,4)

print(result)


#3#a

def cal (n1,n2):
    sum = n1 + n2
    dif = n1 - n2
    prd = n1*n2
    qut = n1/n2

    return{
        'sum':sum,
        'difference':dif,
        'product':prd,
        'quotient':qut }

result = cal(8,5)

print(result)



#part2

#

#1

#local variable  accessed inside function only
#global variable accessed modified global variable inside function and outside function

def inner_fun ():
    local_var = 8
    print('inside the funcion:',local_var)

inner_fun()



    
global_var = 100  

def function():
    print("Inside the function:", global_var) 

function()  
print("Outside the function:", global_var)  

#2
num = 8

def change_value():
    global num
    num = 10

change_value()
print('change value:',num)

#3

num = 5

def  change_value():
    global num
    num = 10

change_value ()

print('change value:',num)

    