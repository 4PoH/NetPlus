#Créer les fichiers csv des séries selon leur fichier texte (txt)
import os
import re
import csv
from sklearn.feature_extraction.text import TfidfVectorizer

def decoupe(texte):
    texte_decoupe = list(re.split('; |, |\' |\n |\s+', texte))
    return " ".join(texte_decoupe) 

def lire_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r', encoding='ansi') as fichier:
            contenu = fichier.read()
        return contenu
    except FileNotFoundError:
        print("Erreur")
        return ""


dossier_series = "series"
dossier_sortie = "listes_mots_series"

if not os.path.exists(dossier_sortie):
    os.makedirs(dossier_sortie)

for nom_fichier in os.listdir(dossier_series):
    chemin_fichier = os.path.join(dossier_series, nom_fichier)
    contenu = lire_fichier(chemin_fichier)
    
    if contenu:
        resultat = decoupe(contenu) 
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([resultat])
        feature_names = vectorizer.get_feature_names_out()
        tfidf_scores = tfidf_matrix.toarray()[0]
        mots_cles_pondere = list(zip(feature_names, tfidf_scores))
        mots_cles_pondere = sorted(mots_cles_pondere, key=lambda x: x[1], reverse=True)
        
        nom_sortie = os.path.splitext(nom_fichier)[0] + ".csv"
        chemin_sortie = os.path.join(dossier_sortie, nom_sortie)
        
        limite_mots = 50000

        with open(chemin_sortie, "w", newline='') as fichier_csv:
            writer = csv.writer(fichier_csv)
            writer.writerow(["Mot", "Poids"])  
            
            mots_inclus = 0 
            
            for mot, poids in mots_cles_pondere:
                if mots_inclus < limite_mots:
                        writer.writerow([mot, poids])
                        mots_inclus += 1
                else:
                    break  
