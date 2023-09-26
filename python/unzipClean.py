import os
import zipfile

def unzip_clean(starting_dir, return_broken_zip=False):
    again = True
    broken_zip = []
    while(again):
        again = False
        for path, dirs, files in os.walk(starting_dir):
            for filename in files:
                if filename.endswith('.zip') and filename not in broken_zip:
                    again = True
                    try:
                        fichierzip = (path + '/' + filename)
                        with zipfile.ZipFile(fichierzip, 'r') as zip_ref:
                            zip_ref.extractall(path)
                        print(f"FINISH : {filename}")
                        os.remove(fichierzip)
                    except:
                        broken_zip.append(filename)
                        print(f" ERROR : {filename}")
                        continue
    if return_broken_zip == True:
        return_broken_zip