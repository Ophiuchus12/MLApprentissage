#modification dataframe avec conditions 

import pandas as pd 

dataSet = pd.read_csv('Data/ozone.csv')

print ("Modification dataframe avec conditions \n")
print (f"dataSet head 5 = \n{dataSet.head(5)}")

dataSet['Résultat'] = False

dataSet.loc [abs(dataSet['O3obs']- dataSet['MOCAGE']) < 2.5, 'Résultat'] = True
print (f"\ndataSet after modification = \n{dataSet.head(5)}")
#réorganisation des colonnes
columns = list(dataSet.columns.values)
lenght = len (columns)
print (f"\ncolumns before reorganization = \n{lenght} \n{columns}")
dataSetOrganized = dataSet[columns[0:3]+ [columns[-1]] + columns[3:10]]
print (f"\ndataSet after reorganization = \n{dataSetOrganized.head(5)}")

#Ajout de ligne dans un dataframe
print(f"Affichage des 3 denrieres lignes avant l'ajout \n {dataSet.tail(3)}")
dataSet = pd.concat([dataSet, pd.DataFrame([{
    'JOUR': '0', 'O3obs': 50.0, 'MOCAGE': 48.0, 'TEMPE': 20.0, 'RMH2O': 20.0, 'NO2': 20.0, 'NO': 15.0, 
    'STATION': 'Aix', 'VentMOD': 0.5, 'VentANG': 0.5, 'Résultat': True}])], ignore_index=True)
print(f"\nAffichage des 3 denrieres lignes apres l'ajout \n {dataSet.tail(3)}")

#Tri avec 1 critère 
#Tri des valeurs de la colonne NO2 par ordre décroissant
dataSetSorted = dataSet.sort_values('NO2', ascending=False)
print (f"\ndataSet sorted by NO2 descending = \n{dataSetSorted.head(5)}")

#Tri avec plusieurs critères
#Tri des valeurs de la colonne O3obs par ordre croissant et TEMPE par ordre décroissant
sortByO3obsTEMPE = dataSet.sort_values(['O3obs', 'TEMPE'], ascending=[True, False])
print (f"\ndataSet sorted by O3obs ascending and TEMPE descending = \n{sortByO3obsTEMPE.head(25)}")