#Algèbre linéaire avec NumPy
import numpy as np

#opérations de base sur les matrices

vecteur_1 = np.array([1,2,3])

print("Algèbre linéaire avec NumPy \n")
print("Opérations de base sur les matrices \n")
print("Tableau vecteur_1 = \n", vecteur_1)
print (f"Addition de vecteur_1 + 5 = \n {vecteur_1 + 5}")
print (f"Soustraction de vecteur_1 - 2 = \n {vecteur_1 - 2}")
print (f"Multiplication de vecteur_1 * 3 = \n {vecteur_1 * 3}")
print (f"Division de vecteur_1 / 2 = \n {vecteur_1 / 2}")
print (f"Puissance de vecteur_1 ** 2 = \n {vecteur_1 ** 2}")
print (f"Cosinus de vecteur_1 = \n {np.cos(vecteur_1)}")

vecteur_2 = np.array([4,5,6])
print("\nTableau vecteur_2 = \n", vecteur_2)
print(f"vecteur_1*vecteur_2 (multiplication element par element) = \n {vecteur_1 * vecteur_2}")

#Opérations sur les matrices 

mat_1 = np.random.randint(-10,10, (3,4))
mat_2 = np.random.randint(-10,10, (4,2))

print("\nOpérations sur les matrices \n")
print("Matrice mat_1 = \n", mat_1)
print("Matrice mat_2 = \n", mat_2)

result = np.matmul(mat_1, mat_2)
print(f"Multiplication de mat_1 et mat_2 = \n {result}")