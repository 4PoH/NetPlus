from simplemma import text_lemmatizer
import pymongo

# Connexion à la base de données MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["SAE_C01"]
collection = database["séries"]
vue = database["vue_nom_series"]

# Permet de lemmatiser un "texte"
def lemmatiser(texte):
    texte_lemmatise = " ".join(text_lemmatizer(texte, lang=('en', 'fr'), greedy=True))
    return texte_lemmatise

# Recupère les mots clés écrits dans le input par l'utilisateur 
def recup_mot_cles():
    mots_cles_entree = input("Entrez les mots-clés de recherche : ")
    return mots_cles_entree

# Permet de rechercher les séries dans la collection en lien avec les mots clés choisis 
# Renvoi les séries ainsi que la somme de leurs poids
def recherche_series_coll(mots_cles_recherche):

    collection = database["séries"]
    vue = database["vue_nom_series"]

    # Pour la recherche des séries
    mots_cles_lemm = lemmatiser(mots_cles_recherche).split()

    series_totales = []  # Liste pour stocker toutes les séries

    # Récupère les documents de la collection qui correspondent aux mots-clés spécifiés
    documents = collection.find({"Mot": {"$in": mots_cles_lemm}})
    nom_series = vue.find()
    serie_trouvee = False

    liste_series = []

    # Vérifie si le mot-clé correspond à une/des série(s) dans la vue
    for nom_serie in nom_series:
        if mots_cles_recherche.lower() in nom_serie["_id"].lower():
            serie_trouvee = True
            liste_series.append(nom_serie["_id"])

    # Affiche toutes les séries trouvées
    print("Liste des séries trouvées :", liste_series)

    # Ajoute les séries associées à chaque mot-clé dans la liste
    for document in documents:
        liste_series = document["liste_series"]
        series_totales.extend(liste_series)

    # Calcule la somme des poids associés à chaque série
    somme_poids_par_serie = {}

    for serie in series_totales:
        nom_serie = serie["serie"]
        poids_serie = serie["poids"]

        if mots_cles_recherche.lower() in nom_serie.lower() and serie_trouvee:
            poids_serie = 100
            
        # Incrémente le poids d'une série si déjà présent dans la liste
        # Sinon ajoute la série ainsi que son poids
        if nom_serie in somme_poids_par_serie:
            somme_poids_par_serie[nom_serie] += poids_serie
        else:
            somme_poids_par_serie[nom_serie] = poids_serie

    # Trie le dictionnaire par poids de manière décroissante
    sorted_dict = dict(sorted(somme_poids_par_serie.items(), key=lambda item: item[1], reverse=True))
    
    # Affiche la somme des poids par série triée
    print("\nSomme des poids par série :")

    # # Si la série n'est pas trouvée dans la vue, mais la liste des séries est vide, l'ajoute avec un poids de 100
    # if serie_trouvee and not sorted_dict:
    #     for serie in liste_series:
    #         print(f"  - Série : {serie}, Poids : 100")

    # for nom_serie, somme_poids in sorted_dict.items():
    #     somme_poids_affichee = min(somme_poids, 100)
    #     print(f"  - Série : {nom_serie}, Somme des poids : {somme_poids_affichee}")

    # Si la série n'est pas trouvée dans la vue, mais la liste des séries est vide, l'ajoute avec un poids de 100
    if serie_trouvee and not sorted_dict:
        for serie in liste_series:
            print(f"{serie}")

    for nom_serie, somme_poids in sorted_dict.items():
        somme_poids_affichee = min(somme_poids, 100)
        print(f"{nom_serie}")
    
    client.close()

# Obtenir les mots clés de recherche de l'utilisateur
#  
#mots_cles_recherche = recup_mot_cles()

#recherche_series_coll(vue, collection, mots_cles_recherche)

#client.close()