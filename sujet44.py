def renverse(mot):
  reverse = ""
  for i in range(len(mot),0,-1):
    print(i)
    reverse += mot[i-1]
  return reverse
print(renverse("informatique"))

def crible(n):
    """
    Renvoie un tableau contenant tous les nombres premiers plus petits
    que n
    """
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(0, n):
        if tab[i] == True:
            premiers.append(i)
            for multiple in range(2 * i, n, i):
                tab[multiple] = False
    return premiers


assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

