# database.py — Module de Persistance des Donnees

**Auteur :** Personne 2  
**Fichier produit :** `donnees.json`  
**Role :** Gere la totalite des operations de lecture et d'ecriture sur le disque dur. Aucun autre fichier du projet ne doit acceder directement a `donnees.json`.

---

## Sommaire

1. [Integration rapide](#1-integration-rapide)
2. [Fonctions disponibles](#2-fonctions-disponibles)
3. [Guide par membre de l'equipe](#3-guide-par-membre-de-lequipe)
4. [Gestion des erreurs](#4-gestion-des-erreurs)
5. [Regles a respecter](#5-regles-a-respecter)

---

## 1. Integration rapide

Ajouter cette ligne en haut de votre fichier :

```python
import database
```

Deux fonctions sont alors disponibles : `database.charger()` et `database.sauvegarder()`.

---

## 2. Fonctions disponibles

### charger()

Lit le fichier `donnees.json` et retourne son contenu sous forme de liste.
Cette fonction ne leve jamais d'exception — elle retourne toujours une liste, meme vide.

**Signature :**

```python
database.charger(path=NOM_FICHIER, verbose=False) -> list[dict]
```

**Parametres :**

| Parametre | Type   | Valeur par defaut | Description                                  |
|-----------|--------|-------------------|----------------------------------------------|
| `path`    | `Path` | `donnees.json`    | Chemin du fichier a lire                     |
| `verbose` | `bool` | `False`           | Affiche les messages de diagnostic si `True` |

**Exemple d'utilisation :**

```python
inventaire = database.charger()
# Retourne la liste sauvegardee, ou [] si aucune donnee n'existe encore

inventaire = database.charger(verbose=True)
# Meme comportement, avec messages de diagnostic dans la console
```

---

### sauvegarder()

Ecrit la liste fournie dans `donnees.json`. Cree le fichier s'il n'existe pas encore.
Ecrase systematiquement le contenu precedent — seule la version la plus recente est conservee.

**Signature :**

```python
database.sauvegarder(data, path=NOM_FICHIER, verbose=False) -> None
```

**Parametres :**

| Parametre | Type         | Valeur par defaut | Description                              |
|-----------|--------------|-------------------|------------------------------------------|
| `data`    | `list[dict]` | *(obligatoire)*   | La liste de dictionnaires a sauvegarder  |
| `path`    | `Path`       | `donnees.json`    | Chemin du fichier a ecrire               |
| `verbose` | `bool`       | `False`           | Affiche un message de confirmation si `True` |

**Exemple d'utilisation :**

```python
database.sauvegarder(inventaire)
# Le fichier donnees.json est mis a jour immediatement

database.sauvegarder(inventaire, verbose=True)
# Affiche : Donnees sauvegardees dans 'donnees.json'.
```

---

## 3. Guide par membre de l'equipe

### Personne 1 — main.py

Charger les donnees au demarrage du programme et sauvegarder apres chaque action utilisateur.

```python
import database

# Demarrage du programme
inventaire = database.charger()

# Apres chaque action dans la boucle du menu
database.sauvegarder(inventaire)
```

---

### Personne 4 — logic.py

Initialiser la liste depuis le fichier au demarrage et sauvegarder apres chaque modification.
Le nom de la variable locale importe peu — Python fait la correspondance automatiquement.

```python
import database

inventaire = database.charger()

def ajouter(dictionnaire):
    inventaire.append(dictionnaire)
    database.sauvegarder(inventaire)
```

---

### Personne 5 — stats.py

Recuperer la liste avec `charger()` et la passer directement a Pandas.

```python
import database
import pandas as pd

def test_pandas():
    donnees = database.charger()
    df = pd.DataFrame(donnees)
    print(df.head())
```

---

## 4. Gestion des erreurs

La fonction `charger()` gere automatiquement les situations suivantes sans lever d'exception :

| Situation                               | Comportement                                              |
|-----------------------------------------|-----------------------------------------------------------|
| Fichier `donnees.json` absent           | Retourne `[]`                                             |
| Fichier vide                            | Retourne `[]`                                             |
| Contenu non JSON (texte brut, etc.)     | Convertit chaque ligne en dictionnaire et retourne la liste |
| Contenu JSON valide mais type incorrect | Normalise automatiquement vers une liste                  |

---

## 5. Regles a respecter

Ne jamais lire ou ecrire `donnees.json` directement depuis un autre fichier du projet.
Toute interaction avec les donnees persistantes doit passer exclusivement par ce module.

Incorrect :

```python
with open("donnees.json", "r") as f:
    data = json.load(f)
```

Correct :

```python
data = database.charger()
```

---

*Pour toute question relative a ce module, contacter la Personne 2.*
