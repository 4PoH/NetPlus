##########################
######## IMPORTS #########
##########################

import srtToTxt as srtToTxt
import subToTxt as subToTxt
import assToTxt as assToTxt
import lematisation as lema
import unzipClean
import shutil
import os
import time
import decoupe_TFIDF
import nom
import updateDatabase
import fuzzywuzzy
from tqdm import tqdm

##########################
##########################

##########################
####### VARIABLES ########
##########################

# Remplacez par le chemin de votre dossier où tout ce fera
DOSSIER_DATA = "NetPlus\data"

# Le nom ou le chemin du dossier ou se trouvent les fichiers de sous titres zippé (en partant de DOSSIER_DATA)
REPERTOIRE_SOUS_TITRE = "sous-titres"
DOSSIER_SOUS_TITRE = os.path.join(DOSSIER_DATA, REPERTOIRE_SOUS_TITRE)

REPERTOIRE_TRAITEMENT = "series"
REPERTOIRE_CSV = "csv"


# DESTINATION = os.path.join(DOSSIER, NOM_DOSSIER_TRAITEMENT)

# NOM_DOSSIER_SERIE_CSV = "1liste_series"   # Nom du fichier CSV de sortie
# DOSSIER_CSV = os.path.join(DOSSIER, NOM_DOSSIER_SERIE_CSV)

# NOM_CSV_TITRE = "1TitreSeries.csv" #Nom du csv qui contiendra le nom des séries
# DOSSIER_TITRE = os.path.join(DOSSIER_CSV, NOM_CSV_TITRE)

ENCODING = "ansi"

##########################
##########################

##########################
####### EXECUTION ########
##########################

t0 = time.time()

##########################
##########################

##########################
####### DEZIPPAGE ########
##########################
# Dézipper les fichiers à partir du répertoire donné
print("Début du dézippage")

# Récupérer les chemins des fichiers ZIP dans toute l'arborescence
zip_files = []
for root, dirs, files in os.walk(DOSSIER_SOUS_TITRE):
    for file in files:
        if file.endswith('.zip'):
            zip_files.append(os.path.join(root, file))

print(zip_files)

for zip_file in tqdm(zip_files, desc="Dézippage"):
    unzipClean.unzip_clean(DOSSIER_SOUS_TITRE)

t1 = time.time()
print("Temps unzip :" + str(t1 - t0))
##########################
##########################