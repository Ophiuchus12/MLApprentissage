#Chargement d'un DataSer csv vs txt
import pandas as pd

#Lire un cvs

data = pd.read_csv('Data/ozone.csv')
print(f"Data from CSV file:\n{data}")

#Lire un txt
data2 = pd.read_csv('Data/ozone.txt', delimiter='\t')
print(f"\nData from TXT file:\n{data2}")