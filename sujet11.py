def convertir(tab):
    fin = 0
    for key,value in enumerate(tab):
        if value ==1:
            fin+= 2**((len(tab) -key )-1)
    return fin
print(
    convertir([1, 0, 1, 0, 0, 1, 1])
)
print(
     convertir([1, 0, 0, 0, 0, 0, 1, 0])
)

liste = [9, 5, 8, 4, 0, 2, 7, 1, 10, 3, 6]

def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        # la variable j sert Ã   dÃ©terminer oÃ¹ placer la valeur Ã   ranger
        j = i
        # tant qu'on a pas trouvÃ© la place de l'Ã©lÃ©ment Ãƒ  insÃ©rer
        # on dÃ©cale les valeurs du tableau vers la droite
        while j > 0 and valeur_insertion < tab[j-1]:
            tab[j] = tab[j-1]
            j = j-1
        tab[j] = valeur_insertion
