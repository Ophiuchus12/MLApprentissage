#Lecture des fichiers de grandes tailles 

import pandas as pd

#Permet de montrer le decoupage en bloc mais là on print tous les blocs
for bloc in pd.read_csv('Data/ozone.csv',chunksize=5):
    print("\nNouveau bloc\n")
    print (bloc)

   