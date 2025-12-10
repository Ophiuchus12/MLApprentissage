#Modifier les données dans les tableaux numpy + copier des tableaux numpy

import numpy as np

#modifier les donnees dans le tableau numpy
vecteur = np.array([[1,2,3],[4,5,6], [7,8,9]])

vecteur [1,1]=99
print("Modifier les donnees dans les tableaux numpy \n")
print("Tableau vecteur apres modification = \n", vecteur)

vecteur [0,:]=99
print("\nTableau vecteur apres modification de la ligne 0 = \n", vecteur)

vecteur [:,2]=88
print("\nTableau vecteur apres modification de la colonne 2 = \n", vecteur)


#copier des tableaux numpy
print("\nCopier des tableaux numpy \n")
vecteur_1 = np.array([1,2,3])
vecteur_2 = vecteur_1   #copie par reference -> meme zone memoire, tableau lie
vecteur_2 [0]=99
print("Tableau vecteur_1 apres modification du vecteur_2 = \n", vecteur_1)
print("Tableau vecteur_2 apres modification du vecteur_2 = \n", vecteur_2)


vecteur_3 = np.array([4,5,6])
vecteur_4 = vecteur_3.copy()  #copie par valeur -> nouvelle zone memoire, tableau independant
vecteur_4 [0]=77
print("\nCopie par valeur \n")
print("tableau vecteur_3 apres modification du vecteur_4 = \n", vecteur_3)
print("tableau vecteur_4 apres modification du vecteur_4 = \n", vecteur_4)