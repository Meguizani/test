"""
module pour un joueur
un module est un fichier qui contient plusieurs fonctions 
"""
def parler(personnage ,message):
    print("{},{}".format(personnage, message))

def au_revoir():
    print("bye!")
## pour verifier que tous fonctionne bien
if __name__ == "__fonction__":
    parler("latifa","my best")
    au_revoir()

