def max_dico(dico):
  keyMax,max = "",0
  for i in dico:
    if dico[i] > max:
      max =dico[i]
      keyMax = i
  return (keyMax,max)
print(max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}))
print(max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50}))


class Pile:
    """
    Classe definissant une structure de pile.
    """
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """
        Renvoie le booleen True si la pile est vide, False sinon.
        """
        return self.contenu == []

    def empiler(self, v):
        """
        Place l'element v au sommet de la pile
        """
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'element place au sommet de la pile,
        si la pile n'est pas vide.
        """
        if not self.est_vide():
            return self.contenu.pop()


def eval_expression(tab):
    p = Pile()
    for element in tab:
        if element != '+' and  element != '*':
            p.empiler(element)
        else:
            if element == '+':
                resultat = p.depiler() + p.depiler()
            else:
                resultat = p.depiler() *  p.depiler()
            p.empiler(resultat)
    return p.depiler()
print(eval_expression([2, 3, '+', 5, '*']))
