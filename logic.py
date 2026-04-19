import database
inventaire = database.charger()
albums = database.charger()

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
        
def afficher_details(nom):
    #Affiche tous les détails d'un artiste par son nom.
    resultats = [a for a in inventaire if nom.lower() in a.get("nom", "").lower()]
    
    if not resultats:
        print(f" Aucun artiste nommé '{nom}' trouvé.")
        return

    print(f"\n===== DÉTAILS DE L'ARTISTE =====")
    for artiste in resultats:
        print(f"\n  Nom    : {artiste.get('nom', 'Non renseigné')}")
        print(f"  Genre  : {artiste.get('genre', 'Non renseigné')}")
        print(f"  Pays   : {artiste.get('pays', 'Non renseigné')}")
        
        # Affiche ses albums si il en a
        ses_albums = [alb for alb in albums if alb.get("artiste", "").lower() == artiste.get("nom", "").lower()]
        if ses_albums:
            print(f"  Albums :")
            for alb in ses_albums:
                print(f" {alb.get('titre')} ({alb.get('annee')}) — {alb.get('streams')} streams")
        else:
            print(f"  Albums : Aucun album enregistré")
    print("====================================\n")


def rechercher(nom):
    #Recherche et affiche un artiste selon son nom.
    resultats = [e for e in inventaire if nom.lower() in e.get("nom", "").lower()]
    if resultats:
        print(f"\n Résultat(s) pour {nom} :")
        for r in resultats:
            print(r)
    else:
        print(f"Aucun résultat pour {nom}.")
        
def rechercher_par_genre(genre):
    #Recherche tous les artistes d'un genre donné.
    resultats = [a for a in inventaire if genre.lower() in a.get("genre", "").lower()]

    if resultats:
        print(f"\n Artistes du genre '{genre}' :")
        for i, artiste in enumerate(resultats, start=1):
            print(f"\n  {i} — {artiste.get('nom')} ({artiste.get('pays')})")
    else:
        print(f" Aucun artiste trouvé pour le genre '{genre}'.")
    print("====================================\n")

def ajouter_album(dictionnaire):
    #Ajoute un album. Le dictionnaire doit contenir : titre, annee, streams, artiste.
    albums.append(dictionnaire)
    print(f" Album '{dictionnaire.get('titre', 'Sans titre')}' ajouté avec succès !")


def afficher_albums():
    #Affiche tous les albums.
    if not albums:
        print(" Aucun album enregistré.")
        return

    print("\n===== TOUS LES ALBUMS =====")
    for i, album in enumerate(albums, start=1):
        print(f"\n--- Album {i} ---")
        print(f"  Titre   : {album.get('titre', 'Non renseigné')}")
        print(f"  Artiste : {album.get('artiste', 'Non renseigné')}")
        print(f"  Année   : {album.get('annee', 'Non renseigné')}")
        print(f"  Streams : {album.get('streams', 'Non renseigné')}")
    print("==============================\n")


def rechercher_album(titre):
    #Recherche un album par son titre.
    resultats = [alb for alb in albums if titre.lower() in alb.get("titre", "").lower()]

    if resultats:
        print(f"\n Résultat(s) pour '{titre}' :")
        for r in resultats:
            print(r)
    else:
        print(f" Aucun album trouvé pour '{titre}'.")


def supprimer_album(titre):
    #Supprime un album par son titre.
    global albums
    avant = len(albums)
    albums = [alb for alb in albums if alb.get("titre") != titre]

    if len(albums) < avant:
        print(f" Album '{titre}' supprimé.")
    else:
        print(f" Aucun album nommé '{titre}' trouvé.")
        
database.sauvegarder(inventaire)

