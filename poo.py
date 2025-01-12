"""
classe       : plan de conception ,genre (ex: humain)
objet        : instance de classe (ex: julien)
attribut     : variable de classe(ex: nom, age,sexe,taille)
propriete    : maniere de manipuler  les attributs (lecture seul,aces non utiliser en dehors de la classe ,ectc...)
methode      : fonction d'une classe(ex: manger(nourriture, quitter))
methode de classse: fonction d'une classe
methode statique : fonction d'une classe mais independante de celle_ci
heritage          : une classe fille qui herite d'une classe mere
"""
class Humain :
    def __init__(self):
        print("creation d'un humain")
        self.prenom = "jaja"
        self.age = 12

h1 = Humain()        
print("prenom de h1 --> {}".format(h1.prenom))
h2 = Humain()
