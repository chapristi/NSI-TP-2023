def min_et_max(tab):
  
  min = tab[0]
  max = tab[0]
  for i in tab:
    if i < min:
      min = i
    if i > max:
      max = i
  return {"min" : min,"max":max}
print(min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]))
class Carte:
    def __init__(self, c, v):
        """ Initialise les attributs couleur (entre 1 et 4), et valeur (entre 1 et 13). """
        self.couleur = c
        self.valeur = v

    def get_valeur(self):
        """ Renvoie la valeur de la carte : As, 2, ..., 10, Valet, Dame, Roi """
        valeurs = ['As','2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi']
        return valeurs[self.valeur - 1]

    def get_couleur(self):
        """ Renvoie la couleur de la carte (parmi pique, coeur, carreau, trÃ¨fle). """
        couleurs = ['pique', 'coeur', 'carreau', 'trÃ¨fle']
        return couleurs[self.couleur - 1]

class Paquet_de_cartes:
    def __init__(self):
        self.contenu = []
        for i in range(1,5):
          for j in range(1,14):
            self.contenu.append(Carte(i,j))
        # A complÃƒÂ©ter

    def get_carte(self, pos):
        assert pos < 52 and pos > -1, "paramÃ¨tre pos     invalide"
        return self.contenu[pos]
        # A complÃƒÂ©ter
jeu = Paquet_de_cartes()
carte1 = jeu.get_carte(20)

print(carte1.get_valeur() + " de " + carte1.get_couleur())
