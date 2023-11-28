import re
import os
import unidecode
import unwantedItem

def recup_dialogue(input_lines):
    subtitles = []
    for line in input_lines:
        if line.startswith("Dialogue:"):
            parts = line.split(',')
            start_time = parts[1]
            end_time = parts[2]
            text = ','.join(parts[9:]).strip()
            subtitles.append(f"{start_time} --> {end_time}\n{text}\n\n")
    return subtitles

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
        dialogues = recup_dialogue(lines)
        for dialogue in dialogues:
            cleaned_text = unwantedItem.remove_items(dialogue)
            new_lines.extend(cleaned_text)

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
