import simplemma as slemma
import os

def lister_txt(dossierDepart):
    # Fonction pour obtenir la liste des fichiers sous un dossier donné
    txt_files = [] # Liste pour stocker les fichiers .txt
    for dirpath, dirnames, filenames in os.walk(dossierDepart, topdown=True):
        for filename in filenames:
            if filename.endswith(".txt"):
                path = os.path.join(dirpath, filename)
                if path not in txt_files:
                    txt_files.append(path)
                    # Ajouter le chemin du fichier .txt uniquement s'il n'est pas déjà dans la liste
    return txt_files

def lematiser(fichier):
    file = open(fichier, "r")
    texte = " ".join(slemma.text_lemmatizer(file.read(), lang=('en', 'fr'), greedy=True))
    file.close
 
    newfile = open(fichier, "w")
    newfile.write(texte)

#liste_txt = lister_txt("NetPlus\data\sous-titres-Copie1")
#lematiser("NetPlus/data/sous-titres-Copie1/breakingbad/breakingbad.txt")