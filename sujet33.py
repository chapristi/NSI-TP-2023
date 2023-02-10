a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \
 'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], \
 'H':['','']}
def taille(arbre,lettre):
  if lettre == "":
    return 0
  else:
    return 1+taille(arbre,arbre[lettre][0])+taille(arbre,arbre[lettre][1])
print(taille(a, 'F'))

def tri_selection(tab):
    N = len(tab)
    for k in range(N - 1):
        imin = k
        for i in range(k , N):
            if tab[i] < tab[imin] :
                imin = i
        tab[k] , tab[imin] = tab[imin] , tab[k]
liste = [41, 55, 21, 18, 12, 6, 25]
tri_selection(liste)
print(liste)
