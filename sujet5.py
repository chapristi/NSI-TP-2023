from random import randint
def lancer(n):
    t = list()
    for _ in range(0,n):
        t.append(randint(1,7))
    return t
lancer = lancer(5)
def paire_6(tab):
    n = 0
    for i in tab:
        if i == 6:
            n+=1
    return n>=2

print(
    paire_6(lancer)
)

img=[[20, 34, 254, 145, 6], [23, 124, 237, 225, 69], [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]

def nbLig(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image)
print("nblig",nbLig(img))

def nbCol(image):
    '''renvoie la largeur de l'image'''
    return len(img)+1
print("ncol",nbCol(img))

def negatif(image):
    '''renvoie le negatif de l'image sous la forme
       d'une liste de listes'''

    # on cree une image de 0 aux memes dimensions que le parametre image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]
    print(L)
    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            L[i][j] = 
    return L

def binaire(image, seuil):
    '''renvoie une image binarisee de l'image sous la forme
       d'une liste de listes contenant des 0 si la valeur
       du pixel est strictement inferieure au seuil
       et 1 sinon'''

    # on cree une image de 0 aux memes dimensions que le parametre image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]

    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            if image[i][j] < seuil :
                L[i][j] = 0
            else:
                L[i][j] = 1
    return L
print(
    "negatif",negatif(img)
)
print("binaire", binaire(img,120))
