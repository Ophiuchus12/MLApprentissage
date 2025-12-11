#Lire les données à partir de fichiers avec NumPy
import numpy as np


data_loaded = np.genfromtxt('Data/np_data_tab8.txt', delimiter=',')
print("\nDonnées lues à partir du fichier 'data.txt' : \n", data_loaded)
my_data = data_loaded.astype('int32')
print("\nDonnées converties en int32 : \n", my_data)

# Creer et utiliser des masques booléens
print("\nCréer et utiliser des masques booléens \n")
data_loaded_mask = np.genfromtxt('Data/np_data_tab8.txt', delimiter=',', dtype='int32')
print("Données chargées : \n", data_loaded_mask)
bool_data = data_loaded_mask > 100
print("\nLes indices booléens pour les valeurs > 100 : \n", bool_data)
gt_100 = data_loaded_mask[bool_data]
print("\nLes valeurs > 100 : \n", gt_100)


#Masque avec plusieurs conditions 
data_loaded_multi = np.genfromtxt('Data/np_data_tab8.txt', delimiter=',', dtype='int32')
print("\nDonnées chargées pour le masque multi-conditions : \n", data_loaded_multi)

btw_50_100 = (data_loaded_multi>50) & (data_loaded_multi<100)
print("\nIndices booléens pour les valeurs entre 50 et 100 : \n", btw_50_100)

not_btw_50_100 = ~btw_50_100
print("\nIndices booléens pour les valeurs pas entre 50 et 100 : \n", not_btw_50_100)

values_btw_50_100 = data_loaded_multi[btw_50_100]
print("\nValeurs entre 50 et 100 : \n", values_btw_50_100)

values_not_btw_50_100 = data_loaded_multi[not_btw_50_100]
print("\nValeurs pas entre 50 et 100 : \n", values_not_btw_50_100)

#numpy.any et numpy.all avec des masques booléens
data_loaded_anyll = np.genfromtxt('Data/np_data_tab8.txt', delimiter=',', dtype='int32')
print("\nDonnées chargées pour any et all : \n", data_loaded_anyll)

#Est ce que il y a au moins une valeur > 150 dans la colonne ?
bool_data_any = np.any(data_loaded_anyll > 150, axis=0)
print("\nY a-t-il au moins une valeur > 150 dans chaque colonne ? \n", bool_data_any)

#Est ce que toutes les valeurs sont > 50 dans la colonne ?
bool_data_all = np.all(data_loaded_anyll > 50, axis=0)
print("\nToutes les valeurs sont-elles > 50 dans chaque colonne ? \n", bool_data_all)