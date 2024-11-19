n = int(input("enter a number:"))

total = 0

for i in range (2,n + 1,2):

    print (i)

    total = total + i

print (total)
 
for i in range (3,31,3):

    print(i)


list = [2,3,5,7,11,13,17,19,23,29]

for i in range (3,31):
    if i % 3 == 0:
        if i in list:
            print(i)

#part 2

n = int(input('enter a number'))

for i in range (1,21):
    print(i)
    if i == n:
        break

n = int(input('enter a number:'))    
for i in range (1,21):

    print(i)

    if i == n :
        break

    if i != n :
           continue 

for i in range (1,16):
     print(i)
     
     if i % 6==0:
      continue



    
    











    