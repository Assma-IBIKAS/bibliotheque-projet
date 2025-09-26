import data as d
#Trier les livres par année de publication (sort))
books= list(d.livres)
new_list =sorted(books, key=lambda x: x["année"])
print(new_list)