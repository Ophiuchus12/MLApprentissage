#Modifier les valeurs d'un dataframe
import pandas as pd

data = pd.read_csv('Data/ozone.csv')


print ("Modifier les valeurs d'un dataframe \n")
print (f"data head 5 = \n{data.head(5)}")
data.iloc[2,2]=999
print (f"\ndata after modification = \n{data.head(5)}")

#Ajouter une variable (colonne) à un dataframe
data['résultat'] = False
print (f"\ndata after adding a new column = \n{data.head(5)}")

data ['Pow2_O3obs'] = pow(data['O3obs'], 2)
print (f"\ndata after adding a new column Pow2_O3obs= \n{data.head(5)}")

#Ajouter une variable (colonne) en fonction d'autres colonnes
#Ajouter une colonne 'Total' qui est la somme des colonnes 5 et 6 -> axis=1 pour sommer les lignes
data['Total'] = data.iloc [:,5:7].sum(axis=1)
print (f"\ndata after adding a new column Total= \n{data.head(5)}")


#Meilleure pratiques pour ajouter une colonne en fonction d'autres colonnes
data['best_Total'] = data.loc [:,['NO2','NO']].sum(axis=1)
print (f"\ndata after adding a new column best_Total= \n{data.head(5)}")

#Réordonner les variables (colonnes) dans un dataframe
columns = list(data.columns.values)
print (f"\ncolumns before reordering = \n{columns}")
dataOrganized = data[columns[0:7]+[columns[-1]] + columns[7:10]]
print (f"\ndata reorganized = \n{dataOrganized.head(5)}")

#Supprimer une variable (colonne) d'un dataframe
dataDropped = data.drop(columns=['Pow2_O3obs'])
print (f"\ndata after dropping Pow2_O3obs column = \n{dataDropped.head(5)}")