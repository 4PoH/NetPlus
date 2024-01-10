import pymongo

# Connexion à la base de données MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["SAE_C01"]
collection = database["séries"]
vue = database["vue_liste_series_mots"] 

pipeline = [
    {
        "$unwind": "$liste_series"
    },
    {
        "$group": {
            "_id": "$liste_series.serie",
            "mots": {"$addToSet": "$Mot"} 
        }
    },
    {
        "$project": {
            "_id": 0, 
            "serie": "$_id",
            "mots": 1
        }
    }
]

vue.insert_many(collection.aggregate(pipeline))

resultats_vue = vue.find()

client.close()