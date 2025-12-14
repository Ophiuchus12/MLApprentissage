#Faire des stats avec un dataframe
import pandas as pd

#Resume global des statistiques descriptives du dataframe
data = pd.read_csv('Data/ozone.csv')
stat = data.describe()
print ("Faire des stats avec un dataframe \n")
print (f"data head 5 = \n{data.head(5)}")
print (f"\nStatistiques descriptives du dataframe = \n{stat}")

#Resume par agrégation
mean =data.groupby('STATION').mean()
print (f"\nMoyenne des valeurs par STATION = \n{mean}")

#Combiner
combined = data.groupby('STATION').mean().sort_values('O3obs', ascending=False)
print (f"\nMoyenne des valeurs par STATION triée par O3obs décroissante = \n{combined}")

#Agregation multiple
byDayOff = data.groupby(['STATION', 'JOUR']).mean()
print (f"\nMoyenne des valeurs par STATION et JOUR = \n{byDayOff}")