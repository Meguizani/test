import modularite

modularite.parler("koffi","parle")
"""
def dire_bonjour():
    print("boonjour tous le monde !")
dire_bonjour()
def dire(nomPersonne, messagePersonne):
    print("{},{}".format(nomPersonne,messagePersonne))
dire("feli","tu es une star")
"""
## * signifie nombre indeterminer de parametre
def show_inventory(*list_items):
    for item in list_items:
        print(item)
show_inventory("epeee","arcs","potion de mana","capede dragon rouge")
show_inventory("fleche")

"""une fonction lambda est une fonction annonyme, elle ne dispose pas de nom
elle realise une seul fonction
"""
ttc= lambda prixHT:prixHT +(prixHT*20/100)
print(ttc(24))
calculer = lambda a,b: a+b
print(calculer(12,13))
