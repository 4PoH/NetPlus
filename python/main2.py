import srtToTxt as srtToTxt
import subToTxt as subToTxt
import assToTxt as assToTxt
import lematisation as lema
import unzipClean as unzipClean
import shutil
import os

#######################
###### VARIABLES ######
#######################

DOSSIER = "data/sous-titres-Copie"  # Remplacez par le chemin de votre dossier
REPERTOIRE_DESTINATION = "1txt"
DESTINATION = os.path.join(DOSSIER, REPERTOIRE_DESTINATION)
FICHIER_CSV = "liste_dossiers.csv"   # Nom du fichier CSV de sortie
ENCODING = "ansi"

#######################
###### FONCTION  ######
#######################

# def compteur(dossierDepart):
#     i = 0
#     for element in os.walk(dossierDepart):
#         for name in element[2]:
#             if name.endswith('.srt') or name.endswith('.SRT') or name.endswith('.vo') or name.endswith('.VO'):
#                 i = i + 1
#             elif name.endswith('.sub') or name.endswith('.SUB'):
#                 i = i + 1
#             elif name.endswith('.ass') or name.endswith('.ASS'):
#                 i = i + 1
#     return i

# print(compteur(DOSSIER))

#######################
###### EXECUTION ######
#######################

# Dézipper les fichiers à partir du répertoire donné
unzipClean.unzip_clean(DOSSIER)

noms_serie = []
print(noms_serie)
for path, dirs, files in os.walk(DOSSIER):
    if (REPERTOIRE_DESTINATION) in dirs:
        shutil.rmtree()

for path, dirs, files in os.walk(DOSSIER):

    depth = len(path.split(os.sep)) - len(DOSSIER.split(os.sep))
    if depth == 1:
        noms_serie.append(os.path.basename(path))  # Stocke le nom du dossier de profondeur 1

    for filename in files:
        if filename.endswith(".srt") or filename.endswith(".SRT"):
            txtFile = os.path.join(DESTINATION,noms_serie[-1]) + ".txt"
            #print(os.path.normpath(os.path.join(path,filename)), os.path.normpath(os.path.join(DESTINATION,noms_serie[-1])))
            srtToTxt.filtrage(os.path.normpath(os.path.join(path,filename)), txtFile, ENCODING)
            #print('srt')

        if filename.endswith(".sub") or filename.endswith(".SUB"):
            txtFile = os.path.join(DESTINATION,noms_serie[-1]) + ".txt"
            #print(os.path.normpath(os.path.join(path,filename)), os.path.normpath(os.path.join(DESTINATION,noms_serie[-1])))
            subToTxt.filtrage(os.path.normpath(os.path.join(path,filename)), txtFile, ENCODING)
            print('sub')

        if filename.endswith(".ass") or filename.endswith(".ASS"):
            txtFile = os.path.join(DESTINATION,noms_serie[-1]) + ".txt"
            #print(os.path.normpath(os.path.join(path,filename)), os.path.normpath(os.path.join(DESTINATION,noms_serie[-1])))
            assToTxt.filtrage(os.path.normpath(os.path.join(path,filename)), txtFile, ENCODING)
            print("ass")


##########################
###### LEMATISATION ###### 
##########################

for path, dirs, files in os.walk(DESTINATION):
    for filename in files:
        lema.lematiser(os.path.join(DESTINATION,filename))