import os
import csv

def lister_noms_dossiers(dossier, fichier_csv):
    """Lister le nom des dossiers"""
    # Obtenir la liste des noms de dossiers
    noms_dossiers = [nom for nom in os.listdir(dossier) if os.path.isdir(os.path.join(dossier, nom))]
    
    # Écrire les noms de dossiers dans un fichier CSV
    with open(fichier_csv, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Nom du Dossier'])
        for nom_dossier in noms_dossiers:
           writer.writerow([nom_dossier])

def modifier_titres_majuscules(fichier_csv):
    """Mettre des majuscules dans au nom des films dans le csv"""
    # Ouvrir le fichier CSV en mode lecture
    with open(fichier_csv, mode='r', newline='', encoding='utf-8') as csvfile:
        # Lire le fichier CSV
        reader = csv.reader(csvfile)
        lignes = list(reader)

    # Modifier les titres en majuscules
    for i in range(1, len(lignes)):  # Commencer à partir de la deuxième ligne (index 1)
        titre = lignes[i][0]
        lignes[i][0] = titre.title()

    # Écrire les lignes modifiées dans un nouveau fichier CSV
    nouveau_fichier_csv = fichier_csv[:-4] + '_modifie.csv'
    with open(nouveau_fichier_csv, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for ligne in lignes:
            writer.writerow(ligne)