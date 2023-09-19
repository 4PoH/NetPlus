import os
import re
import unidecode

###############################
###############################

def lister_srt(dossierDepart):
    c1,c2,c3,c4 = 0,0,0,0
    # Fonction pour obtenir la liste des fichiers sous un dossier donné
    srt_files = [] # Liste pour stocker les fichiers .srt
    for dirpath, dirnames, filenames in os.walk(dossierDepart, topdown=True):
      for filename in filenames:
        if (filename.endswith(".srt")):
          path = os.path.join(dirpath, filename)
          if path not in srt_files:
            c1 += 1
            srt_files.append(path)
            # Ajouter le chemin du fichier .srt uniquement s'il n'est pas déjà dans la liste

        if (filename.endswith(".SRT")):
          path = os.path.join(dirpath, filename)
          if path not in srt_files:
            c2 += 1
            srt_files.append(path)
            # Ajouter le chemin du fichier .srt uniquement s'il n'est pas déjà dans la liste

        if (filename.endswith(".vo")):
          path = os.path.join(dirpath, filename)
          if path not in srt_files:
            c3 += 1
            srt_files.append(path)
            # Ajouter le chemin du fichier .srt uniquement s'il n'est pas déjà dans la liste

        if (filename.endswith(".VO")):
          path = os.path.join(dirpath, filename)
          if path not in srt_files:
            c4 += 1
            srt_files.append(path)
            # Ajouter le chemin du fichier .srt uniquement s'il n'est pas déjà dans la liste
    print(f"c1 = {c1}, c2 = {c2}, c3 = {c3}, c4 = {c4}")
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

def remove_items(line):
  newline = line.replace('<i>', '').replace('</i>', '')
  newline = newline.replace(' -', '').replace('- ', '')
  newline = newline.replace(' :', '').replace(': ', '').replace(':', '')
  newline = newline.replace('...', '')
  newline = newline.replace('.', '')
  newline = newline.replace('?', '')
  newline = newline.replace('!', '')
  newline = newline.replace(',', '')
  newline = newline.replace('"', '')
  return newline

###############################
###############################

def clean_up(lines):
  """
  Get rid of all non-text lines and
  try to combine text broken into multiple lines
  Also, convert all characters to lowercase
  """
  new_lines = []
  for line in lines[1:]:
    line = remove_items(line)
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

def filtrage(fichier, encoding='utf-8'):
  """
  fichier : nom fichier srt
  encoding : encoding par default : utf-8
  """
  new_lines = []

  with open(fichier, encoding=encoding, errors='replace') as f:
    lines = f.readlines()
    new_lines.extend(clean_up(lines))

  dossier_name = os.path.basename(os.path.dirname(fichier))  # Obtient le nom du répertoire
  new_file_name = os.path.join(os.path.dirname(fichier), f"{dossier_name}.txt")  # Crée le nom du fichier texte

  mode = 'a' if os.path.exists(new_file_name) else 'w'  # Détermine le mode d'ouverture

  with open(new_file_name, mode) as f:
    for line in new_lines:
      line = unidecode.unidecode(line)
      f.write(line)
  #print(new_file_name)

###############################
###############################