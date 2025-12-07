import numpy as np

#Initialisation de tableaux numpy avec des valeurs spécifiques

#Initialisation de tableaux numpy 
vecteur_1 = np.zeros(10)
vecteur_2 = np.zeros(10, dtype='int32')
#3 lignes et 5 colonnes
vecteur_3 = np.ones((3,5), dtype='int16')

print("Initialisation de tableaux numpy \n")
print("Tableau vecteur_1 = \n", vecteur_1)
print("Tableau vecteur_2 = \n", vecteur_2)
print("Tableau vecteur_3 = \n", vecteur_3)

#Initialisation de tableaux numpy avec des valeurs spécifiques
#2 lignes et 4 colonnes remplies avec la valeur 7
vecteur_4 = np.full((2,4),7)
#Tableau de meme forme que vecteur_4 rempli avec la valeur 9
vecteur_5 = np.full_like(vecteur_4,9)
#Matrice identite de taille 3x3
vecteur_6 = np.identity(3)

print("\nTableau vecteur_4 = \n", vecteur_4)
print("Tableau vecteur_5 = \n", vecteur_5)
print("Tableau vecteur_6 = \n", vecteur_6)