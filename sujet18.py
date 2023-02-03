def max_et_indice(tab):
    index,max = 0,tab[0]
    for key,value in enumerate(tab):
        if value > max:
            max = value
            index = key
    return(max,index)
print(
    max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8])
)

def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les entiers
    de 1 Ã   n, False sinon
    '''
    for i in range(1,len(tab)):
        if 1+tab[i] != tab[i+i]:
            return False
    return True
print( est_un_ordre([1, 6, 2, 8, 3, 7]))
print( est_un_ordre([5, 4, 3, 6, 7, 2, 1, 8, 9]))

def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de point de rupture de ordre qui reprÃ©sente un ordre
    de gÃ¨nes de chromosome
    '''
    assert ... # ordre n'est pas un ordre de gÃƒÂ¨nes
    n = len(ordre)
    nb = 0
    if ordre[...] != 1: # le premier n'est pas 1
        nb = nb + 1
    i = 0
    while i < ...:
        if ... not in [-1, 1]: # l'ÃƒÂ©cart n'est pas 1
            nb = nb + 1
        i = i + 1
    if ordre[...] != n: # le dernier n'est pas n
        nb = nb + 1
    return nb
