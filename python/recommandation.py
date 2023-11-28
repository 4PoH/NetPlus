import pymongo

# Établir la connexion avec la base de données
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.SAEC01

# Fonctions
def get_series_user(userid):
    series_user = []
    user = db.utilisateurs.find_one({'id': userid})
    for serie in user['listeSeries']:
        series_user.append(serie) 
    return series_user

def get_all_series():
    series = []
    result_request = db.vue_nom_series.distinct('_id')
    for serie in result_request:
        series.append(serie)
    return series

# Variables fixé
UserID = 123

# Tests
# series_user_test = get_series_user(UserID)
# print(series_user_test)

series = get_all_series()
print(series)

def mots_pour_serie(nom_serie):
    result = db.séries.find({"liste_series.serie": nom_serie}, {"Mot": 1, "_id": 0})
    mots = [doc["Mot"] for doc in result]
    return mots

# Exemple d'utilisation de la fonction avec le nom d'une série
serie_a_rechercher = "Lost"  # Remplacez par le nom de la série recherchée
mots_contenant_serie = mots_pour_serie(serie_a_rechercher)

print(f"Les mots contenant la série '{serie_a_rechercher}':")
print(mots_contenant_serie)