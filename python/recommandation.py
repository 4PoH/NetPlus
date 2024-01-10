from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pymongo

def recommander(nom_utilisateur):
    # Connexion à la base de données MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client["SAE_C01"]
    collection_series_mots = database["liste_series_mots"] 
    collection_utilisateurs = database["utilisateurs"]

    # Récupère la liste des séries visionnées par l'utilisateur
    utilisateur = collection_utilisateurs.find_one({"Nom": nom_utilisateur})

    if utilisateur:
        series_visionnees = [serie["Titre"] for serie in utilisateur.get("listeSeries", [])]
        if series_visionnees:
            # Récupère les mots-clés associés à toutes les séries
            resultats = collection_series_mots.find()
            series_data = [{"serie": resultat["serie"], "mots": resultat["mots"]} for resultat in resultats]

            # Construit la liste des mots-clés des séries visionnées par l'utilisateur
            mots_cles_series_visionnees = [" ".join(serie["mots"]) for serie in series_data if serie["serie"] in series_visionnees]

            # Convertit la liste de mots-clés en une seule chaîne
            str_mots_cles_series_visionnees = " ".join(mots_cles_series_visionnees)

            # Obtient les mots-clés de toutes les séries
            mots_cles_series = [" ".join(serie["mots"]) for serie in series_data]

            # Calcule la similarité cosinus
            tfidf_vectorizer = TfidfVectorizer()
            tfidf_matrix = tfidf_vectorizer.fit_transform(mots_cles_series)
            cosinus_similarite = linear_kernel(tfidf_vectorizer.transform([str_mots_cles_series_visionnees]), tfidf_matrix).flatten()

            # Trie les séries en fonction de la similarité
            indice_similarite_serie = cosinus_similarite.argsort()[::-1]

            # Affiche les séries similaires
            print(f"Séries similaires aux séries visionnées par l'utilisateur:")
            for index in indice_similarite_serie:
                if series_data[index]["serie"] not in series_visionnees:  # Excluez les séries déjà visionnées
                    serie_similaire = series_data[index]["serie"]
                    similarite = cosinus_similarite[index]
                    print(f"  - {serie_similaire} (Similarité : {similarite:.4f})")
        else:
            print("L'utilisateur n'a pas encore visionné de séries.")
    else:
        print("Utilisateur non trouvé.")

    # Fermeture de la connexion
    client.close()