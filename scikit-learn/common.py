import matplotlib.pyplot as plt

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
