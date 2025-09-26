import data as d

#Trier les livres par année de publication (sort))
books= list(d.livres)
def trier_livres():
     global books
     new_list =sorted(books, key=lambda x: x["année"])
     return new_list

def identifien_ancienne_recent():
     livre_trier= trier_livres()
     ancien_livre= livre_trier[0]
     livre_recent= livre_trier[-1]
     print (f" le plus ancien:  {ancien_livre} \n le plus récent: {livre_recent}")
users= d.utilisateurs
utilisateur_binome = ()
tous_utilisateurs_binom = ()
def affichage_d_etulisateur():
     i=0
     while i < len(users):
          tuple_1= (users[i])
          
          tuple_2= (users[i+1])         
          utilisateur_binome = (tuple_1,)+ (tuple_2,)
          print(utilisateur_binome)
          i=i+2
          if i % 2 == 2 :
             tous_utilisateurs_binom = (utilisateur_binome)
             print(tous_utilisateurs_binom)
             break
          
      

dictionair={}
aime_livres= list(d.aime_livres)

def afficher_un_dictionnair():
     dictionair = {}
     i=0
     count=0
     for l1 in aime_livres:
          for l2 in aime_livres:
               if l1[1] == l2[1]:
                    count= count+1
          dictionair[l1[1]] = count 
          count=0   
     print(dictionair)
afficher_un_dictionnair()