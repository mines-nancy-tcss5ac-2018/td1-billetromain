def somme_digit(n) :
    a = str(n)
    somme = 0
    for i in range(len(a)):
        somme = somme + int(a[i])
    return somme

assert somme_digit(2**10) == 7
print(somme_digit(2**1000))

def rang_alphabet(lettre) :
    return ord(lettre) - 64     #Calcul du rang de la lettre avec la fonction ord(lettre)
    
def valeur_nom() :
    valeur = 0
    f = open('Names.txt','r')
    chaine = f.read()
    a = chaine.split(',')       #Création d'une liste contenant tous les noms
    ttri = sorted(a, key = str.lower)   #Tri de cette liste
    for i in range(len(ttri)) : 
        for j in range(1,len(ttri[i])-1) :
                       valeur = valeur + rang_alphabet(ttri[i][j]) * (i+1)
    return valeur

print(valeur_nom())

def palindrome(n):                  #Fonction qui teste si n est un palindrome, renvoie TRUE si oui, sinon False
    a = str(n)
    for i in range((len(a)//2)) :
        if a[i] != a[-i - 1] :
            return False
    return True

def inv(n) :                     #Fonction qui renvoie le nombre lu de droite à gauche 123===>321
    a = str(n)
    s = 0
    for i in range(len(a)):
        s = s + (10**i)*int(a[i])
    return s


    

def Lychrel(n) :        
    c = n                           #Initialisation du compteur à n, on retirera 1 à chaque fois que l'on rencontrera un nombre qui n'est pas de Lychrel (i.e qui se transforme en palindrome)
    for i in range(0,n) :           #Première boucle qui va parcourir n nombre et modifier le compteur pour chaque i n'étant pas un nombre de Lychrel
        s = i
        for j in range(1,51) :      #50 itérations test pour i
            s = s + inv(s)
            if palindrome(s) :      #Si s est un palindrome, alors on enlève 1 au compteur car i n'est pas un nombre de Lychrel, puis on sort de la boucle avec break pour incrémenter i
                c = c - 1
                break
    return c

print(Lychrel(10000))

             
            
            
            