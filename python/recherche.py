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

# Recupère les mots clés écrit dans le input par l'utilisateur 
# Et les lemmatise pour la recherche des séries
def recup_mot_cles_lemm():
    mots_cles_entree = input("Entrez les mots-clés de recherche : ")
    return mots_cles_entree

# Permet de rechercher les séries dans la collection en lien avec les mots clés choisis 
# Renvoi les séries ainsi que la somme de leurs poids
def recherche_series_coll(vue, collection, mots_cles_recherche):
    mots_cles_lemm = lemmatiser(mots_cles_recherche).split()

    series_totales = []  # Liste pour stocker toutes les séries

    # Récupère les documents de la collection qui correspondent aux mots-clés spécifiés
    documents = collection.find({"Mot": {"$in": mots_cles_lemm}})
    nom_series = vue.find()

    # mots_cles_lemm = "Breaking Bad"
    for nom_serie in nom_series:
        if nom_serie["_id"] == mots_cles_lemm:
            print("Serie Trouvee !!!")
        else:
            print("introuvable")

    
    for resultat in nom_series:
        print(resultat)

    # Ajoute les séries associées à chaque mot-clé dans la liste
    for document in documents:
        liste_series = document["liste_series"]
        series_totales.extend(liste_series)

    # Affiche la liste totale des séries
    # Autant de liste que de mots clés recherchées
    print("Liste totale des séries associées :")
    for serie in series_totales:
        print(f"  - Série : {serie['serie']}, Poids : {serie['poids']}")

    # Calcule la somme des poids associés à chaque série
    somme_poids_par_serie = {}
    for serie in series_totales:
        nom_serie = serie["serie"]
        poids_serie = serie["poids"]
        # Incrémente le poids d'une série si déjà présent dans la liste
        # Sinon ajoute la série ainsi que son poids
        if nom_serie in somme_poids_par_serie:
            somme_poids_par_serie[nom_serie] += poids_serie
        else:
            somme_poids_par_serie[nom_serie] = poids_serie

    # Sort (tri) le dictionnaire
    # Afin d'avoir les plus haut poids en premiers
    sorted_dict = dict(sorted(somme_poids_par_serie.items(), key=lambda item: item[1], reverse=True))

    # Affiche la somme des poids par série triée
    print("\nSomme des poids par série :")
    for nom_serie, somme_poids in sorted_dict.items():
        print(f"  - Série : {nom_serie}, Somme des poids : {somme_poids}")

# Obtenir les mots clés de recherche de l'utilisateur
mots_cles_recherche = recup_mot_cles_lemm()

recherche_series_coll(vue, collection, mots_cles_recherche)

client.close()