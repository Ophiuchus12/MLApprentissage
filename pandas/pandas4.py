#Filtrer les lignes avec une condition spécifique dans un dataframe pandas
import pandas as pd
data = pd.read_csv('Data/ozone.csv')

#acceder au ligne avec index -> iloc / acceder aux lignes avec une condition -> loc

#Filtrer les lignes avec 1 condition
dayOff = data.loc[data['JOUR']==1]
print("Filtrer les lignes avec une condition spécifique dans un dataframe pandas \n")
print(f"dayOff head 5 = \n{dayOff.head(5)}")

#Filtrer les lignes avec plusieurs conditions
result = data.loc[(data['JOUR']==1) & (data['O3obs']>=100)]
print(f"\nresult head 5 = \n{result.head(5)}")

#Filtrer les lignes avec une condition sur les chaines de caractères


result2 = data.loc[(data['JOUR']==1) & 
                    (data['O3obs']>=100)
                   & ((data['STATION'] == 'Ram') |
                      (data['STATION'] == 'Cad'))
                ]

#Reset index après un filtrage
resetData = result2.reset_index()

print(f"\nresult2 = \n{resetData}")

#Ajout de (drop=True) pour supprimer l'ancienne colonne d'index (si plus besoin de garder en mémoire l'index d'origine)
resetData2 = result2.reset_index(drop=True)
print(f"\nresult2 avec drop=True = \n{resetData2}")

#Filtrer avec des valeurs uniques 
unidueStations = data['STATION'].unique()
print(f"\nunidueStations = \n{unidueStations}")

#Filrer avec un regex 
stationA = data.loc[data['STATION'].str.contains('.a.')]
print(f"\nstationA head 5 = \n{stationA.head(5)}")

#Acceder aux variables 
variables = data.columns
print(f"\nvariables = \n{variables}")

#lire une colonne spécifique
myDataSet3 = data['STATION']
print(f"\nmyDataSet3 = \n{myDataSet3.head(5)}")

#Acceder à plusieurs colonnes spécifiques
myDataSet4 = data[['STATION', 'O3obs']]
print(f"\nmyDataSet4 = \n{myDataSet4[0:5]}")

#Acceder aux valeurs d'une cellule spécifique
myDataSet5 = data.iloc [3, 2]  #ligne 3, colonne 2
print(f"\nmyDataSet5 = \n{myDataSet5}")