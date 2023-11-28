import csv
import os
import json
from fuzzywuzzy import fuzz # Permet de trouver des correspondance
import pymongo # Permet de d'interagire avec une base de données Mongo
import pandas as pd
from tqdm import tqdm # Affiche une barre de progression dans le terminal lors de l'execution du script 

# Permet de trouver les correspondances entre le nom des répertoires de séries 
# avec une liste de nom de séries écrit en "propre"
def trouver_correspondance(terme_a_comparer, liste_de_series):
    correspondance_trouvee = None
    meilleur_score = 0

    for nom_serie in liste_de_series:
        score = fuzz.ratio(terme_a_comparer.lower(), nom_serie.lower())
        if score > meilleur_score:
            meilleur_score = score
            correspondance_trouvee = nom_serie

    return correspondance_trouvee

repertoire_series = "script/listes_mots_series"
dictionnaire_mots_cles = {}
chemin_fichier_csv = "script/liste_dossiers.csv"
colonne_propre = []

with open(chemin_fichier_csv, "r") as fichier_csv:
    lecteur_csv = csv.reader(fichier_csv)
    for ligne in lecteur_csv:
        if len(ligne) >= 2:
            colonne_propre.append(ligne[1])

for nom_fichier in os.listdir(repertoire_series):
    if nom_fichier.endswith(".csv"):
        chemin_fichier = os.path.join(repertoire_series, nom_fichier)
        with open(chemin_fichier, "r", newline='', encoding="ansi") as fichier_csv:
            lecteur_csv = csv.reader(fichier_csv)
            next(lecteur_csv, None) 

            nom_serie_propre = trouver_correspondance(nom_fichier[:-4], colonne_propre) or "Nom_inconnu"

            for ligne in lecteur_csv:
                if len(ligne) >= 2:
                    mot = ligne[0]
                    poids = float(ligne[1])

                    if mot in dictionnaire_mots_cles:
                        dictionnaire_mots_cles[mot]["liste_series"].append({"serie": nom_serie_propre, "poids": poids})
                    else:
                        dictionnaire_mots_cles[mot] = {"liste_series": [{"serie": nom_serie_propre, "poids": poids}]}


chemin_fichier_json = "mots_cles.json"
with open(chemin_fichier_json, "w", encoding="utf-8") as fichier_json:
    json.dump(dictionnaire_mots_cles, fichier_json, indent=4)

def importerDonneMongo():
    client = pymongo.MongoClient("mongodb://localhost:27017/") 
    database = client["SAE_C01"]
    collection = database["séries"]
    
    chemin_fichier_json = "mots_cles.json"
    
    # Charger le fichier JSON
    with open(chemin_fichier_json, "r", encoding="utf-8") as fichier_json:
        donnees_json = json.load(fichier_json)
    
    barre_progression = tqdm(donnees_json.items(), desc="Importation des données", unit="mot")
    
    # Insérer les données dans la collection MongoDB
    for mot, details in barre_progression:
        jsonFormat = {"Mot": str(mot), "liste_series": details["liste_series"]}
        collection.insert_one(jsonFormat)
    
    client.close()

importerDonneMongo()

print(f"Le dictionnaire des mots-clés a été importé dans la collection MongoDB.")
