def Netplus():
    REPONSE = 0

    print("Bienvenue sur Netplus")
    while REPONSE != 3:
        
        REPONSE = input("Que voulez vous faire ? \n 1 - Recherche \n 1 - Recommendation \n 1 - Quitter")

        if REPONSE not in (1,2,3):
            print("Réponse invalide")
            pass

        if REPONSE == 1:
            ENTREE_RECHERCHE = input("Veuillez indiquer le nom d'une série ou des mots clés")

        if REPONSE == 2:
            ENTREE_RECHERCHE = input("Veuillez indiquer le nom d'une série ou des mots clés")

        if REPONSE == 3:
            ENTREE_RECHERCHE = input("Veuillez indiquer le nom d'une série ou des mots clés")
        
