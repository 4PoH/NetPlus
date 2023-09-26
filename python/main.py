import nom as nom
import srtToTxt as srtToTxt
import subToTxt as subToTxt
import assToTxt as assToTxt
import os

#######################
###### VARIABLES ######
#######################

DOSSIER = "NetPlus\data\\testscopy"  # Remplacez par le chemin de votre dossier
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

print(compteur(DOSSIER))

#######################
###### EXECUTION ######
#######################

# Dézipper les fichiers à partir du répertoire donné


# Récupérer le nom des series et les mettres dans le csv
# nom.lister_noms_dossiers(DOSSIER, FICHIER_CSV)
# nom.modifier_titres_majuscules(FICHIER_CSV)

# Récupérer la liste des .srt à transformer en texte
liste_fichiers_srt = srtToTxt.lister_srt(DOSSIER)
#print(liste_fichiers_srt)

compteur = 0
total = len(liste_fichiers_srt)
#print(liste_fichiers_srt)
for element in liste_fichiers_srt:
    #print(element) # Pour voir le nom des fichiers qui sont traités
    srtToTxt.filtrage(element,ENCODING)
    compteur += 1
    print(f"{compteur} / {total} traités")
print(f"{compteur} / {total} traités")

# #srtToTxt.filtrage("data\\testZippage\\sous-titres-adezipper\\xfiles\\XFiles-s09e19-20.srt", ENCODING)


# # Récupérer la liste des .sub à transformer en texte
# liste_fichiers_sub = subToTxt.lister_sub(DOSSIER)
# print("2")
# # Récupérer la liste des .ass à transformer en texte
# liste_fichiers_ass = assToTxt.lister_ass(DOSSIER)
# print("3")
# # Récupérer les fichiers .txt pour exécuter le tf-idf

# #print(liste_fichiers_srt, liste_fichiers_sub, liste_fichiers_ass)