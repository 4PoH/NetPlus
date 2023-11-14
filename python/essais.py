import srtToTxt as srtToTxt
import subToTxt as subToTxt
import assToTxt as assToTxt
import lematisation as lema
import unzipClean as unzipClean
import os

#######################
###### VARIABLES ######
#######################

DOSSIER = "data\sous-titres-Copie"  # Remplacez par le chemin de votre dossier
DESTINATION = os.path.join(DOSSIER, "1txt")
FICHIER_CSV = "liste_dossiers.csv"   # Nom du fichier CSV de sortie
ENCODING = "ansi"


noms_serie = []
print(noms_serie)
for path, dirs, files in os.walk(DOSSIER):
    print(files)
    # depth = len(path.split(os.sep)) - len(DOSSIER.split(os.sep))
    # if depth == 1:
    #     noms_serie.append(os.path.basename(path))  # Stocke le nom du dossier de profondeur 1

    # for filename in files:
    #     if filename.endswith(".srt") or filename.endswith(".SRT"):
    #         txtFile = os.path.join(DESTINATION,noms_serie[-1]) + ".txt"
    #         #print(os.path.normpath(os.path.join(path,filename)), os.path.normpath(os.path.join(DESTINATION,noms_serie[-1])))
    #         srtToTxt.filtrage(os.path.normpath(os.path.join(path,filename)), txtFile, ENCODING)
    #         print('srt')

    #     if filename.endswith(".sub") or filename.endswith(".SUB"):
    #         txtFile = os.path.join(DESTINATION,noms_serie[-1]) + ".txt"
    #         #print(os.path.normpath(os.path.join(path,filename)), os.path.normpath(os.path.join(DESTINATION,noms_serie[-1])))
    #         subToTxt.filtrage(os.path.normpath(os.path.join(path,filename)), txtFile, ENCODING)
    #         print('sub')

    #     if filename.endswith(".ass") or filename.endswith(".ASS"):
    #         print("ass")
    #         pass