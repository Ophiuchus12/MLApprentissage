import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from math import sqrt
from sklearn.metrics import mean_squared_error, r2_score



#affichage des parametres (biais + poids) du modele
def display_model(x_train, regression_alg):
    if not hasattr(regression_alg, "coef_"):
        print("⚠️ Le modèle n'est pas entraîné")
        return

    print("Modèle linéaire appris :\n")
    for var, coef in zip(x_train.columns, regression_alg.coef_):
        print(f"{coef:.3f} * {var}")
    print(f"Intercept (biais) = {regression_alg.intercept_:.3f}")

    plt.barh(x_train.columns, regression_alg.coef_)
    plt.xlabel("Coefficient (standardisé)")
    plt.title("Influence des variables")
    plt.axvline(0)  # séparation positif / négatif
    plt.show()


def graph_test_prediction(y_test_known, test_prediction):
    plt.scatter(y_test_known, test_prediction, color='black')
    plt.title("les predictions du modele vs realite")
    plt.xlabel("les valeurs deja observées")
    plt.ylabel("les prédictions du modele")
    #la ligne rouge correspond au modele parfait -> chaque y predit vaut exactement le y attendu
    plt.plot([40.0, 160.0],[40.0, 160.0], 'red', lw=1)
    plt.show()

def create_evaluate_model(index_fold, x_train, x_test, y_train, y_test):
    regression_alg = LinearRegression()
    regression_alg.fit(x_train, y_train)
    test_prediction = regression_alg.predict(x_test)
    rmse = sqrt(mean_squared_error(y_test, test_prediction))
    r2 = r2_score(y_test, test_prediction)
    print(f"RUN {index_fold} : R2 = {round(r2,2)} - RMSE = {round(rmse,2)}")
    return (rmse, r2)