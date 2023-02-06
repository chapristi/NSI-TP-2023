def recherche(tab,n):
  i = -1
  for key,value in enumerate(tab):
    if n == value:
      i = key
  return i
print(recherche([2, 3, 4, 5, 6], 5))
print(recherche([2, 3, 4, 6, 7], 5))

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def position_alphabet(lettre):
    return ord(lettre) - ord('A')
def cesar(message, decalage):
    resultat = ''
    for c in message:
        if 'A' <= c and c <= 'Z':
            indice = ( position_alphabet(c) + decalage ) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat  + c
    return resultat

print(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4))
print(cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5))
