import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Charger l'ensemble de données Iris
iris = load_iris()
X, y = iris.data, iris.target

# Entraîner le modèle
model = RandomForestClassifier()
model.fit(X, y)

# Créer un dictionnaire contenant le modèle et les noms des classes
modelpkl = {
    'model': model,
    'class_names': iris.target_names.tolist()  # Convertir les noms des classes en liste
}

# Sauvegarder le dictionnaire dans un fichier pickle
joblib.dump(modelpkl, '../server/model.pkl')
