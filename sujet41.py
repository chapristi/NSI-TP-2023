def recherche(lettre,mot):
  count = 0
  for i in mot:
    if lettre == i:
      count += 1
  return count
print(recherche('e', "sciences"))
print( recherche('i', "mississippi"))
valeurs = [100,50,20,10,5,2,1]

def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return []
    v = valeurs[rang]
    if v <=  a_rendre:
        return [v]+ rendu_glouton(a_rendre - v, rang)
    else :
        return rendu_glouton(a_rendre, rang+1)
print(rendu_glouton(67, 0))
