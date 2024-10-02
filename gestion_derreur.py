"""age_utilisateur =input("quel age as tu? ")
try:

    age_utilisateur=int(age_utilisateur)
    
except:
    print("l'age est incorrecte !")
else:
    print("tu as ",age_utilisateur,"ans")
finally:
    print("fin du programme")
"""
"""nombre1 =150
nombre2= input("choisir le nombre pour diviser : ")
try:

    nombre2 = int(nombre2)
    print("resultat = {}".format(nombre1/nombre2))
except ZeroDivisionError:
    print("vous essayer de diviser par zero")
except ValueError:
    print("vous devez entrez un nombre")
except:
    print("valeur incorrecte.")


"""
try:
    age = input("quel age as tu? : ")
    age = int(age)
    if age <30 :
        raise ZeroDivisionError("on a lever une exception")
except:
    print(" votre  exeception est capturer")

  


