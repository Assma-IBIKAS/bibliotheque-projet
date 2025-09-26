from data import utilisateurs, livres, aime_livres


#1- filter les utilisateurs :
def get_majeurs():
    return list(filter(lambda u:u[3] >= 18, utilisateurs))

#2- formater les noms en mjs : 
def mjsc():
    return list(map(lambda u: f"{u[1].upper()} {u[2].upper()}", utilisateurs))