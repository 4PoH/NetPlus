import srtToTxt as srtToTxt
import subToTxt as subToTxt
import assToTxt as assToTxt
import lematisation as lema
import unzipClean as unzipClean
import shutil
import os
import time
import decoupe_TFIDF
import nom
import updateDatabase
import fuzzywuzzy
from tqdm import tqdm

def isATraiter(file):
    # Liste des extensions à vérifier
    extensions_traitees = ['.srt', '.SRT', '.sub', '.SUB', '.ass', '.ASS']  # Ajoutez les extensions nécessaires

    # Obtenez l'extension du fichier
    file_extension = os.path.splitext(file)[1]

    # Vérifiez si l'extension du fichier est dans la liste des extensions à traiter
    if file_extension in extensions_traitees:
        return True
    return False

#######################
###### VARIABLES ######
#######################

DOSSIER = "NetPlus/data/sous-titres" # Remplacez par le chemin de votre dossier
NOM_DOSSIER_TRAITEMENT = "1series"
DESTINATION = os.path.join(DOSSIER, NOM_DOSSIER_TRAITEMENT)

NOM_DOSSIER_SERIE_CSV = "1liste_series"   # Nom du dossier pour les CSV
DOSSIER_CSV = os.path.join(DOSSIER, NOM_DOSSIER_SERIE_CSV)

NOM_CSV_TITRE = "1TitreSeries.csv" #Nom du csv qui contiendra le nom des séries
DOSSIER_TITRE = os.path.join(NOM_DOSSIER_SERIE_CSV, NOM_CSV_TITRE)

ENCODING = "ansi"

#######################
###### EXECUTION ######
#######################
t0 = time.time()

##########################
####### DEZIPPAGE ########
##########################
unzipClean.unzip_clean(DOSSIER)

t1 = time.time()
print("Temps unzip :" + str(t1 - t0))
##########################
###### TRAITEMENT ######
##########################
print("Début du traitement")

noms_serie = []
file_a_traiter = []

for path, dirs, files in os.walk(DOSSIER):
    if (DESTINATION) in dirs:
        shutil.rmtree(DESTINATION)

for path, dirs, files in os.walk(DOSSIER):
    depth = len(path.split(os.sep)) - len(DOSSIER.split(os.sep))
    if depth == 1:
        noms_serie.append(os.path.basename(path))  # Stocke le nom du dossier de profondeur 1

    for filename in files:
        if isATraiter(filename):
            file_a_traiter.append(filename)

        if filename.endswith(".srt") or filename.endswith(".SRT"):
            txtFile = os.path.join(DESTINATION,noms_serie[-1]) + ".txt"
            srtToTxt.filtrage(os.path.normpath(os.path.join(path,filename)), txtFile, ENCODING)

        if filename.endswith(".sub") or filename.endswith(".SUB"):
            txtFile = os.path.join(DESTINATION,noms_serie[-1]) + ".txt"
            subToTxt.filtrage(os.path.normpath(os.path.join(path,filename)), txtFile, ENCODING)

        if filename.endswith(".ass") or filename.endswith(".ASS"):
            txtFile = os.path.join(DESTINATION,noms_serie[-1]) + ".txt"
            assToTxt.filtrage(os.path.normpath(os.path.join(path,filename)), txtFile, ENCODING)

t2 = time.time()
print("Temps traitement :" + str(t2-t1))
##########################
###### LEMATISATION ######
##########################
print("Début de la lemmatisation")

files_lema = []
for root, dirs, files in os.walk(DESTINATION):
    for file in files:
        files_lema.append(os.path.join(root, file))

for file in tqdm(files_lema, desc="Lemmatisation"):
    lema.lematiser_file(file)

t3 = time.time()
print("Temps lemmatisation :" + str(t3-t2))
##########################
###### TF IDF ######
##########################
decoupe_TFIDF.creer_csv_series(DESTINATION, DOSSIER_CSV)

t4 = time.time()
print("Temps TF-IDF :" + str(t4-t3))
##########################

##########################
###### Nom séries ######
##########################

nom.lister_noms_dossiers(DOSSIER, DOSSIER_TITRE)
#nom.modifier_titres_majuscules(DOSSIER_TITRE)

t5 = time.time()
print("Temps nom séries :" + str(t5-t4))
##########################

##########################
####### Insert BDD #######
##########################

dictionnaire_mots_cles = updateDatabase.creer_dictionnaire_mots_cles(DOSSIER, os.path.join(DOSSIER, DOSSIER_TITRE))
chemin_fichier_json = "mots_cles.json"

with open(chemin_fichier_json, "w", encoding="utf-8") as fichier_json:
    json.dump(dictionnaire_mots_cles, fichier_json, indent=4)

updateDatabase.importer_donnees_mongo(dictionnaire_mots_cles)

print(f"Le dictionnaire des mots-clés a été importé dans la collection MongoDB.")

t6 = time.time()
##########################

print("Temps unzip :" + str(t1-t0))
print("Temps traitement :" + str(t2-t1))
print("Temps lemmatisation :" + str(t3-t2))
print("Temps TF-IDF :" + str(t4-t3))
print("Temps nom séries :" + str(t5-t4))
print("Temps Insertion bdd :" + str(t6-t5))
print("Temps total :" + str(t6-t0))