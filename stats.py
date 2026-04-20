import database

try:
    import pandas as pd
except ImportError:
    pd = None


def _pandas_disponible() -> bool:
    if pd is None:
        print("Pandas n'est pas installe. Les statistiques sont indisponibles.")
        return False
    return True


def test_pandas():
    if not _pandas_disponible():
        return None

    donnees = database.charger()

    if not donnees:
        print("La liste est vide, rien a afficher.")
        return None

    df = pd.DataFrame(donnees)
    print("Pandas fonctionne. Voici un apercu :\n")
    print(df.head())
    return df


def aplatir_albums() -> list[dict]:
    catalogue = database.charger()
    lignes = []

    for artiste in catalogue:
        albums = artiste.get("albums", [])
        if not isinstance(albums, list):
            continue

        for album in albums:
            if not isinstance(album, dict):
                continue

            lignes.append(
                {
                    "id": artiste.get("id"),
                    "nom": artiste.get("nom"),
                    "genre": artiste.get("genre"),
                    "pays": artiste.get("pays"),
                    "titre": album.get("titre"),
                    "annee": album.get("annee"),
                    "streams": album.get("streams", 0),
                }
            )

    return lignes


def creer_dataframe_albums():
    if not _pandas_disponible():
        return None

    lignes = aplatir_albums()
    if not lignes:
        print("Aucune donnee d'album disponible.")
        return None

    return pd.DataFrame(lignes)


def top5_artistes(df):
    if df is None or df.empty:
        print("Aucune statistique disponible pour le top 5.")
        return None

    print("\nTOP 5 ARTISTES PAR STREAMS :")
    print("-" * 40)
    top5 = (
        df.groupby("nom")["streams"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )
    top5.columns = ["Artiste", "Total Streams"]
    print(top5.to_string(index=False))
    return top5


def moyenne_streams_par_genre(df):
    if df is None or df.empty:
        print("Aucune statistique disponible pour les genres.")
        return None

    print("\nMOYENNE DES STREAMS PAR GENRE :")
    print("-" * 40)
    moyenne = (
        df.groupby("genre")["streams"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )
    moyenne.columns = ["Genre", "Moyenne Streams"]
    moyenne["Moyenne Streams"] = moyenne["Moyenne Streams"].round(0)
    print(moyenne.to_string(index=False))
    return moyenne


def albums_par_annee(df):
    if df is None or df.empty:
        print("Aucune statistique disponible par annee.")
        return None

    print("\nNOMBRE D'ALBUMS PAR ANNEE :")
    print("-" * 40)
    par_annee = df.groupby("annee")["titre"].count().reset_index()
    par_annee.columns = ["Annee", "Nombre d'albums"]
    print(par_annee.to_string(index=False))
    return par_annee


def exporter_rapport(df, chemin: str = "rapport.csv") -> bool:
    if df is None or df.empty:
        print("Aucun rapport a exporter.")
        return False

    df.to_csv(chemin, index=False, encoding="utf-8-sig")
    print(f"\nRapport exporte dans '{chemin}' avec succes.")
    return True


def generer_rapport_complet():
    if not _pandas_disponible():
        return None

    print("GENERATION DU RAPPORT COMPLET...")
    print("=" * 40)

    df = creer_dataframe_albums()
    if df is None:
        return None

    top5_artistes(df)
    moyenne_streams_par_genre(df)
    albums_par_annee(df)
    exporter_rapport(df)

    return df


if __name__ == "__main__":
    test_pandas()
    generer_rapport_complet()
