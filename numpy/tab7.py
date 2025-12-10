#Statistiques des tableaux numpy

import numpy as np

mat_1 = np.random.randint(-10,10, (5,5))
mat_1_min = np.min(mat_1)
mat_1_max = np.max(mat_1)
#minimum par colonne (axis=0) et maximum par ligne (axis=1)
mat_1_min_axis0 = np.min(mat_1, axis=0)
mat_1_max_axis1 = np.max(mat_1, axis=1)
mat_1_mean = np.mean(mat_1)
mat_1_sum = np.sum(mat_1)
mat_1_mean_axis0 = np.mean(mat_1, axis=0)
mat_1_std = np.std(mat_1, axis=1)

print("Statistiques des tableaux numpy \n")
print("Matrice mat_1 = \n", mat_1)

print("\nMinimum global de mat_1 = \n", mat_1_min)
print("\nMaximum global de mat_1 = \n", mat_1_max)
print("\nMinimum par colonne de mat_1 = \n", mat_1_min_axis0)
print("\nMaximum par ligne de mat_1 = \n", mat_1_max_axis1)
print("\nMoyenne de mat_1 = \n", mat_1_mean)
print("\nSomme de mat_1 = \n", mat_1_sum)
print("\nMoyenne par colonne de mat_1 = \n", mat_1_mean_axis0)
print("\nEcart-type par ligne de mat_1 = \n", mat_1_std)