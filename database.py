import json
from pathlib import Path
from typing import Any

NOM_FICHIER = Path("donnees.json")


# =========================
# NORMALISATION
# =========================
def _normalize_data(data: Any) -> list[dict]:
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        return [data]
    return [{"valeur": data}]


# =========================
# CHARGER
# =========================
def charger(path: Path = NOM_FICHIER, verbose: bool = False) -> list[dict]:
    if not path.exists():
        return []

    contenu = path.read_text(encoding="utf-8").strip()

    if not contenu:
        return []

    try:
        return _normalize_data(json.loads(contenu))
    except json.JSONDecodeError:
        lignes = [l for l in contenu.splitlines() if l.strip()]
        return [{"valeur": l} for l in lignes]


# =========================
# SAUVEGARDE 
# =========================
def sauvegarder(
    data: list[dict] | dict,
    path: Path = NOM_FICHIER,
    verbose: bool = False
) -> None:
    """Ajoute toujours les données sans jamais écraser."""

    ancien = charger(path)

    if isinstance(data, dict):
        ancien.append(data)
    else:
        ancien.extend(_normalize_data(data))

    path.write_text(
        json.dumps(ancien, ensure_ascii=False, indent=4),
        encoding="utf-8"
    )

    if verbose:
        print(f"Données ajoutées dans '{path}'")
