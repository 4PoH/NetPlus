import os
import re
import unidecode
import unwantedItem

###############################
###############################

def lister_srt(dossierDepart):
    # Fonction pour obtenir la liste des fichiers sous un dossier donné
    srt_files = [] # Liste pour stocker les fichiers .srt
    for dirpath, dirnames, filenames in os.walk(dossierDepart, topdown=True):
        for filename in filenames:
            if filename.endswith(".srt") or filename.endswith(".SRT"):
                path = os.path.join(dirpath, filename)
                if path not in srt_files:
                    srt_files.append(path)
                    # Ajouter le chemin du fichier .srt uniquement s'il n'est pas déjà dans la liste
    return srt_files

###############################
###############################

def is_time_stamp(l):
  if l[:2].isnumeric() and l[2] == ':':
    return True
  return False

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
  if is_time_stamp(l):
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
  inside_i_tag = False

  for line in lines[1:]:
    line = unwantedItem.remove_items(line)
    if has_no_text(line):
      continue
    if '<i>' in line:
      inside_i_tag = True
      line = line.replace('<i>', '')
    if '</i>' in line:
      inside_i_tag = False
      line = line.replace('</i>', '')

    if inside_i_tag and len(new_lines):
      new_lines[-1] += ' ' + line.lower()
    else:
      new_lines.append(line.lower())
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

###############################
###############################