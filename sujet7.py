def fusion(tab1,tab2):
  tab = tab1+tab2
  tabend = []
  while len(tab) != 0:
    min_value = tab[0]
    i_min = 0
    for key,value in enumerate(tab):
      if value < min_value:
        min_value = value 
        i_min = key
    tabend.append(min_value)
    tab.pop(i_min)
  return tabend
print(fusion([3, 5], [2, 5]))
print(fusion([-2, 4], [-3, 5, 10]))
print(fusion([4], [2, 6]))




romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def traduire_romain(nombre) :
    """ Renvoie l'ecriture decimale du nombre donnÃ© en chiffres romains """
    if len(nombre) == 1:
        return 1
    elif romains[nombre[0]] >= romains[nombre[1]] :
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return romains[nombre[1]] - traduire_romain(nombre[1:])
print(traduire_romain("XIV"))
print(traduire_romain("CXLII"))
print(traduire_romain("MMXXIII"))
