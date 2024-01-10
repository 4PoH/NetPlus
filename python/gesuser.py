import pymongo

def getuser():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client["SAE_C01"]
    collection_utilisateurs = database["utilisateurs"]
    collection_series_mots = database["liste_series_mots"] 

    utilisateurs = list(collection_utilisateurs.find())

    for i in range(len(utilisateurs)):
        utilisateur = utilisateurs[i]
        series_visionnees = [serie["Titre"] for serie in utilisateur.get("listeSeries", [])]

        print(f"{i + 1}. {utilisateur['Nom']}")
        if series_visionnees:
            print("   Séries visionnées:")
            for serie in series_visionnees:
                print(f"      - {serie}")
        else:
            print("   Aucune série visionnée")

def liste_users():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client["SAE_C01"]
    collection_utilisateurs = database["utilisateurs"]

    utilisateurs = list(collection_utilisateurs.find())
    liste_users = []

    for i in range(len(utilisateurs)):
        utilisateur = utilisateurs[i]
        series_visionnees = [serie["Titre"] for serie in utilisateur.get("listeSeries", [])]
        nom_utilisateur = utilisateur['Nom']

        infos_utilisateur = {
            "Nom": nom_utilisateur,
            "Series_visionnees": series_visionnees
        }

        liste_users.append(infos_utilisateur)

    client.close()
    return liste_users

# getuser()
# print(liste_users())