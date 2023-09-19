import os
import zipfile
import shutil
import time

def unzip_and_cleanup(repertoire):
    start_time = time.time()  # Enregistre le temps de début

    for root, dirs, files in os.walk(repertoire):
        for filename in files:
            if filename.endswith('.zip'):
                zip_path = os.path.join(root, filename)
                extraction_path = os.path.join(root, 'temp_folder')
                os.makedirs(extraction_path, exist_ok=True)

                try:
                    # Vérification si le fichier est un zip
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(extraction_path)
                except zipfile.BadZipFile as e:
                    print(f"Le fichier {zip_path} n'est pas un fichier zip valide.")
                    continue

                # Déplacement des fichiers extraits vers le répertoire parent
                for extracted_file in os.listdir(extraction_path):
                    extracted_path = os.path.join(extraction_path, extracted_file)
                    new_path = os.path.join(root, extracted_file)
                    if not os.path.exists(new_path):
                        os.rename(extracted_path, new_path)

                # Suppression du répertoire temporaire
                shutil.rmtree(extraction_path)

                # Suppression du fichier zip
                os.remove(zip_path)

    end_time = time.time()  # Enregistre le temps de fin
    execution_time = end_time - start_time  # Calcule le temps d'exécution

    print(f"L'exécution a pris {execution_time:.2f} secondes.")

unzip_and_cleanup('NetPlus\\data\\testZippage\\sous-titres-adezipper-Copie')