import srtToTxt as srtToTxt
import subToTxt as subToTxt
import assToTxt as assToTxt
import lematisation as lema
import unzipClean as unzipClean
import shutil
import os
import time
import decoupe_TFIDF

#######################
###### VARIABLES ######
#######################

#DOSSIER = "NetPlus\data\sous-titres-Copie"  # Remplacez par le chemin de votre dossier
DOSSIER = "NetPlus\data\sous"
REPERTOIRE_DESTINATION_TRAITEMENT = "series"
DESTINATION = os.path.join(DOSSIER, REPERTOIRE_DESTINATION_TRAITEMENT)
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

t0 = time.time()

##########################
###### DEZIPPAGE ######
##########################


# Dézipper les fichiers à partir du répertoire donné
unzipClean.unzip_clean(DOSSIER)
t1 = time.time()

##########################
###### TRAITEMENT ######
##########################

noms_serie = []

for path, dirs, files in os.walk(DOSSIER):
    if (REPERTOIRE_DESTINATION_TRAITEMENT) in dirs:
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

t2 = time.time()

##########################
###### LEMATISATION ######
##########################

for path, dirs, files in os.walk(DESTINATION):
    for filename in files:
        lema.lematiser(os.path.join(DESTINATION,filename))

t3 = time.time()

##########################
###### TF IDF ######
##########################


t4 = time.time()
##########################


print("Temps unzip :" + str(t1-t0))
print("Temps traitement :" + str(t2-t1))
print("Temps lemmatisation :" + str(t3-t2))
print("Temps TF-IDF :" + str(t4-t3))