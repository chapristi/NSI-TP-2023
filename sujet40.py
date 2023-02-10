def nombre_de_mots(phrase):
  count = 1
  warning = ["?","!"]
  for key,value in enumerate(phrase):
    if value == " " and phrase[key+1] != warning[0] and phrase[key+1] != warning[1]:
      count+= 1
  return count
print( nombre_de_mots('Cet exercice est simple.'))
print(nombre_de_mots('Le point d exclamation est separe !'))
print(nombre_de_mots('Combien de mots y a t il dans cette phrase ?'))
print(nombre_de_mots('Fin.')

class Noeud:
    def __init__(self, valeur):
        '''MÃ©thode constructeur pour la classe Noeud. ParamÃ¨tre d'entrÃ©e : valeur (int)'''
        self.valeur = valeur
        self.gauche = None
        self.droit = None
    def getValeur(self):
        '''MÃ©thode accesseur pour obtenir la valeur du noeud Aucun paramÃ¨tre en entrÃ©e'''
        return self.valeur
    def droitExiste(self):
        '''MÃ©thode renvoyant True si le sous-arbre droit est non vide Aucun paramÃ¨tre en entrÃ©e'''
        return (self.droit is not None)
    def gaucheExiste(self):
        '''MÃ©thode renvoyant True si le sous-arbre gauche est non vide Aucun paramÃ¨tre en entrÃ©e'''
        return (self.gauche is not None)
    def inserer(self, cle):
        '''MÃ©thode d'insertion de clÃ© dans un arbre binaire de recherche ParamÃ¨tre d'entrÃ©e : cle (int)'''
        if cle < self.valeur :
            # on insÃ¨re Ã  gauche
            if self.gaucheExiste():
                # on descend Ã  gauche et on recommence le test initial
                return self.gauche.inserer(cle)
            else:
                # on crÃ©e un fils gauche
                self.gauche = Noeud(cle)
        elif cle > self.valeur:
            # on insÃ¨re Ã  droite
            if self.droitExiste():
                # on descend Ã  droite et on recommence le test initial
                return  self.droit.inserer(cle)
            else:
                # on crÃ©e un fils droit
                self.droit  = Noeud(cle)
arbre = Noeud(7)
for cle in (3, 9, 1, 6):
  arbre.inserer(cle)
print(arbre.gauche.getValeur())
print(arbre.droit.getValeur())
print(arbre.gauche.gauche.getValeur())
print(arbre.gauche.droit.getValeur())


