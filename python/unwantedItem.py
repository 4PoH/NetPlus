def remove_items(line):
  newline = line.replace('<i>', '').replace('</i>', '')
  newline = newline.replace(' -', '').replace('- ', '')
  newline = newline.replace('(', '').replace(')', '')
  newline = newline.replace(' :', '').replace(': ', '').replace(':', '')
  newline = newline.replace('...', '')
  newline = newline.replace('.', '')
  newline = newline.replace('?', '')
  newline = newline.replace('!', '')
  newline = newline.replace(',', '')
  newline = newline.replace('"', '')
  newline = newline.replace('--', '')
  newline = newline.replace("'", '')
  return newline