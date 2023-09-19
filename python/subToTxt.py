from pysubparser import parser
import os
import re
import unidecode

#subtitles = parser.parse('NetPlus\\data\\testZippage\\sous-titres-adezipper-Copie\\buffy\\Buffy-2x01WhenSheWasBad.EN.sub', encoding='ansi')
subtitles = parser.parse('NetPlus\\data\\testZippage\\sous-titres-adezipper-Copie\\desperatehousewives\Desperate.Housewives.612.2hd.EN.TAG.ass', encoding='ansi')

for subtitle in subtitles:
    print(subtitle)

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