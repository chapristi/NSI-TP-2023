def moyenne(tab):
    coef = 0
    note = 0
    for i in tab:
        note += i[0] * i[1]
        coef += i[1]
    if coef == 0:
        return None
    return note / coef
      
print(moyenne([(15, 2), (9, 1), (12, 3)]))


def pascal(n):
    triangle= [[1]]
    for k in range(1,n+1):
        ligne_k = [1]
        for i in range(1,k):
            ligne_k.append(triangle[k-1][i-1]+triangle[k-1][i])
        ligne_k.append(1)
        triangle.append(ligne_k)
    return triangle
print(
    pascal(
        6
    )
)
