def verifie(tab):
  k  = tab[0]
  for i in tab:
    if i < k:
      return False
    k = i
  return True
print(verifie([0, 5, 8, 8, 9]))    

urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']

def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat
election  = depouille(urne)

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if  election[candidat] > nmax :
            nmax = election[candidat] 
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale
print(election)
print(vainqueur(election=election))
 
