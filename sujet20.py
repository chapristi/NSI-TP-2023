def ajoute_dictionnaires(d1, d2):
    d = {}
    for k in d1:
        if k in d2 :
            d[k] = d1[k] + d2[k]
        else :
            d[k] = d1[k]
    for k in d2 :
        if k not in d:
            d[k] = d2[k]
    return d
      
    
    

        
print(ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}))
print( ajoute_dictionnaires({}, {2: 9, 3: 11}))
print(ajoute_dictionnaires({1: 5, 2: 7}, {}))
from random import randint
def nbre_coups():
    n = 0
    cases_vues = [0]
    case_en_cours = 0
    nbre_cases = 12
    while len(cases_vues) < nbre_cases:
        x = randint(1, 6)
        case_en_cours = (case_en_cours + x) % nbre_cases
        if case_en_cours not in cases_vues:
            cases_vues.append(case_en_cours)
        n = n+1
    return n
print(nbre_coups())
