import os
import re
import unidecode

###############################
###############################

def lister_sub(dossierDepart):
    # Fonction pour obtenir la liste des fichiers sous un dossier donné
    sub_files = [] # Liste pour stocker les fichiers .sub
    for dirpath, dirnames, filenames in os.walk(dossierDepart, topdown=True):
        for filename in filenames:
            if filename.endswith(".sub"):
                path = os.path.join(dirpath, filename)
                if path not in sub_files:
                    sub_files.append(path)
                    # Ajouter le chemin du fichier .sub uniquement s'il n'est pas déjà dans la liste
    return sub_files

###############################
###############################