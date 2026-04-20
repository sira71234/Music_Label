import json
from pathlib import Path
from typing import Any

NOM_FICHIER = Path("donnees.json")


def _normalize_item(item: Any) -> dict:
    if isinstance(item, dict):
        return item
    return {"valeur": item}


def _normalize_data(data: Any) -> list[dict]:
    if isinstance(data, list):
        return [_normalize_item(item) for item in data]
    return [_normalize_item(data)]


def charger(path: Path = NOM_FICHIER, verbose: bool = False) -> list[dict]:
    path = Path(path)

    if not path.exists():
        return []

    try:
        contenu = path.read_text(encoding="utf-8").strip()
    except OSError:
        return []

    if not contenu:
        return []

    try:
        donnees = json.loads(contenu)
        resultat = _normalize_data(donnees)
    except json.JSONDecodeError:
        lignes = [ligne for ligne in contenu.splitlines() if ligne.strip()]
        resultat = [{"valeur": ligne} for ligne in lignes]

    if verbose:
        print(f"{len(resultat)} element(s) charge(s) depuis '{path}'.")

    return resultat


def sauvegarder(
    data: list[dict] | dict,
    path: Path = NOM_FICHIER,
    verbose: bool = False,
) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    donnees = _normalize_data(data)
    path.write_text(
        json.dumps(donnees, ensure_ascii=False, indent=4),
        encoding="utf-8",
    )

    if verbose:
        print(f"Donnees sauvegardees dans '{path}'.")
