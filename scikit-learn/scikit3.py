###########################
#Regression polynomiale
###########################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import preprocessing
from math import sqrt
import matplotlib.pyplot as plt
from common import display_model, graph_test_prediction

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures

#Meme logique que pour la regression lineaire sauf que l'on utilise le module PolynomialFeatures 
#qui permet de generer des variables polynomiales a partir des variables initiales

data = pd.read_csv('Data/ozone.csv', sep=r'\s+')
y=data['maxO3']
data = data [['T9', 'T12','T15','Ne9', 'Ne12', 'Ne15', 'Vx9', 'Vx12', 'Vx15', 'maxO3v']]

#def standardisation valeur - moyenne / ecart-type
#('Normalisation' dans sklearn correspond en fait à une standardisation)
def standardisation(data_standar):
    columns = data_standar.columns
    for col in columns :
        x = data_standar[[col]].values.astype(float)
        standardiz = preprocessing.StandardScaler()
        res = standardiz.fit_transform(x)
        data_standar[col] = res

standardisation(data)

#separation des donnees en jeu de test et d'entrainement
x_train, x_test, y_train, y_test = train_test_split(data, y, test_size=0.2)

#creation d'un objet qui calculera les puissaces de 2 des variables
polynomial_features = PolynomialFeatures(degree=2)

#instanciation de l'algo de regression lineaire
poly_regression_alg = LinearRegression()

#creation d'un pipeline qui applique d'abord la transformation polynomiale puis l'algo de regression lineaire
model = Pipeline ([
    ("polynomial_features", polynomial_features),
    ("linear_regression", poly_regression_alg)
])

model.fit(x_train, y_train)

train_prediction = model.predict(x_train)

print("EVALUATION SUR LE JEU DE TEST")
print (f"RMSE sur le jeu d'entrainement : {round(sqrt(mean_squared_error(y_train, train_prediction)),2)}")
print (f"R2 sur le jeu d'entrainement : {round(r2_score(y_train, train_prediction),2)}")

#Avec les donnees d'entrainement
graph_test_prediction(y_train, train_prediction)

#Avec les donnees de test
test_prediction = model.predict(x_test)
print("EVALUATION SUR LE JEU DE TEST")
print (f"RMSE sur le jeu de test : {round(sqrt(mean_squared_error(y_test, test_prediction)),2)}")
print (f"R2 sur le jeu de test : {round(r2_score(y_test, test_prediction),2)}")
graph_test_prediction(y_test, test_prediction)

#exemple de retour (cata)
# EVALUATION SUR LE JEU DE TEST
# RMSE sur le jeu d'entrainement : 5.13
# R2 sur le jeu d'entrainement : 0.97
# EVALUATION SUR LE JEU DE TEST
# RMSE sur le jeu de test : 32.72
# R2 sur le jeu de test : -0.75