from users import get_majeurs, mjsc,resume
from books import affichage_d_etulisateur,trier_livres, afficher_un_dictionnair, identifien_ancienne_recent
if __name__ == "__main__":

    majeurs = get_majeurs()
    print("Utilisateurs majeurs : ",majeurs)

    # Afficher les noms formatés en majuscules
    print("Noms en majuscules :")
    print(mjsc(majeurs))
    print()

    # afficher les résumés
    print("Résumé par utilisateur :")
    for r in resume(majeurs):
        print(r)
while True:
    choice= input("choose an operation \n 1.affichage des utilisateur \n 2.afficher les j'aime de chaque livre \n 3. afficher les livres\n 4.Livres le plus ancien et le plus récent \n 5.Filtrer les utilisateurs majeurs \n 6.Noms en majuscules \n 7. \n 8. \n 9.quitter ")
    match choice :
          case "1":
              print(affichage_d_etulisateur())
              continue
          case "2":
              print(afficher_un_dictionnair())
              continue
          case "3":
              print(trier_livres())
              continue
          case "4":
              print( identifien_ancienne_recent())
              continue
          case "5":
                majeurs = get_majeurs()
                print("Utilisateurs majeurs : ",majeurs)
                continue
          case "6":
                 print("Noms en majuscules :")
                 print(mjsc(majeurs))
                 print()
                 continue
          case "9":
            break
          case _:
            continue

