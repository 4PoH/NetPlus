import os
import re
import unidecode

###############################
###############################

def lister_sub(dossierDepart):
    # Fonction pour obtenir la liste des fichiers sous un dossier donné
    sub_files = [] # Liste pour stocker les fichiers .sub
    for dirpath, dirnames, filenames in os.walk(dossierDepart, topdown=True):
        for filename in filenames:
            if filename.endswith(".sub") or filename.endswith(".SUB"):
                path = os.path.join(dirpath, filename)
                if path not in sub_files:
                    sub_files.append(path)
                    # Ajouter le chemin du fichier .sub uniquement s'il n'est pas déjà dans la liste
    return sub_files

###############################
###############################

def remove_timestamp(line):
    new_line = re.sub(r'\{\d+\}\{\d+\}', '', line)
    return new_line

###############################
###############################

def has_letters(line):
  if re.search('[a-zA-Z]', line):
    return True
  return False

###############################
###############################

def has_no_text(line):
  l = line.strip()
  if not len(l):
    return True
  if l.isnumeric():
    return True
  if l[0] == '(' and l[-1] == ')':
    return True
  if not has_letters(line):
    return True
  return False

###############################
###############################

def is_lowercase_letter_or_comma(letter):
  if letter.isalpha() and letter.lower() == letter:
    return True
  if letter == ',':
    return True
  return False

###############################
###############################

def clean_up(lines):
  new_lines = []
  for line in lines[1:]:
    line = remove_timestamp(line)
    if has_no_text(line):
      continue  
    elif len(new_lines) and is_lowercase_letter_or_comma(line[0]):
      # combine with previous line
      new_lines[-1] = new_lines[-1].strip() + ' ' + line.lower()  # Convert to lowercase
    else:
      # append line
      new_lines.append(line.lower())  # Convert to lowercase
  return new_lines

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
        new_lines.extend(clean_up(lines))

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

#filtrage("NetPlus\data\sous-titres-Copie1\southpark\South Park - 7x01 - Cancelled.en.sub")