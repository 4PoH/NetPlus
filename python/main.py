import nom as nom
import srtToTxt as srtToTxt
import subToTxt as subToTxt
import assToTxt as assToTxt
import lematisation as lema
import unzipClean as unzipClean
import os

#######################
###### VARIABLES ######
#######################

DOSSIER = "NetPlus\data\sous-titres-Copie1"  # Remplacez par le chemin de votre dossier
DOSSIER_DESTINATION = "NetPlus/data/sous-titres-Copie1/1txt"
FICHIER_CSV = "liste_dossiers.csv"   # Nom du fichier CSV de sortie
ENCODING = "ansi"

#######################
###### FONCTION  ######
#######################

def compteur(dossierDepart):
    i = 0
    for element in os.walk(dossierDepart):
        for name in element[2]:
            if name.endswith('.srt') or name.endswith('.SRT') or name.endswith('.vo') or name.endswith('.VO'):
                i = i + 1
            elif name.endswith('.sub') or name.endswith('.SUB'):
                i = i + 1
            elif name.endswith('.ass') or name.endswith('.ASS'):
                i = i + 1
    return i

# print(compteur(DOSSIER))

#######################
###### EXECUTION ######
#######################

# Dézipper les fichiers à partir du répertoire donné
unzipClean.unzip_clean(DOSSIER)

# Récupérer le nom des series et les mettres dans le csv
# nom.lister_noms_dossiers(DOSSIER, FICHIER_CSV)
# nom.modifier_titres_majuscules(FICHIER_CSV)
2
# Récupérer la liste des .srt à transformer en texte
liste_fichiers_srt = srtToTxt.lister_srt(DOSSIER)
#print(liste_fichiers_srt)

compteur = 0
total = len(liste_fichiers_srt)
for element in liste_fichiers_srt:
    srtToTxt.filtrage(element,DOSSIER_DESTINATION,ENCODING)
    compteur += 1
    print(f"{compteur} / {total} fichier .srt traités")
print(f"{compteur} / {total} fichier .srt traités")

# Récupérer la liste des .sub à transformer en texte
liste_fichiers_sub = subToTxt.lister_sub(DOSSIER)
# print(liste_fichiers_sub)

compteur = 0
total = len(liste_fichiers_sub)
for element in liste_fichiers_sub:
    subToTxt.filtrage(element,DOSSIER_DESTINATION,ENCODING)
    compteur += 1
    print(f"{compteur} / {total} fichier .sub traités")
print(f"{compteur} / {total} fichier .sub traités")

# # Récupérer la liste des .sub à transformer en texte
# liste_fichiers_sub = subToTxt.lister_sub(DOSSIER)
# # print(liste_fichiers_sub)

# compteur = 0
# total = len(liste_fichiers_sub)
# for element in liste_fichiers_sub:
#     subToTxt.filtrage(element,ENCODING)
#     compteur += 1
#     print(f"{compteur} / {total} fichier .sub traités")
# print(f"{compteur} / {total} fichier .sub traités")

##########################
###### LEMATISATION ######
##########################

# liste_fichiers_txt = lema.lister_txt(DOSSIER)

# compteur = 0
# total = len(liste_fichiers_txt)
# for element in liste_fichiers_txt:
#     lema.lematiser(element)
#     compteur += 1
#     print(f"{compteur} / {total} fichier .txt traités")
# print(f"{compteur} / {total} fichier .txt traités")