def a_doublon(tab):
    tab2 = []
    for i in tab:
        for j in tab2:
            if i==j:
                return True
        tab2.append(i)
    return False
print(a_doublon([1, 2, 4, 6, 6]))
