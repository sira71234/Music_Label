# stats.py — Personne 5 : Analyste & Qualité
import pandas as pd
import json


def charger_json(chemin="catalogue.json"):
    """
    Charge le fichier JSON et retourne la liste des artistes.
    """
    with open(chemin, encoding="utf-8") as f:
        return json.load(f)


def aplatir_albums(catalogue):
    """
    Transforme la liste des artistes en une liste de lignes
    une ligne par album avec les infos de l'artiste.
    """
    lignes = []
    for artiste in catalogue:
        for album in artiste["albums"]:
            lignes.append({
                "id":      artiste["id"],
                "nom":     artiste["nom"],
                "genre":   artiste["genre"],
                "pays":    artiste["pays"],
                "titre":   album["titre"],
                "annee":   album["annee"],
                "streams": album["streams"]
            })
    return lignes


def top5_artistes(df):
    """
    Retourne le top 5 des artistes par nombre total de streams.
    """
    print("\n🏆 TOP 5 ARTISTES PAR STREAMS :")
    print("─" * 40)
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
    """
    Retourne la moyenne des streams par genre musical.
    """
    print("\n🎵 MOYENNE DES STREAMS PAR GENRE :")
    print("─" * 40)
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
    """
    Retourne le nombre d'albums sortis par année.
    """
    print("\n📅 NOMBRE D'ALBUMS PAR ANNÉE :")
    print("─" * 40)
    par_annee = (
        df.groupby("annee")["titre"]
        .count()
        .reset_index()
    )
    par_annee.columns = ["Année", "Nombre d'albums"]
    print(par_annee.to_string(index=False))
    return par_annee


def exporter_rapport(df, chemin="rapport.csv"):
    """
    Exporte le DataFrame complet dans un fichier CSV.
    """
    df.to_csv(chemin, index=False, encoding="utf-8-sig")
    print(f"\n✅ Rapport exporté dans '{chemin}' avec succès !")


def generer_rapport_complet():
    """
    Fonction principale qui génère toutes les statistiques.
    """
    print("📊 GÉNÉRATION DU RAPPORT COMPLET...")
    print("═" * 40)

    # Chargement des données
    catalogue = charger_json()
    lignes = aplatir_albums(catalogue)
    df = pd.DataFrame(lignes)

    # Statistiques
    top5_artistes(df)
    moyenne_streams_par_genre(df)
    albums_par_annee(df)

    # Export CSV
    exporter_rapport(df)

    return df


# --- Test ---
if __name__ == "__main__":
    generer_rapport_complet()