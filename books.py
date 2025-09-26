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
