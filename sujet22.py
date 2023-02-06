def liste_puissances(a,n):
  t =[]
  for i in range(1,n+1):
    t.append(a**i)   
  return t
def liste_puisssances_borne(a,borne):
  t = []
  i = 1
  ok = True
  
  if a == borne:
    return []
  while ok == True:
    if a ** i < borne:
      t.append( a ** i)
    else:
      ok = False
    i+=1

  return t
    
    

print(liste_puissances(3, 5))
print(liste_puissances(-2, 4))
print(liste_puisssances_borne(2, 16))
print(liste_puisssances_borne(2, 17))
print(liste_puisssances_borne(5, 5))
dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
        "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
        "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
        "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
        "W": 23, "X": 24, "Y": 25, "Z": 26}


def est_parfait(mot):
    # mot est une chaÃ®ne de caractÃ¨res (en lettres majuscules)
    code_concatene = ""
    code_additionne = 0
    for c in mot:
        code_concatene = str(code_concatene) + str(dico[c])
        code_additionne = int(code_additionne) +int(dico[c])
    code_concatene = int(code_concatene)
    if int(code_concatene)  % int(code_additionne) == 0:
        mot_est_parfait = True
    else:
        mot_est_parfait = False
    return code_additionne, code_concatene, mot_est_parfait
print(est_parfait("PAUL"))
print(est_parfait("ALAIN"))
