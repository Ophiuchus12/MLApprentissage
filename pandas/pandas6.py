#Diminuer le nombre de variables (colonnes) dans un dataframe
import pandas as pd
import re

data = pd.read_csv('Data/ecoles-creches-idf.csv')
print ("Diminuer le nombre de variables (colonnes) dans un dataframe \n")
print (f"data head 5 = \n{data.head(5)}")
print (f"\n Columns before dropping = \n{data.columns.values}")

#Réduire les colonnes en utilisant melt
#On garde les colonnes ID et geometry, on réduit les colonnes PM10_2012 à PM10_2017 en deux colonnes : Année et Valeur
# PM10_Annee contiendra les années (2012 à 2017) et Valeur contiendra les valeurs correspondantes
dataReduced = data.melt(['ID','geometry'], ['PM10_2012','PM10_2013','PM10_2014','PM10_2015', 'PM10_2016','PM10_2017'], 'PM10_Annee', 'Valeur')
print (f"\ndata after reducing columns = \n{dataReduced.head(5)}")

#Appliquer une fonction à une colonne d'un dataframe (variable)
myData = data[['ID', 'geometry']]
print (f"\nmyData before applying function = \n{myData.head(5)}")

def get_latitude(s, flag):
    # separate la chaine de caractere s en utilisant les caracteres '(', ',' et ')' comme separateurs
    # si flag == 0, retourne la latitude (deuxieme valeur)
    # si flag == 1, retourne la longitude (troisieme valeur)
    res = re.split('\(|\,|\)', s)
    if flag == 0:
        res = res[1]
    else:
        res = res[2]
    return float(res)

# Appliquer la fonction get_latitude à la colonne 'geometry' pour obtenir la latitude
myData['Latitude'] = myData['geometry'].apply(get_latitude, args=(0,))
print (f"\nmyData after applying function to get Latitude = \n{myData.head(5)}")