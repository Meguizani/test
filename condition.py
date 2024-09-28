"""
les operateur  de comparaison : ==(egal a)
                                != different de 
                                >
                                <
                                <=
                                >=
    les conditions multiples :  and 
                                or
                                in / not in (dans /pas dans) 

"""
lettre_hasard = "r"
if lettre_hasard not in "aeyuio":
    print("c'est une consomme")
else:
    print("c'est une voyellle")
age = input("entrez votre age : ")
age = int(age)
if 0<age and age<=100:
    print("l'age est valide")
else:
    print("l'age invalide ")