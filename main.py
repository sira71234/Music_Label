import logic
import stats

def menu():
    print("\n________Sahel Sound Records________\n")
    print("1. Catalogue des artistes et albums")
    print("2. Gestionnaire d'artistes")
    print("3. Gestionnaire d'albums")
    print("4. Statistiques et rapport")
    print("5. Quitter l'application")

def main():
    while True:
        menu()
        choice = input("Veuillez choisir une option (1-5): ").strip()

        match choice:
            case '1':
                while True:
                    print("______Catalogue______")
                    print("1. Afficher tous les artistes")
                    print("2. Rechercher un artiste par nom et par genre")
                    print("3.Afficher les details d'un artiste")
                    print("4. Retour au menu principal")
                    sub_choice = input("Veuillez choisir une option (1-4): ").strip()
                    match sub_choice:
                        case '1':
                            print("______Affichage de tous les artistes______")
                            logic.afficher_tout()
                            input("Appuyez sur Entrée pour continuer...")

                        case '2':
                            while True:
                                print("______Recherche d'un artiste par nom et par genre...______")
                                print("1. Rechercher par nom")
                                print("2. Rechercher par genre")
                                print("3. Retour au menu precedent")
                                search_choice = input("Veuillez choisir une option (1-3): ").strip()
                                match search_choice:
                                    case '1':
                                        print("______Recherche par nom...______")
                                        logic.rechercher(input("Entrez le nom de l'artiste à rechercher: "))
                                        input("Appuyez sur Entrée pour continuer...")
                                    case '2':
                                        print("______Recherche par genre...______")
                                        input("Appuyez sur Entrée pour continuer...")
                                    case '3':
                                        break
                                    case _:
                                        print("Option invalide")

                        case '3':
                            print("______Affichage des details d'un artiste...______")
                            input("Appuyez sur Entrée pour continuer...")

                        case '4':
                            break

                        case _:
                            print("Option invalide")


            case '2':
                print("______Gestionnaire d'artistes______")
                while True:
                    print("1. Ajouter un artiste")
                    print("2. Modifier les details d'un artiste existant")
                    print("3. Supprimer un artiste")
                    print("4. Retour au menu principal")
                    sub_choice = input("Veuillez choisir une option (1-4): ").strip()
                    match sub_choice:
                        case '1':
                            print("______Ajout d'un artiste...______")
                            input("Appuyez sur Entrée pour continuer...")
                        case '2':
                            print("______Modification des details d'un artiste...______")
                            input("Appuyez sur Entrée pour continuer...")
                        case '3':
                            print("______Suppression d'un artiste...______")
                            logic.supprimer(input("Entrez le nom de l'artiste à supprimer: "))
                            input("Appuyez sur Entrée pour continuer...")
                        case '4':
                            break
                        case _:
                            print("Option invalide")

            case '3':
                print("______Gestionnaire d'albums______")
                while True:
                    print("1. Ajouter un album a un artiste existant")
                    print("2. Modifier les details d'un album existant")
                    print("3. Supprimer un album")
                    print("4. Retour au menu principal")
                    sub_choice = input("Veuillez choisir une option (1-4): ").strip()
                    match sub_choice: 
                        case '1':
                            print("______Ajout d'un album a un artiste existant...______")
                            input("Appuyez sur Entrée pour continuer...")
                        case '2':
                            print("______Modification des details d'un album...______")
                            input("Appuyez sur Entrée pour continuer...")
                        case '3':
                            print("______Suppression d'un album...______")
                            input("Appuyez sur Entrée pour continuer...")
                        case '4':
                            break
                        case _:
                            print("Option invalide")

            case '4':
                while True:
                    print("______Statistiques et rapport______")
                    print("1. Consulter le top 5 des artistes les plus populaires")
                    print("2.Consulter la moyenne des streams par genre musical")
                    print("3. Consulter le nombre total d'albums sortis par année")
                    print("4. Rapport complet")
                    print("5. Retour au menu principal")
                    sub_choice = input("Veuillez choisir une    option (1-5): ").strip()
                    match sub_choice:
                        case '1':
                            print("______Consulter le top 5 des artistes les plus populaires...______")
                            df = stats.pd.DataFrame(stats.aplatir_albums())
                            stats.top5_artistes(df)
                            input("Appuyez sur Entrée pour continuer...")
                        case '2':
                            print("______Consulter la moyenne des streams par genre musical...______")
                            starts = stats.pd.DataFrame(stats.aplatir_albums())
                            stats.moyenne_streams_par_genre(starts)
                            input("Appuyez sur Entrée pour continuer...")
                        case '3':
                            print("______Consulter le nombre total d'albums sortis par année...______")
                            starts = stats.pd.DataFrame(stats.aplatir_albums())
                            stats.albums_par_annee(starts)
                            input("Appuyez sur Entrée pour continuer...")
                        case '4':
                            print("______Rapport complet...______")
                            stats.generer_rapport_complet()
                            input("Appuyez sur Entrée pour continuer...")
                        case '5':
                            break
                        case _:
                            print("Option invalide")

            case '5':
                    print("Merci d'avoir utilisé l'application. Au revoir!")
                    break
            case _: 
                    print("Option invalide")

print(main())