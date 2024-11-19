import numpy as np

c =np.random.randint(0,5)

print(c)



letter = input("enter a letter")

vow = "aeiouAEIOU"

if letter in vow  :

    print("yes")

for i in range(1, 6):
    if i % 2 == 0:
        
        continue
    print("*")

num = 5
while num > 0:
    print(num)
    num -= 1
    if num == 3:
        continue
else:
    print("Done")

for i in range(1, 6):
    if i % 2 == 0:
        continue
        print(i)
        
    print("*")



