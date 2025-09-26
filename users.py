from data import utilisateurs, livres, aime_livres


#1- filter les utilisateurs :
def get_majeurs():
    return list(filter(lambda u:u[3] >= 18, utilisateurs))

#2- formater les noms en mjs : 
def mjsc(users):
    return list(map(lambda u: f"{u[1].upper()} {u[2].upper()}", utilisateurs))

#3- creer un dictionnaire :

def livres_utilisateur(user_id):
    return [titre for (uid, titre) in aime_livres if uid == user_id]


def resume(users):
    resumes = []
    for u in users:
        id_user, prenom, nom, age = u
        livres = livres_utilisateur(id_user)
        livres_str = ", ".join([f"'{titre}'" for titre in livres])
        resumes.append(f"{prenom.upper()} {nom.upper()} ({age} ans) aime : {livres_str}")
    return resumes
