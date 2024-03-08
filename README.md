# 🏡 [ParisAirbnb](https://tryparisairbnb-f7bcf2a9b109.herokuapp.com/)

## Prédiction des Prix de Location Airbnb à Paris


## 📋 Table des matières

- [Description du Projet](#-description-du-projet)
- [Sources des Données et modélisation](#-sources-des-données-et-modélisation)
- [Utilisation du Projet](#-utilisation-du-projet)


## 🎯 Description du Projet

ParisAirbnb est une application web de prédiction des prix de nuitée des logements en location sur les sites spécialisés (nous avons pris comme référence Airbnb). Nous avons développé ParisAirbnb dans un contexte où de nombreux propriétaires de logements à Paris envisagent de louer leurs biens durant la période des Jeux olympiques Paris 2024. Plus largement, cette application cible les propriétaires immobiliers ou toute personne envisageant d'acquérir un bien immobilier dans les 20 arrondissements de Paris pour le mettre en location de courte durée.

Ce travail s'inscrit dans un travail d'équipe plus large à retrouver dans ce dépôt [ici](https://github.com/Val832/produit_digital).

### Objectifs
- Développer un outil 🛠️ avancé pour la prédiction des prix de location des logements Airbnb à Paris. 
- Fournir des estimations 💸 précises des prix à la nuitée, basées sur les caractéristiques détaillées de chaque logement.

### Problématique
- Comble la lacune de l'outil d'estimation de prix proposé par Airbnb, en offrant des prévisions plus précises et détaillées 🎯.

### Solution apportée
- **Estimations Personnalisées** 📋: Utilisation d'un formulaire pour permettre aux utilisateurs de recevoir des estimations basées sur des critères spécifiques.
- **Interface Utilisateur en VBA** 🖥️: Création d'une interface conviviale pour la saisie des données et l'affichage des résultats.


## 📚 Sources des Données et modélisation

### Source des Données : Inside Airbnb
- **Provenance** 🌐: Les données proviennent d'Inside Airbnb, une initiative indépendante offrant des analyses détaillées des listings Airbnb.
- **Contenu** 📄: Informations détaillées sur les listings parisiens, y compris emplacement, fréquence de location et revenus des hôtes.
- **Fiabilité** ✔️: Données régulièrement mises à jour pour garantir leur exactitude et pertinence.

Pour plus de détails sur les données et les différents traitements voi [ici](https://github.com/Val832/produit_digital/tree/main/src/df_manipulation/2023)

Pour accéder à la base de données, visitez [Inside Airbnb](http://insideairbnb.com/get-the-data.html).

### Modèle
Pour estimer le prix de la nuitée, nous avons développé plusieurs modèles de machine learning en utilisant des algorithmes de régression tels que la régression linéaire, les arbres de décision, les forêts aléatoires et le boosting. Bien que le modèle de régression linéaire se soit révélé légèrement moins performant que les autres, nous avons décidé de le conserver. En effet, son manque de précision est largement compensé par la capacité qu'il offre à estimer un intervalle d'erreur fiable.

Pour plus de détails sur les modèles voir [ici](https://github.com/Val832/produit_digital/tree/main/src/data_science/models)



## 🚀 Utilisation du Projet

Pour estimer le prix de votre logement utilisez ce lien 👉🏿 [ici](https://tryparisairbnb-f7bcf2a9b109.herokuapp.com/)

Pour les plus curieux qui souhaitent faire tourner l'application en local, nous conseillons l'utilisation de conteneurs Docker.

**Construire une image Doker**

```bach
docker build -t parisaribnb_img . 
``` 

**Construire et lancer un conteneur Doker**

Avant de lancer le conteneur, veuillez préciser le port dans le Dockerfile avec la ligne `EXPOSE 5000`.
Vous pouvez choisir un port différent de 5000, mais nous le garderons dans la suite des étapes.

```bach
docker run -p 5000:5000 --name parisaribnb  parisaribnb_img
``` 


`5000:5000` correspond à `<port_hôte>:<port_conteneur>`.

### A venir
- Ajout de Shapley values pour mettre en avant les points forts des logements
- Migration vers une interface Streamlit
