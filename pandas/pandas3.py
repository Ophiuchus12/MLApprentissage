#Acces aux données d'un dataframe pandas
import pandas as pd

data = pd.read_csv('Data/ozone.csv')
#lire une ligne spécifique
myDataSet = data.iloc[5]

print("Acces aux données d'un dataframe pandas \n")
print(f"myDataSet = \n{myDataSet}")

#lire un ensemble de lignes
myDataSet2 = data.iloc[2:5]
print(f"\nmyDataSet2 = \n{myDataSet2}")


#Parcourir les lignes d'un dataframe
print("\nParcourir les lignes d'un dataframe \n")
for index, row in data.iterrows():
    print("La valeur d'indice [{}] : \n {}".format(index, row))