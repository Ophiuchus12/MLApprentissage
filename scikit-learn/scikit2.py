# Manipulation et analyse de données sous forme de tableaux (DataFrame)
import pandas as pd
# Fournit des fonctions mathématiques de base, ici la racine carrée
from math import sqrt
# Création de graphiques et visualisation des données
import matplotlib.pyplot as plt
# Séparation d’un jeu de données en ensembles d’entraînement et de test
from sklearn.model_selection import train_test_split, KFold
# Implémentation de la régression linéaire
from sklearn.linear_model import LinearRegression
# Fonctions d’évaluation : erreur quadratique moyenne et coefficient de détermination
from sklearn.metrics import mean_squared_error, r2_score
# Outils de prétraitement des données (normalisation, standardisation, etc.)
from sklearn import preprocessing

from common import display_model, graph_test_prediction, create_evaluate_model

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


standardisation(data)
print (f"data standardisées \n{standardisation(data).head(5)}")
print (f"\n describe new data standardisées \n {standardisation(data).describe()}")
print (f"\n data post ope {data.head(5)}")



#COMPARAISON DE train_test_split et de KFOLD
#train_test_split -> retourne directement les jeux de données (les données elles-mêmes, pas les indices)
#KFold -> retourne les indices des jeux de données (il faut ensuite aller chercher les données dans le DataFrame à partir de ces indices)



kf = KFold(n_splits=2, shuffle=False)
#print de 2 dataset à partir de data
for train_index, test_index in kf.split(data):
    print ("Les indices de train_index =", train_index)
    print ("Les indices de test_index =", test_index)
    print("\n\n")

#impact du shuffle
kfShuffle = KFold(n_splits=2, shuffle=True)
#print de 2 dataset à partir de data avec impact du shuffle 
for train_index, test_index in kfShuffle.split(data):
    print ("Les indices de train_index shuffle =", train_index)
    print ("Les indices de test_index shuffle =", test_index)
    print("\n\n")


#Le nombre d'élements dans des listes est fixé par le nb de dataset à construire
#Essayons avec 3

kf3 = KFold(n_splits=3, shuffle= False)
for train_index, test_index in kf3.split(data):
    print (f"\nle nb d'éléments dans train_index : {train_index.shape[0]}")
    print (f"\nle nb d'éléments dans test_index : {test_index.shape[0]}")

# Corrélation n_splits ↔ taille du train/test
# Si :
# N = nombre total d’observations
# n_splits = k
# Alors, approximativement :
# taille du test= N/k
# taille du train=N−taille du test≈N⋅k−1/k



##############################
#EVALUATION DU MODELE AVEC KFOLD
##############################

nb_model = 5 
#5 plis (folds) ->1 pli sert de jeu de test,4 plis servent de jeu d’entraînement

kf=KFold(n_splits=nb_model, shuffle=False)

index_fold = 0 
average_rmse = 0
average_r2 = 0

for train_index, test_index in kf.split(data):
    x_train, x_test = data.iloc[train_index], data.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

    current_rmse, current_r2 = create_evaluate_model(index_fold, x_train, x_test, y_train, y_test)
    average_rmse = average_rmse + current_rmse
    average_r2 = average_r2 + current_r2
    index_fold = index_fold + 1

average_rmse = average_rmse / nb_model
average_r2 = average_r2 / nb_model
print (f"\nAverage RMSE over {nb_model} folds : {round(average_rmse,2)}")
print (f"\nAverage R2 over {nb_model} folds : {round(average_r2,2)}")