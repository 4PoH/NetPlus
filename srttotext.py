import os
import re

###############################
ORIGIN_DIRECTORY = "tests"
###############################

def directories_with_srt(directory):
    srt_directories = [] # List to stock the directories
    for dirpath, dirnames, filenames in os.walk(directory, topdown=True):
        if any(filename.endswith(".srt") for filename in filenames):
            if dirpath not in srt_directories:
                srt_directories.append(dirpath)
                # Add directories only if they contains .srt file and aren't already in the list
    return srt_directories

def is_timestamp(l):
    return True if l[:2].isnumeric() and l[2] == ':' else False

def is_text_content(line):
    return True if re.search('[a-zA-Z]', line) else False

def has_no_text(line):
    if not len(line):
        return True
    if line.isnumeric():
        return True
    if is_timestamp(line):
        return True
    if line[0] == '(' and line[-1] == ')':
        return True
    if not is_text_content(line):
        return True
    return False

def filter_lines(lines):
    """ Remove timestamps, any lines without text, and line breaks """
    new_lines = []
    for line in lines[1:]:
        line = line.strip()
        if has_no_text(line):
            continue
        else:
            # Strip the line of text before adding it to the list
            new_lines.append(line)

    # Combine the lines into a single data string
    return ' '.join(new_lines)

def file_srt_to_txt(file_name, cur_dir, new_dir, encoding):
    with open(os.path.join(cur_dir, file_name), 'r', encoding=encoding, errors='replace') as f:
        data = filter_lines(f.readlines())
    new_file_name = os.path.join(cur_dir, new_dir, file_name[:-4]) + '.txt'
    with open(new_file_name, 'w') as f:
        f.write(data)

def main(directorypath):
    if not os.path.isdir(directorypath):
        print('Enter a valid directory path')
        exit()

    encoding = 'ansi'

    # Create a dedicated directory for the converted files
    new_dir = 'srt_to_txt'
    try:
        os.makedirs(os.path.join(directorypath, new_dir))
    except FileExistsError:
        # Directory already exists
        pass

    with os.scandir(directorypath) as dir_it:
        for file_entry in dir_it:
            if file_entry.name.endswith(".srt") and file_entry.is_file():
                file_srt_to_txt(file_entry.name, directorypath, new_dir, encoding)

srt_files_list = directories_with_srt(ORIGIN_DIRECTORY)
totalfiles = len(srt_files_list)
print(srt_files_list)
print(totalfiles)

nbfiles = 0
for element in srt_files_list:
    main(element)
    nbfiles += 1
    print(str(nbfiles) + '/' + str(totalfiles))