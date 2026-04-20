import logic
import saisir
import stats


def pause() -> None:
    input("Appuyez sur Entree pour continuer...")


def menu() -> None:
    print("\n________Sahel Sound Records________\n")
    print("1. Catalogue des artistes et albums")
    print("2. Gestionnaire d'artistes")
    print("3. Gestionnaire d'albums")
    print("4. Statistiques et rapport")
    print("5. Quitter l'application")


def menu_catalogue() -> None:
    while True:
        print("\n______Catalogue______")
        print("1. Afficher tous les artistes")
        print("2. Rechercher un artiste par nom ou par genre")
        print("3. Afficher les details d'un artiste")
        print("4. Retour au menu principal")
        sub_choice = input("Veuillez choisir une option (1-4): ").strip()

        match sub_choice:
            case "1":
                logic.afficher_tout()
                pause()
            case "2":
                menu_recherche()
            case "3":
                nom = input("Entrez le nom de l'artiste: ").strip()
                logic.afficher_details_artiste(nom)
                pause()
            case "4":
                break
            case _:
                print("Option invalide.")


def menu_recherche() -> None:
    while True:
        print("\n______Recherche______")
        print("1. Rechercher par nom")
        print("2. Rechercher par genre")
        print("3. Retour au menu precedent")
        search_choice = input("Veuillez choisir une option (1-3): ").strip()

        match search_choice:
            case "1":
                nom = input("Entrez le nom de l'artiste a rechercher: ").strip()
                logic.rechercher_par_nom(nom)
                pause()
            case "2":
                genre = input("Entrez le genre a rechercher: ").strip()
                logic.rechercher_par_genre(genre)
                pause()
            case "3":
                break
            case _:
                print("Option invalide.")


def menu_artistes() -> None:
    while True:
        print("\n______Gestionnaire d'artistes______")
        print("1. Ajouter un artiste")
        print("2. Modifier les details d'un artiste existant")
        print("3. Supprimer un artiste")
        print("4. Retour au menu principal")
        sub_choice = input("Veuillez choisir une option (1-4): ").strip()

        match sub_choice:
            case "1":
                artiste = saisir.recuperer_artiste()
                logic.ajouter_artiste(artiste)
                pause()
            case "2":
                nom = input("Nom de l'artiste a modifier: ").strip()
                nouvelles_donnees = saisir.recuperer_mise_a_jour_artiste()
                logic.modifier_artiste(nom, nouvelles_donnees)
                pause()
            case "3":
                nom = input("Entrez le nom de l'artiste a supprimer: ").strip()
                logic.supprimer_artiste(nom)
                pause()
            case "4":
                break
            case _:
                print("Option invalide.")


def menu_albums() -> None:
    while True:
        print("\n______Gestionnaire d'albums______")
        print("1. Ajouter un album a un artiste existant")
        print("2. Modifier les details d'un album existant")
        print("3. Supprimer un album")
        print("4. Retour au menu principal")
        sub_choice = input("Veuillez choisir une option (1-4): ").strip()

        match sub_choice:
            case "1":
                nom_artiste = input("Nom de l'artiste: ").strip()
                album = saisir.recuperer_album()
                logic.ajouter_album(nom_artiste, album)
                pause()
            case "2":
                nom_artiste = input("Nom de l'artiste: ").strip()
                titre_album = input("Titre de l'album a modifier: ").strip()
                nouvelles_donnees = saisir.recuperer_mise_a_jour_album()
                logic.modifier_album(nom_artiste, titre_album, nouvelles_donnees)
                pause()
            case "3":
                nom_artiste = input("Nom de l'artiste: ").strip()
                titre_album = input("Titre de l'album a supprimer: ").strip()
                logic.supprimer_album(nom_artiste, titre_album)
                pause()
            case "4":
                break
            case _:
                print("Option invalide.")


def menu_stats() -> None:
    while True:
        print("\n______Statistiques et rapport______")
        print("1. Consulter le top 5 des artistes les plus populaires")
        print("2. Consulter la moyenne des streams par genre musical")
        print("3. Consulter le nombre total d'albums sortis par annee")
        print("4. Rapport complet")
        print("5. Retour au menu principal")
        sub_choice = input("Veuillez choisir une option (1-5): ").strip()

        match sub_choice:
            case "1":
                df = stats.creer_dataframe_albums()
                stats.top5_artistes(df)
                pause()
            case "2":
                df = stats.creer_dataframe_albums()
                stats.moyenne_streams_par_genre(df)
                pause()
            case "3":
                df = stats.creer_dataframe_albums()
                stats.albums_par_annee(df)
                pause()
            case "4":
                stats.generer_rapport_complet()
                pause()
            case "5":
                break
            case _:
                print("Option invalide.")


def main() -> None:
    while True:
        menu()
        choice = input("Veuillez choisir une option (1-5): ").strip()

        match choice:
            case "1":
                menu_catalogue()
            case "2":
                menu_artistes()
            case "3":
                menu_albums()
            case "4":
                menu_stats()
            case "5":
                print("Merci d'avoir utilise l'application. Au revoir!")
                break
            case _:
                print("Option invalide.")


if __name__ == "__main__":
    main()
