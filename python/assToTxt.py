import os
import re
import unidecode

###############################
###############################

def lister_ass(dossierDepart):
    # Fonction pour obtenir la liste des fichiers sous un dossier donné
    ass_files = [] # Liste pour stocker les fichiers .ass
    for dirpath, dirnames, filenames in os.walk(dossierDepart, topdown=True):
        for filename in filenames:
            if filename.endswith(".ass"):
                path = os.path.join(dirpath, filename)
                if path not in ass_files:
                    ass_files.append(path)
                    # Ajouter le chemin du fichier .ass uniquement s'il n'est pas déjà dans la liste
    return ass_files

###############################
###############################