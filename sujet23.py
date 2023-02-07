animaux = [ {'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2},
 {'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},
 {'nom':'Tom', 'espece':'chat', 'age':7, 'enclos':4},
 {'nom':'Belle', 'espece':'chien', 'age':6, 'enclos':3},
 {'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]
def selection_enclos(table,num_enclos):  
  t = []
  for i in table:
    if i["enclos"] == num_enclos:
      t.append(i)
  return t

print(selection_enclos(animaux, 5))
print(selection_enclos(animaux, 2)
)
print( selection_enclos(animaux, 7)
)
tab_a = [3, 3, 3, 9, 9, 9, 1, 1, 1, 7, 2, 2, 2, 4, 4, 4, 8, 8, 8, 5, 5, 5]

tab_b = [8, 5, 5, 5, 9, 9, 9, 18, 18, 18, 3, 3, 3]

tab_c = [5, 5, 5, 1, 1, 1, 0, 0, 0, 6, 6, 6, 3, 8, 8, 8]

def trouver_intrus(tab, g, d):
    '''
    Renvoie la valeur de l'intrus situe entre les indices g et d
    dans la liste tab ou :
        tab verifie les conditions de l'exercice,
        g et d sont des multiples de 3.
    '''
    if g == d:
        return tab[g]

    else:
        nombre_de_triplets = (d - g)// 3
        indice = g + 3 * (nombre_de_triplets // 2)
        if tab[indice + 1] == tab[indice] :
            return trouver_intrus(tab,indice+3,d)
        else:
            return trouver_intrus(tab,g,indice)
print(trouver_intrus([3, 3, 3, 9, 9, 9, 1, 1, 1, 7, 2, 2, 2, 4, 
4, 4, 8, 8, 8, 5, 5, 5], 0, 21))
