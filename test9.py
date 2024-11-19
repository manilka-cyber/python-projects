import numpy as np
import matplotlib.pyplot as plt
A = np.array([[0,0,0,0,0]])
print(A)
print('*')

B = np.array([[1,1,1,1],[1,1,1,1],[1,1,1,1]])
print(B)
print('*')

C = np.array([[0,0,0],[1,0,1],[1,0,1],[1,0,1],[0,0,0]])
print(C)
print('*')

print(" A shape:", A.shape)
print("Size is A:",A.size)
print(" B shape:", B.shape)
print("Size is B:",B.size)
print(" C shape:", C.shape)
print("Size is C:",C.size)
print('*')
b_t=B.T
print(b_t)
print('*')
b_t[:,1]=0
print(b_t)
print('*')
B_transposed_adjusted = np.pad(b_t, ((0, 0), (1, 1)), 'constant', constant_values=1)
T = np.vstack((A, B_transposed_adjusted))
print(T)
print('*')
space = np.ones((C.shape[0], 1), dtype=int)  
IT = np.hstack([C, space, T])

print("Combined Array representing 'IT':")
print(IT)



plt.imshow(IT, cmap='gray', vmin=0, vmax=1)
plt.axis('off')
plt.show()