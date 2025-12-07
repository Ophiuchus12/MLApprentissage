import numpy as np

#acceder au donnees dans les tableaux numpy

#acceder au donnees dans le tableau de dimension 1
vecteur = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Acceder aux donnees dans le tableau \n")
print("Tableau vecteur = \n", vecteur)
print(f"L'element a l'index 0 = {vecteur[0]}")
print(f"L'element a l'index 4 = {vecteur[[1,5]]}")
print(f"L'element a l'index -1 = {vecteur[[0,-1]]}")
print(f"Les elements de l'index 2 a 5 = {vecteur[2:6]}")
print(f"Les elements de l'index debut a 4 = {vecteur[:5]}")
print(f"Les elements de l'index 5 a fin = {vecteur[5:]}")
print(f"Les elements de l'index 1 a 8 avec un pas de 2 = {vecteur[1:9:2]}")


#acceder au donnees dans le tableau de dimension 2
vecteur2D = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
print("\nAcceder aux donnees dans le tableau 2D \n")
print("Tableau vecteur2D = \n", vecteur2D)
print(f"L'element a l'index (0,0) = {vecteur2D[0,0]}")
print(f"L'element a l'index (2(ligne),3(colonnes)) = {vecteur2D[2,3]}")
print(f"Les elements de la ligne 1 = {vecteur2D[1,:]}")
print(f"Les elements de la colonne 3 = {vecteur2D[:,3]}")
print(f"Les elements de la ligne 0 a 2 et colonne 1 a 3 = \n {vecteur2D[0:3,1:4]}")
print(f"Les elements du tableau vecteur = \n {vecteur2D[:,:]}")

#acceder au donnees dans le tableau de dimension 3
vecteur3D = np.array([[[1,0,0],[0,0,0]], [[0,2,0],[0,0,3]]])
print("\nAcceder aux donnees dans le tableau 3D \n")
print("Tableau vecteur3D = \n", vecteur3D)
#Le premier indice represente la matrice, le deuxieme la ligne et le troisieme la colonne
print(f"L'element a l'index (0,0,0) = {vecteur3D[0,0,0]}")
print(f"L'element a l'index (1,1,2) = {vecteur3D[1,1,2]}")
print(f"Les elements de la matrice 0 = \n {vecteur3D[0,:,:]}")

