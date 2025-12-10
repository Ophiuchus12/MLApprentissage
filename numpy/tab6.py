#restructurer un tableau numpy

import numpy as np

mat_1 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
mat_2 = mat_1.reshape((3,4))
mat_3 = mat_1.reshape((2,3,2))

print("Restructurer un tableau numpy \n")
print("Matrice mat_1 = \n", mat_1)
print("\nMatrice mat_2 apres reshape en (3,4) = \n", mat_2)
print("\nMatrice mat_3 apres reshape en (2,3,2) = \n", mat_3)

#Superposition de tableaux numpy

vec_1 = np.array([1,2,3,4,5])
vec_2 = np.array([10,20,30,40,50])
v_stack = np.vstack([vec_1,vec_2])
v_stack_big = np.vstack([vec_1,vec_2,vec_1,vec_2])
h_stack = np.hstack([vec_1,vec_2])

print ("\nSuperposition de tableaux numpy \n")
print("Tableau vec_1 = \n", vec_1)
print("Tableau vec_2 = \n", vec_2)
print("\nSuperposition verticale (vstack) de vec_1 et vec_2 = \n", v_stack)
print("\nSuperposition verticale (vstack) de vec_1 et vec_2 repete = \n", v_stack_big)
print("\nSuperposition horizontale (hstack) de vec_1 et vec_2 = \n", h_stack)