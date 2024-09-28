#coding:utf-8
  
""" 
les types standards :
        entier numerique
        nombre flottant 
        chaine de caractere 
        booleen
les fonction vue
        print()--> afficher le texte sur l'ecran
        input()--> lire le clavier
        type()--> retourne le type d'une donnee , variable
        int() float() bool() --> caster une donnee la convertir
        str.float()--> formater une chaine 

"""

agePersonne = 14
lePrixHT=5
continuePartie = True
nomJoueur= input(" entrez le nom du joueur: ")
print(type(agePersonne))
texte = "l'age de la personne est : {} et le prix hors taxe est : {} euro"
print(texte.format(agePersonne,lePrixHT))
print("bienvenue ",nomJoueur)