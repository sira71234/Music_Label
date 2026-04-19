import database

def ajouter(dictionnaire):
    #Ajoute un dictionnaire (artiste/album) dans l'inventaire.
    catalogue = database.charger()


    database.sauvegarder(nouvel_artiste)
    print(f"'{dictionnaire.get('nom', 'Élément')}' ajouté avec succès !")


def afficher_tout():

    inventaire = database.charger()
    #Affiche tous les éléments stockés dans l'inventaire.
    if not inventaire:
        print("L'inventaire est vide pour l'instant.")
        return

    print("\n INVENTAIRE COMPLET ")
    for i, element in enumerate(inventaire, start=1):
        print(f"\n Artiste {i} ")
        for cle, valeur in element.items():
            print(f"  {cle} : {valeur}")
    print("=================================\n")

def supprimer(nom):

    global inventaire
    inventaire = database.charger()
    #Supprime un artiste de l'inventaire selon son nom.
    avant = len(inventaire)
    inventaire = [e for e in inventaire if e.get("nom") != nom]
    if len(inventaire) < avant:
        print(f"{nom} supprimé de l'inventaire.")
    else:
        print(f"Aucun artiste nommé {nom} trouvé.")

def rechercher(nom):
    #Recherche et affiche un artiste selon son nom.
    resultats = [e for e in inventaire if nom.lower() in e.get("nom", "").lower()]
    if resultats:
        print(f"\n Résultat(s) pour {nom} :")
        for r in resultats:
            print(r)
    else:
        print(f"Aucun résultat pour {nom}.")
