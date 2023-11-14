import re
import os
import unidecode

def recup_dialogue(file_content, encoding="ansi"):
    lines = file_content.splitlines()
    subtitles = []
    for line in lines:
        if line.startswith("Dialogue:"):
            parts = line.split(',')
            start_time = parts[1]
            end_time = parts[2]
            text = ','.join(parts[9:]).strip()
            subtitles.append(f"{start_time} --> {end_time}\n{text}\n\n")
    return '\n'.join(subtitles)

def cleanSubtitleText(subtitle_text):
    # Utiliser une expression régulière pour retirer les balises de formatage et les timestamps
    cleaned_text = re.sub(r'{\\[^}]+}', '', subtitle_text)
    cleaned_text = re.sub(r'\d+:\d+:\d+\.\d+ --> \d+:\d+:\d+\.\d+\n', '', cleaned_text)
    
    # Retirer les retours à la ligne et les espaces en double
    cleaned_text = cleaned_text.replace('\n', ' ').replace('  ', ' ')
    
    # Remplacer les occurrences de \N par un espace
    cleaned_text = cleaned_text.replace('\\N', ' ')
    
    return cleaned_text.strip()

###############################
###############################

def filtrage(fichier, fichier_destination, encoding='utf-8'):
    """
    fichier : nom fichier srt
    encoding : encoding par défaut : utf-8
    """
    new_lines = []

    with open(fichier, encoding=encoding, errors='replace') as f:
        lines = f.readlines()
        dialogue = recup_dialogue(lines,encoding)
        new_lines.extend(cleanSubtitleText(dialogue))

    # Crée le dossier si nécessaire
    destination_folder = os.path.dirname(fichier_destination)
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    mode = 'a' if os.path.exists(fichier_destination) else 'w'  # Détermine le mode d'ouverture

    destination = os.path.normpath(fichier_destination)

    with open(destination, mode) as f:
        for line in new_lines:
            line = unidecode.unidecode(line)
            f.write(line)

###############################
###############################




# # Exemple d'utilisation
# input_file = "data/tests-Copie/desperatehousewives/Desperate.Housewives.612.2hd.EN.TAG.ass"
# result = recup_dialogue(input_file)
# final = cleanSubtitleText(result)

# # Afficher le résultat
# #print(result)
# print(final)
