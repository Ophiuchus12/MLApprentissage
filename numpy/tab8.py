#Lire les données à partir de fichiers avec NumPy
import numpy as np


data_loaded = np.genfromtxt('Data/np_data_tab8.txt', delimiter=',')
print("\nDonnées lues à partir du fichier 'data.txt' : \n", data_loaded)
my_data = data_loaded.astype('int32')
print("\nDonnées converties en int32 : \n", my_data)