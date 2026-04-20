import database


def _charger_catalogue() -> list[dict]:
    return database.charger()


def _sauvegarder_catalogue(catalogue: list[dict]) -> None:
    database.sauvegarder(catalogue)


def _normaliser_texte(valeur: str) -> str:
    return str(valeur).strip().casefold()


def _convertir_entier(valeur, defaut: int = 0) -> int:
    try:
        return int(valeur)
    except (TypeError, ValueError):
        return defaut


def _prochain_id(catalogue: list[dict]) -> str:
    plus_grand_id = 0

    for artiste in catalogue:
        identifiant = str(artiste.get("id", ""))
        if identifiant.startswith("ART-"):
            try:
                plus_grand_id = max(plus_grand_id, int(identifiant.split("-")[1]))
            except (IndexError, ValueError):
                continue

    return f"ART-{plus_grand_id + 1:03d}"


def _trouver_index_artiste(catalogue: list[dict], nom: str) -> int | None:
    nom_normalise = _normaliser_texte(nom)

    for index, artiste in enumerate(catalogue):
        if _normaliser_texte(artiste.get("nom", "")) == nom_normalise:
            return index

    return None


def _trouver_index_album(albums: list[dict], titre: str) -> int | None:
    titre_normalise = _normaliser_texte(titre)

    for index, album in enumerate(albums):
        if _normaliser_texte(album.get("titre", "")) == titre_normalise:
            return index

    return None


def _normaliser_album(album: dict) -> dict:
    return {
        "titre": str(album.get("titre", "")).strip(),
        "annee": _convertir_entier(album.get("annee"), 0),
        "streams": _convertir_entier(album.get("streams"), 0),
    }


def _afficher_artiste(artiste: dict, details: bool = False) -> None:
    albums = artiste.get("albums", [])
    if not isinstance(albums, list):
        albums = []

    print(f"ID     : {artiste.get('id', 'N/A')}")
    print(f"Nom    : {artiste.get('nom', 'Inconnu')}")
    print(f"Genre  : {artiste.get('genre', 'Inconnu')}")
    print(f"Pays   : {artiste.get('pays', 'Inconnu')}")
    print(f"Albums : {len(albums)}")

    if details and albums:
        print("Albums :")
        for album in albums:
            print(
                f"  - {album.get('titre', 'Sans titre')} "
                f"({album.get('annee', 'N/A')}) - {album.get('streams', 0)} streams"
            )


def ajouter(dictionnaire: dict) -> bool:
    return ajouter_artiste(dictionnaire)


def ajouter_artiste(dictionnaire: dict) -> bool:
    catalogue = _charger_catalogue()
    nom = str(dictionnaire.get("nom", "")).strip()

    if not nom:
        print("Le nom de l'artiste est obligatoire.")
        return False

    if _trouver_index_artiste(catalogue, nom) is not None:
        print(f"Un artiste nomme '{nom}' existe deja.")
        return False

    albums = dictionnaire.get("albums", [])
    if not isinstance(albums, list):
        albums = []

    nouvel_artiste = {
        "id": str(dictionnaire.get("id") or _prochain_id(catalogue)),
        "nom": nom,
        "genre": str(dictionnaire.get("genre", "")).strip() or "Inconnu",
        "pays": str(dictionnaire.get("pays", "")).strip() or "Inconnu",
        "albums": [
            _normaliser_album(album)
            for album in albums
            if isinstance(album, dict) and str(album.get("titre", "")).strip()
        ],
    }

    catalogue.append(nouvel_artiste)
    _sauvegarder_catalogue(catalogue)
    print(f"'{nouvel_artiste['nom']}' ajoute avec succes.")
    return True


def modifier_artiste(nom: str, nouvelles_donnees: dict) -> bool:
    catalogue = _charger_catalogue()
    index = _trouver_index_artiste(catalogue, nom)

    if index is None:
        print(f"Aucun artiste nomme '{nom}' trouve.")
        return False

    artiste = catalogue[index]
    nouveau_nom = str(nouvelles_donnees.get("nom", "")).strip()
    if nouveau_nom and _normaliser_texte(nouveau_nom) != _normaliser_texte(nom):
        if _trouver_index_artiste(catalogue, nouveau_nom) is not None:
            print(f"Un artiste nomme '{nouveau_nom}' existe deja.")
            return False
        artiste["nom"] = nouveau_nom

    for champ in ("genre", "pays"):
        valeur = str(nouvelles_donnees.get(champ, "")).strip()
        if valeur:
            artiste[champ] = valeur

    _sauvegarder_catalogue(catalogue)
    print(f"Les informations de '{artiste['nom']}' ont ete mises a jour.")
    return True


def afficher_tout() -> list[dict]:
    catalogue = _charger_catalogue()

    if not catalogue:
        print("Le catalogue est vide pour l'instant.")
        return []

    print("\nCATALOGUE COMPLET")
    print("=" * 40)
    for index, artiste in enumerate(catalogue, start=1):
        print(f"\nArtiste {index}")
        _afficher_artiste(artiste)
    print("\n" + "=" * 40)
    return catalogue


def supprimer(nom: str) -> bool:
    return supprimer_artiste(nom)


