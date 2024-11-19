'''
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
        continue 

for i in range (1,16):
     

    if % 6==0:
     print(i)

    continue

'''
from PIL import Image

img = Image.open("Manilka_Sooriyabandara_A_confident_businesswoman_with_long,_dark_hair,_we_a7291214-599d-4505-8124-c49ba0948c4b.png")
img = img.resize((600, 400))
img.save("resized_image.jpg")



    
    











    