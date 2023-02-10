def recherche(elt,tab):
  indice = -1
  for key,value in enumerate(tab):
    if value == elt:
      indice = key
  return indice


print(recherche(1, [2, 3, 4]))
class AdresseIP:

    def __init__(self, adresse):
        self.adresse = adresse
   
    def liste_octet(self):
        """renvoie une liste de nombres entiers,
           la liste des octets de l'adresse IP"""
        return [int(i) for i in self.adresse.split(".")] 
        
    def est_reservee(self):
        """renvoie True si l'adresse IP est une adresse
           reservee, False sinon"""
        return self.adresse =="192.168.0.0"  or self.adresse == "192.168.0.255"
             
    def adresse_suivante(self):
        """renvoie un objet de AdresseIP avec l'adresse 
           IP qui suit l'adresse self
           si elle existe et False sinon"""
        if self.adresse[3]< 254:
            octet_nouveau = str(self.adresse[3] + 1)
            return AdresseIP('192.168.0.' + octet_nouveau)
        else:
            return False
