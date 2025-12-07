import numpy as np

#tableau 1 dimension
vecteur = np.array([1, 2, 3, 4, 5])

print("tableau 1 dimension = \n")
print("vecteur 1 dim = \n", vecteur)
print(f"le nb de dim ce vecteur = {vecteur.ndim}")
print(f"la forme de ce vecteur = {vecteur.shape}")

#tableau 2 dimensions
vecteur2D = np.array([[1,2,3],[4,5,6]])
print("\n tableau 2 dimensions = \n")
print("vecteur 2 dim = \n", vecteur2D)
print(f"le nb de dim ce vecteur2D = {vecteur2D.ndim}")
print(f"la forme de ce vecteur2D = {vecteur2D.shape}")

#tableau 3 dimensions
vecteur3D = np.array([[[1,1,1],[2,2,2],[3,3,3]], [[4,4,4],[5,5,5], [6,6,6]]])
print("\n tableau 3 dimensions = \n")
print("vecteur 3 dim = \n", vecteur3D)
print(f"le nb de dim ce vecteur3D = {vecteur3D.ndim}")
print(f"la forme de ce vecteur3D = {vecteur3D.shape}")


#type et taille d'un tableau numpy

vecteur_1 = np.array([[1,2,3,4],[5,6,7,8]], dtype='int16')
vecteur_2 = np.array([[1,2,3,4],[5,6,7,8]], dtype='float32')
vecteur_3 = np.array([[1,2,3,4],[5,6,7,8]], dtype='float64')

print ("\nType et taille d'un tableau numpy \n")
print("\nTableau vecteur_1 = \n", vecteur_1)
print(f"Le type de vecteur_1 = {type(vecteur_1)}")
print(f"le type des elements du vecteur_1 = {vecteur_1.dtype}") 
print(f"la taille en octet de chaque element = {vecteur_1.itemsize} octets")
print(f"Le nombre d'element dans ce vecteur_1 = {vecteur_1.size}")
print(f"La taille totale en octets de ce vecteur_1 = {vecteur_1.nbytes} octets")

print("\nTableau vecteur_2 = \n", vecteur_2)
print(f"Le type de vecteur_2 = {type(vecteur_2)}")
print(f"le type des elements du vecteur_2 = {vecteur_2.dtype}") 
print(f"la taille en octet de chaque element = {vecteur_2.itemsize} octets")
print(f"Le nombre d'element dans ce vecteur_2 = {vecteur_2.size}")
print(f"La taille totale en octets de ce vecteur_2 = {vecteur_2.nbytes} octets")

print("\nTableau vecteur_3 = \n", vecteur_3)
print(f"Le type de vecteur_3 = {type(vecteur_3)}")
print(f"le type des elements du vecteur_3 = {vecteur_3.dtype}") 
print(f"la taille en octet de chaque element = {vecteur_3.itemsize} octets")
print(f"Le nombre d'element dans ce vecteur_3 = {vecteur_3.size}")
print(f"La taille totale en octets de ce vecteur_3 = {vecteur_3.nbytes} octets")
