fhand = open('first.txt')

print('Name of the file:',fhand.name)

print('closed',fhand.closed)

fhand.close()

print('closed',fhand.closed)