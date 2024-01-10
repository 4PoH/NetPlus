import recherche as recherche
import gesuser as gesuser
import recommandation as recommandation

def Netplus():
    REPONSE = 0

    print("\n|-----------------------------------------------|\n|------------ Bienvenue sur Netplus ------------|\n|-----------------------------------------------|")
    while REPONSE != 3:
        
        REPONSE = input("\n|----------- Que voulez vous faire ? -----------|\n| 1 - Recherche                                 |\n| 2 - Recommendation                            |\n| 3 - Quitter                                   |\n|-----------------------------------------------| \nVotre réponse : ")

        if REPONSE not in ("1", "2", "3"):
            print("Réponse invalide")
            pass

        if REPONSE == "1":
            ENTREE_RECHERCHE = input("Veuillez indiquer le nom d'une série ou des mots clés")
            recherche.recherche_series_coll(ENTREE_RECHERCHE)

        if REPONSE == "2":
            print("Veuillez indiquer l'utilisateur pour lequel vous voulez des séries")
            users = gesuser.liste_users()
            afficher_utilisateurs(users)
            ENTREE_RECOMMENDATION = input("Veuillez indiquer le nom de l'utilisateur : ")
            recommandation.recommander(ENTREE_RECOMMENDATION)
            # Prévoir mauvais user

        if REPONSE == "3":
            print("\n|-----------------------------------------------|\n|- Merci d'avoir utiliser Netplus et à bientôt -|\n|-----------------------------------------------|")
            break

def afficher_utilisateurs(users):
    for i, user in enumerate(users, start=1):
        print(f"{i}. {user['Nom']}")
        print("   Séries visionnées:")
        for serie in user['Series_visionnees']:
            print(f"      - {serie}")

Netplus()
