def recuperer_info():
    print("\n=== AJOUT D'UN ELEMENT ===")
    
    nom = input("Nom : ")
    genre = input("Genre : ")
    annee = input("Année : ")

    info = {
        "nom": nom,
        "genre": genre,
        "annee": annee
    }
    return info


if __name__ == "__main__":
    resultat = recuperer_info()
    print(resultat)