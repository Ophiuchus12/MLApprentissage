#Sauvegarder un dataframe dans un fichier CSV
import pandas as pd

dataSet = pd.read_csv('Data/ozone.csv')
dataSet['O3obs_pow2'] = pow(dataSet['O3obs'],2)
print ("Sauvegarder un dataframe dans un fichier CSV \n")
print (f"dataSet head 5 = \n{dataSet.head(5)}")

columns = list(dataSet.columns.values)
dataSetOganized = dataSet[columns[0:2] + [columns[-1]] + columns[2:10]]
print (f"\ndataSet organized = \n{dataSetOganized.head(5)}")
dataSetOganized.to_csv('Data/ozone_modified.csv')
#OOn peut ajouter des paramètres à to_csv comme index=False pour ne pas sauvegarder l'index
print ("\nDataframe saved to 'Data/ozone_modified.csv'")