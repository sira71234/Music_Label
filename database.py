import json
from pathlib import Path
from typing import Any

NOM_FICHIER = Path("donnees.json")


def _normalize_data(data: Any) -> list[dict]:
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        return [data]
    return [{"valeur": data}]


def charger(path: Path = NOM_FICHIER, verbose: bool = False) -> list[dict]:
    """Charge et normalise les données JSON du fichier.

    Si le fichier n'existe pas, retourne une liste vide.
    Si le fichier est vide, retourne une liste vide.
    Si le JSON contient un dict ou un autre type, il est converti en liste.
    Si le contenu n'est pas du JSON, il est converti en liste de lignes.
    """
    if not path.exists():
        return []

    contenu = path.read_text(encoding="utf-8").strip()
    if not contenu:
        if verbose:
            print("Fichier vide détecté. Démarrage avec une liste vide.")
        return []

    try:
        donnees = json.loads(contenu)
    except json.JSONDecodeError:
        if verbose:
            print("Contenu non-JSON détecté. Tentative de conversion en liste...")
        lignes = [ligne for ligne in contenu.splitlines() if ligne.strip()]
        donnees = [{"valeur": ligne} for ligne in lignes]
        if donnees:
            sauvegarder(donnees, path, verbose=verbose)
            if verbose:
                print(f"{len(donnees)} ligne(s) convertie(s) en JSON.")
        return donnees

    donnees_normalisees = _normalize_data(donnees)
    if donnees_normalisees is not donnees:
        if verbose:
            print("Conversion automatique du contenu en liste.")
        sauvegarder(donnees_normalisees, path, verbose=verbose)
    return donnees_normalisees


def sauvegarder(data: list[dict], path: Path = NOM_FICHIER, verbose: bool = False) -> None:
    """Sauvegarde la liste de dictionnaires dans le fichier JSON."""
    path.write_text(json.dumps(data, ensure_ascii=False, indent=4), encoding="utf-8")
    if verbose:
        print(f"Données sauvegardées dans '{path}'.")
