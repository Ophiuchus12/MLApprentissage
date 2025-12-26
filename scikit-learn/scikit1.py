#Creation d'un modele linéaire multiple pour prédire la pollution dans une ville
#Variable vent et pluie -> qualitative (pour devenir quantitative les transformer en valeurs numeriques)
#Dans notre exemple la variable à expliquer est Maxo3

#Prédire quelle valeur prendra Maxo3 demain

# Manipulation et analyse de données sous forme de tableaux (DataFrame)
import pandas as pd
# Fournit des fonctions mathématiques de base, ici la racine carrée
from math import sqrt
# Création de graphiques et visualisation des données
import matplotlib.pyplot as plt
# Séparation d’un jeu de données en ensembles d’entraînement et de test
from sklearn.model_selection import train_test_split
# Implémentation de la régression linéaire
from sklearn.linear_model import LinearRegression
# Fonctions d’évaluation : erreur quadratique moyenne et coefficient de détermination
from sklearn.metrics import mean_squared_error, r2_score
# Outils de prétraitement des données (normalisation, standardisation, etc.)
from sklearn import preprocessing

#Recuperation des data

data = pd.read_csv('Data/ozone.csv', sep=r'\s+')


print (f"DATA \n{data}")

columns = data.columns.values
print(f"columns {columns}")
#isolation de la variable dans un vecteur à expliquer 
y=data['maxO3']
print (f"data isolée {y}")


data = data [['T9', 'T12','T15','Ne9', 'Ne12', 'Ne15', 'Vx9', 'Vx12', 'Vx15', 'maxO3v']]
print (f"data {data}")
stat = data.describe()
print (f"stats des donnees data \n{stat}")


#def standardisation valeur - moyenne / ecart-type
def standardisation(data_standar):
    columns = data_standar.columns
    for col in columns :
        x = data_standar[[col]].values.astype(float)
        standardiz = preprocessing.StandardScaler()
        res = standardiz.fit_transform(x)
        data_standar[col] = res
    return data_standar


dataStandadization = standardisation(data)
print (f"data standardisées \n{dataStandadization}")
print (f"\n describe new data standardisées \n {dataStandadization.describe()}")

#Construction d'un modele lineaire 

#pour appliquer l'algo linieaire -> creation d'un JDD de test 
x_train, x_test, y_train, y_test = train_test_split(data, y, test_size=0.2)

#Instantiation algo lineaire
regression_alg = LinearRegression()
#resultat de l'instruction ci-dessous -> modele qui peut etre utiliser pour predire la concetration d'air en ozone en partant des 10 variables explicatives
regression_alg.fit(x_train, y_train)

#calculs de métrique de performances 
train_prediction = regression_alg.predict(x_train)

# Calcul et affichage de la racine de l'erreur quadratique moyenne (RMSE) arrondie à 2 décimales
# Le RMSE mesure l'écart moyen entre les prédictions et les valeurs réelles d'entraînement
print (f"RMSE = {round(sqrt(mean_squared_error(y_train, train_prediction)),2)}")

# Calcul et affichage du coefficient de détermination (R²) arrondi à 2 décimales
# Le R² mesure la proportion de variance expliquée par le modèle (entre 0 et 1, plus proche de 1 est mieux)
print(f"R2_score = {round(r2_score(y_train, train_prediction),2)}")