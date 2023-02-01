def indices_max(tab):
    max = tab[0]
    t = [0]
    if len(tab) ==1:
        return (max,t)
    for index,value in enumerate(tab):
        if value > max:
            max = value
            t = [index]
        elif value == max:
            t.append(index)
    return (max,t)
print(indices_max([7]))


def positif(pile):
    pile_1 = list(pile)
    pile_2 = list()
    while pile_1 != []:
        x = pile_1.pop()
        if x >= 0:
            pile_2.append(x)
    while pile_2 != []:
        x = pile_2.pop()
        pile_1.append(x)
    return pile_1
print(positif([-1, 0, 5, -3, 4, -6, 10, 9, -8]))
