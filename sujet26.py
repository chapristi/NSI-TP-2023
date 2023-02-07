
def multiplication(n1,n2):
  if n2 == 0 or n1 == 0:
    return 0
  elif n1 < 0 and n2 < 0:
    #surement mieux à faire ;)
    n1 -= n1 + n1
    n2 -= n2 + n2
    return n1  + multiplication(n1,n2-1)
  else:
    return n1  + multiplication(n1,n2-1)
print(multiplication(3, 5))
print( multiplication(-4, -8))
def dichotomie(tab, x):
    """
    tab : tableau dâ€™entiers triÃ© dans lâ€™ordre croissant
    x   : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
             fin = m - 1 
    return False
print( dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27))
