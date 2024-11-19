#part 1
import matplotlib.pyplot as plt
import numpy as np
A = np.array([0,0,0,0,0])
B = np.array([[1,1,1,1],[1,1,1,1],[1,1,1,1]])
C = np.array([[0,0,0],[1,0,1,],[1,0,1,],[1,0,1,],[0,0,0]])

#1
print("#1")
print(A)
print(A.shape)
print(A.size)

#2
print("#2")
print(B)
print(B.shape)
print(B.size)

#3
print("#3")
print(C)
print(C.shape)
print(C.size)


#part 2
#5
B_T = B.T
print("#5")
print(B_T)


B_T = B.T
#6
for i in range(0,4):
    for j in range(1,2,):
        if B_T[i,j] == 1:
            B_T[i,j] = 0
print("#6")
print(B_T)

#7
B_TU= np.pad(B_T, ((0,0),(1,1)), "constant", constant_values=1)
LT=np.vstack((A,B_TU))
print("#7")
print(LT)

#8
space = np.ones((C.shape[0], 1), dtype=int)
IT= np.hstack((C, space , LT))
print("#8")
print(IT)

plt.imshow(IT, cmap = 'gray', vmin=0, vmax=1)
plt.axis('off')
plt.show()