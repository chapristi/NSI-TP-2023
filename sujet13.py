def recherche(a,tab):
    nb = 0
    for i in tab:
        if a == i:
            nb+=1
    return nb
print(recherche(5, [-2, 5, 3, 5, 4, 5]))


pieces = [1, 2, 5, 10, 20, 50, 100, 200]

def rendu_monnaie(somme_due, somme_versee):

    rendu = []
    a_rendre = somme_versee - somme_due
    i = len(pieces) - 1
    while a_rendre > 0 :
        if pieces[i] <= a_rendre :
            rendu.append(pieces[i])
            a_rendre = a_rendre -  pieces[i]
        else :
            i = i-1
    return rendu
print( rendu_monnaie(102, 500))
