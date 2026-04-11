# stats.py — Personne 5 : Analyste & Qualité
import pandas as pd


def test_pandas(liste):
    """
    Teste que Pandas peut lire une liste de dictionnaires.
    Paramètre : liste — une liste de dictionnaires (ex: artistes)
    Retourne  : le DataFrame créé
    """
    if not liste:
        print("⚠️  La liste est vide, rien à afficher.")
        return None

    df = pd.DataFrame(liste)
    print("✅ Pandas fonctionne ! Voici un aperçu des données :\n")
    print(df.head())
    return df


# --- Test rapide pour vérifier que ça marche ---
if __name__ == "__main__":
    liste_test = [
        {"nom": "Fally Ipupa", "genre": "Afrobeat", "pays": "RDC"},
        {"nom": "Aya Nakamura", "genre": "Afropop", "pays": "Mali"},
        {"nom": "Burna Boy",   "genre": "Afrobeat", "pays": "Nigeria"},
    ]
    test_pandas(liste_test)