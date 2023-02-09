class Arbre:
   def __init__(self, etiquette):
     self.v = etiquette
     self.fg = None
     self.fd = None
a=Arbre(1)
a.fg=Arbre(4)
a.fd=Arbre(0)
a.fd.fd=Arbre(7)
def taille(abr : Arbre):
  if abr == None:
    return 0
  else:
    return 1 + taille(abr.fg) + taille(abr.fd)
print(taille(a))
def hauteur(abr : Arbre):
  if abr == None:
    return 0
  else:
    return 1 + max(hauteur(abr.fg) ,hauteur(abr.fd))
print(hauteur(a))


def ajoute(indice, element, liste):
    nbre_elts = len(liste)
    L = [0 for i in range(nbre_elts + 1)]
    if indice < len(liste):
        for i in range(indice):
            L[i] = liste[i]
        L[indice] = element
        for i in range(indice + 1, nbre_elts + 1):
            L[i] = liste[i-1]
    else:
        for i in range(nbre_elts):
            L[i] = liste[i]
        L[nbre_elts] = element
    return L
print(ajoute(1, 4, [7, 8, 9]))
