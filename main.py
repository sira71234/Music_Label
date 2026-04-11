print("\n________Sahel Sound Records________\n")
def menu():
    print("1. Consulter le catalogue")
    print("2. Ajouter un artiste")
    print("3. Ajouter un album a un artiste existant")
    print("4. Statistiques et rapport")
    print("5. Quitter l'application")

def main():
    while True:
        menu()
        choice = input("Veuillez choisir une option (1-5): ").strip()

        match choice:
            case '1':
                while True:
                    print("______Consulter le catalogue______")
                    print("1. Afficher tous les artistes")
                    print("2. Rechercher un artiste par nom et par genre")
                    print("3.Afficherles details d'un artiste")
                    print("4. Retour au menu principal")
                    sub_choice = input("Veuillez choisir une option (1-4): ").strip()
                    match sub_choice:
                        case '1':
                            print("Affichage de tous les artistes...")

                        case '2':
                            print("Recherche d'un artiste par nom et par genre...")

                        case '3':
                            print("Affichage des details d'un artiste...")

                        case '4':
                            break

                        case _:
                            print("Option invalide")


            case '2':
                print("______Ajouter un artiste______")
                while True:
                    print("1. Ajouter un artiste")
                    print("2. Retour au menu principal")
                    sub_choice = input("Veuillez choisir une option (1-2): ").strip()
                    match sub_choice:
                        case '1':
                            print("______Ajout d'un artiste...______")
                        case '2':
                            break
                        case _:
                            print("Option invalide")

            case '3':
                print("______Ajouter un album a un artiste existant______")
                while True:
                    print("1. Ajouter un album a un artiste existant")
                    print("2. Retour au menu principal")
                    sub_choice = input("Veuillez choisir une option (1-2): ").strip()
                    match sub_choice: 
                        case '1':
                            print("______Ajout d'un album a un artiste existant...______")
                        case '2':
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
                        case '2':
                            print("______Consulter la moyenne des streams par genre musical...______")
                        case '3':
                            print("______Consulter le nombre total d'albums sortis par année...______")
                        case '4':
                            print("______Rapport complet...______")
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