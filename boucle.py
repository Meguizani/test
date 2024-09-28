jeu_lancer =True
print("")
"""
boucles : for / while
mots_cles : break (casse la boucle)/ continue (revient au debut de la boucle)

while jeu_lancer:
    choix_menu=input("> ")
    if choix_menu=="again":
        continue
    elif choix_menu == "quit":
        break
    elif choix_menu=="hello":
        print("bonjour: ")
    else:
        print("commande introuvable")

"""
sentence = "hello world"
for letter in sentence:
    print(letter)
