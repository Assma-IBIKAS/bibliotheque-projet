from users import get_majeurs, mjsc,resume

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