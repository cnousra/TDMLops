# Iris Flower Prediction App

Ce projet est une application web permettant de prédire l'espèce d'une fleur d'iris en fonction de ses caractéristiques (longueur et largeur des sépales et pétales). L'application utilise un modèle machine learning entraîné sur l'ensemble de données Iris.

## Structure du Projet

Le projet est structuré comme suit :

- `client/`: Contient le code de l'interface utilisateur (Streamlit) pour la consommation de l'API.
  - `app.py`: Fichier principal de l'application Streamlit pour la consommation de l'API REST.
  - `requirements.txt`: Liste des packages Python nécessaires pour l'application client.
  - `Dockerfile`: Instructions pour construire l'image Docker de l'application client.

- `server/`: Contient le code de l'API FastAPI pour le déploiement du modèle.
  - `app.py`: Fichier principal de l'API FastAPI pour le déploiement du modèle et la gestion des requêtes REST.
  - `requirements.txt`: Liste des packages Python nécessaires pour l'API FastAPI.
  - `Dockerfile`: Instructions pour construire l'image Docker de l'API FastAPI.
  - `model.pkl`: Fichier contenant le modèle machine learning entraîné avec les noms des classes.

- `td/`: Contient votre précédent exercice (non modifié dans cette mise à jour).

## Prérequis

Avant de pouvoir exécuter l'application, assurez-vous d'avoir installé Python et Docker sur votre système.

## Installation et Exécution

1. Clonez ce dépôt du projet sur votre machine avec : git clone <url_repository>
ou télécharger le dossier du projet dans le réporitory Github




2. Lancez Docker Compose pour construire et exécuter les conteneurs :

docker-compose up --build


Pour arrêter les conteneurs, utilisez la commande suivante :

docker-compose down

3. Accédez à l'application client dans votre navigateur en ouvrant l'URL suivante :


http://localhost:8501


4. Consultez la documentation de l'API FastAPI à l'adresse suivante :

http://localhost:8000/docs






