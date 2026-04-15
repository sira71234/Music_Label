inventaire = []

def ajouter(dictionnaire):
    #Ajoute un dictionnaire (artiste/album) dans l'inventaire.
    inventaire.append(dictionnaire)
    print(f"'{dictionnaire.get('nom', 'Élément')}' ajouté avec succès !")


def afficher_tout():
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
    #Supprime un artiste de l'inventaire selon son nom.
    global inventaire
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


if __name__ == "__main__":

    # On simule l'ajout de quelques artistes
    ajouter({"nom": "Fally Ipupa", "genre": "Afrobeat", "pays": "RDC"})
    ajouter({"nom": "Burna Boy", "genre": "Afrobeat", "pays": "Nigeria"})
    ajouter({"nom": "Aya Nakamura", "genre": "Afropop", "pays": "Mali"})

    # On affiche tout
    afficher_tout()

    # On teste la recherche
    rechercher("burna")

    # On teste la suppression
    supprimer("Fally Ipupa")
    afficher_tout()