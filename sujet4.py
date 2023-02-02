def a_doublon(tab):
    tab2 = []
    for i in tab:
        for j in tab2:
            if i==j:
                return True
        tab2.append(i)
    return False
print(a_doublon([1, 2, 4, 6, 6]))



bombes = [(1, 1), (2, 4), (3, 1), (3, 3), (4, 4)]
grille_test = [[1, 1, 1, 0, 0], [1, -1, 1, 1, 1], [2, 2, 3, 2, -1], [1, -1, 2, -1, 3], [1, 1, 2, 2, -1]]

def voisinage(n, ligne, colonne):
    """ Renvoie la liste des coordonnÃ©es des voisins de la case
        (ligne, colonne) en gÃ¨rant les cases sur les bords. """
    voisins = []
    for l in range(max(0,ligne-1), min(n, ligne+2)):
        for c in range(max(0, colonne-1), min(n, colonne+2)):
            if (l, c) != (ligne, colonne):
                voisins.append((l,c))
    return voisins

def incremente_voisins(grille, ligne, colonne):
    """ IncrÃ©mente de 1 toutes les cases voisines d'une bombe. """
    voisins = voisinage(len(grille), ligne, colonne)
    for l, c in voisins:
        if grille[l][c] != -1: # si ce n'est pas une bombe
            grille[l][c] +=1  		# on ajoute 1 Ã  sa valeur

def genere_grille(bombes):
    """ Renvoie une grille de dÃ©mineur de taille nxn oÃ¹ n est
        le nombre de bombes, en plaÃ§ant les bombes Ã  l'aide de
        la liste bombes de coordonnÃ©es (tuples) passÃ©e en
        paramÃ¨tre. """
    n = len(bombes)
    # Initialisation d'une grille nxn remplie de 0
    grille = [[0 for colonne in range(n)] for ligne in range(n)]

    # Place les bombes et calcule les valeurs des autres cases
    for ligne, colonne in bombes:
        grille[ligne][colonne] = -1  # place la bombe
        incremente_voisins(grille,ligne,colonne)

    return grille
print(genere_grille([(1, 1), (2, 4), (3, 1), (3, 3), (4, 4)]))
