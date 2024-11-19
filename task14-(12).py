fhand = open("first.txt")

count = 0

for line in fhand:

    print(line.rstrip())

    count = count +1

print('lines count:',count)

fhand.close()