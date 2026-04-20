def _demander_texte(message: str) -> str:
    return input(message).strip()


def recuperer_info() -> dict:
    return recuperer_artiste()


def recuperer_artiste() -> dict:
    print("\n=== AJOUT D'UN ARTISTE ===")
    return {
        "nom": _demander_texte("Nom : "),
        "genre": _demander_texte("Genre : "),
        "pays": _demander_texte("Pays : "),
        "albums": [],
    }


def recuperer_mise_a_jour_artiste() -> dict:
    print("\n=== MODIFICATION D'UN ARTISTE ===")
    print("Laissez vide un champ a conserver.")
    return {
        "nom": _demander_texte("Nouveau nom : "),
        "genre": _demander_texte("Nouveau genre : "),
        "pays": _demander_texte("Nouveau pays : "),
    }


def recuperer_album() -> dict:
    print("\n=== AJOUT D'UN ALBUM ===")
    return {
        "titre": _demander_texte("Titre : "),
        "annee": _demander_texte("Annee : "),
        "streams": _demander_texte("Streams : "),
    }


def recuperer_mise_a_jour_album() -> dict:
    print("\n=== MODIFICATION D'UN ALBUM ===")
    print("Laissez vide un champ a conserver.")
    return {
        "titre": _demander_texte("Nouveau titre : "),
        "annee": _demander_texte("Nouvelle annee : "),
        "streams": _demander_texte("Nouveau nombre de streams : "),
    }


if __name__ == "__main__":
    print(recuperer_artiste())
