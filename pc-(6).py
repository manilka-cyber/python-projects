'''
#Part 1
#1 and a

number = int(input("Enter a number: "))


print("Even numbers from 1 to", number, "are:")
even_sum = 0
for i in range(1, number + 1):
    if i % 2 == 0:
        print(i, end=" ")
        even_sum += i


print("\nSum of even numbers from 1 to", number, "is:", even_sum)
'''

'''
#2 and a

print("Multiples of 3 from 1 to 30 are:")
for i in range(3, 31, 3):
    print(i, end=" ")

print("\nMultiples of 3 that are prime numbers:")
for i in range(3, 31, 3):
    is_prime = True
    if i > 1:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
    if is_prime:
        print(i, end=" ")

'''
'''
#Part 3

#1 and a


n = int(input("Enter a number between 1 and 20: "))


print("Numbers from 1 to 20, stopping at", n)
for i in range(1, 21):
    if i == n:
        break
    print(i, end=" ")
print()


print("Numbers from 1 to 20, skipping", n)
for i in range(1, 21):
    if i == n:
        continue
    print(i, end=" ")
print()

'''
#2


print("Numbers from 1 to 15, skipping multiples of 6:")
for i in range(1, 16):
    if i % 6 == 0:
        continue
    print(i,end=" ")