def supprimer_artiste(nom: str) -> bool:
    catalogue = _charger_catalogue()
    index = _trouver_index_artiste(catalogue, nom)

    if index is None:
        print(f"Aucun artiste nomme '{nom}' trouve.")
        return False

    artiste = catalogue.pop(index)
    _sauvegarder_catalogue(catalogue)
    print(f"{artiste.get('nom', nom)} a ete supprime du catalogue.")
    return True


def rechercher(nom: str) -> list[dict]:
    return rechercher_par_nom(nom)


def rechercher_par_nom(nom: str) -> list[dict]:
    catalogue = _charger_catalogue()
    terme = _normaliser_texte(nom)
    resultats = [
        artiste
        for artiste in catalogue
        if terme and terme in _normaliser_texte(artiste.get("nom", ""))
    ]

    if resultats:
        print(f"\nResultat(s) pour '{nom}' :")
        for artiste in resultats:
            print("-" * 30)
            _afficher_artiste(artiste)
    else:
        print(f"Aucun resultat pour '{nom}'.")

    return resultats


def rechercher_par_genre(genre: str) -> list[dict]:
    catalogue = _charger_catalogue()
    terme = _normaliser_texte(genre)
    resultats = [
        artiste
        for artiste in catalogue
        if terme and terme in _normaliser_texte(artiste.get("genre", ""))
    ]

    if resultats:
        print(f"\nArtistes trouves pour le genre '{genre}' :")
        for artiste in resultats:
            print("-" * 30)
            _afficher_artiste(artiste)
    else:
        print(f"Aucun artiste trouve pour le genre '{genre}'.")

    return resultats


def afficher_details_artiste(nom: str) -> dict | None:
    catalogue = _charger_catalogue()
    index = _trouver_index_artiste(catalogue, nom)

    if index is None:
        print(f"Aucun artiste nomme '{nom}' trouve.")
        return None

    artiste = catalogue[index]
    print("\nDETAILS DE L'ARTISTE")
    print("=" * 40)
    _afficher_artiste(artiste, details=True)
    print("=" * 40)
    return artiste


def ajouter_album(nom_artiste: str, album: dict) -> bool:
    catalogue = _charger_catalogue()
    index = _trouver_index_artiste(catalogue, nom_artiste)

    if index is None:
        print(f"Aucun artiste nomme '{nom_artiste}' trouve.")
        return False

    artiste = catalogue[index]
    albums = artiste.get("albums", [])
    if not isinstance(albums, list):
        albums = []
        artiste["albums"] = albums
    titre = str(album.get("titre", "")).strip()

    if not titre:
        print("Le titre de l'album est obligatoire.")
        return False

    if _trouver_index_album(albums, titre) is not None:
        print(f"L'album '{titre}' existe deja pour cet artiste.")
        return False

    nouvel_album = _normaliser_album(album)
    albums.append(nouvel_album)
    _sauvegarder_catalogue(catalogue)
    print(f"L'album '{titre}' a ete ajoute a '{artiste.get('nom', nom_artiste)}'.")
    return True


def modifier_album(nom_artiste: str, titre_album: str, nouvelles_donnees: dict) -> bool:
    catalogue = _charger_catalogue()
    index_artiste = _trouver_index_artiste(catalogue, nom_artiste)

    if index_artiste is None:
        print(f"Aucun artiste nomme '{nom_artiste}' trouve.")
        return False

    artiste = catalogue[index_artiste]
    albums = artiste.get("albums", [])
    if not isinstance(albums, list):
        albums = []
        artiste["albums"] = albums
    index_album = _trouver_index_album(albums, titre_album)

    if index_album is None:
        print(f"Aucun album nomme '{titre_album}' trouve pour '{artiste.get('nom', nom_artiste)}'.")
        return False

    album = albums[index_album]
    nouveau_titre = str(nouvelles_donnees.get("titre", "")).strip()
    if nouveau_titre and _normaliser_texte(nouveau_titre) != _normaliser_texte(titre_album):
        if _trouver_index_album(albums, nouveau_titre) is not None:
            print(f"Un album nomme '{nouveau_titre}' existe deja pour cet artiste.")
            return False
        album["titre"] = nouveau_titre

    if str(nouvelles_donnees.get("annee", "")).strip():
        album["annee"] = _convertir_entier(nouvelles_donnees.get("annee"), album.get("annee", 0))

    if str(nouvelles_donnees.get("streams", "")).strip():
        album["streams"] = _convertir_entier(
            nouvelles_donnees.get("streams"),
            album.get("streams", 0),
        )

    _sauvegarder_catalogue(catalogue)
    print(f"L'album '{album.get('titre', titre_album)}' a ete mis a jour.")
    return True


def supprimer_album(nom_artiste: str, titre_album: str) -> bool:
    catalogue = _charger_catalogue()
    index_artiste = _trouver_index_artiste(catalogue, nom_artiste)

    if index_artiste is None:
        print(f"Aucun artiste nomme '{nom_artiste}' trouve.")
        return False

    artiste = catalogue[index_artiste]
    albums = artiste.get("albums", [])
    if not isinstance(albums, list):
        albums = []
        artiste["albums"] = albums
    index_album = _trouver_index_album(albums, titre_album)

    if index_album is None:
        print(f"Aucun album nomme '{titre_album}' trouve pour '{artiste.get('nom', nom_artiste)}'.")
        return False

    album = albums.pop(index_album)
    _sauvegarder_catalogue(catalogue)
    print(f"L'album '{album.get('titre', titre_album)}' a ete supprime.")
    return True
