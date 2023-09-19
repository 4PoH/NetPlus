import nom as nom
import srtToTxt as srtToTxt
import subToTxt as subToTxt
import assToTxt as assToTxt

#######################
###### VARIABLES ######
#######################

DOSSIER = "NetPlus\\data\\sous-titres-Copie"  # Remplacez par le chemin de votre dossier
FICHIER_CSV = "liste_dossiers.csv"   # Nom du fichier CSV de sortie
ENCODING = "ansi"

#######################
###### EXECUTION ######
#######################

# Récupérer le nom des series et les mettres dans le csv
# nom.lister_noms_dossiers(DOSSIER, FICHIER_CSV)
# nom.modifier_titres_majuscules(FICHIER_CSV)

# Récupérer la liste des .srt à transformer en texte
liste_fichiers_srt = srtToTxt.lister_srt(DOSSIER)

compteur = 0
for element in liste_fichiers_srt:
    srtToTxt.filtrage(element,ENCODING)
    compteur += 1
print(f"{compteur} / {len(liste_fichiers_srt)} traités")

# Récupérer la liste des .sub à transformer en texte
liste_fichiers_sub = subToTxt.lister_sub(DOSSIER)

# Récupérer la liste des .ass à transformer en texte
liste_fichiers_ass = assToTxt.lister_ass(DOSSIER)

# Récupérer les fichiers .txt pour exécuter le tf-idf

