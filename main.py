######################################
#### Arbres Binaires de Recherche ####
######################################

# 1 | Arbres Binaires de recherche


class ABR:

  def __init__(self, val):
    self.valeur = val
    self.gauche = None
    self.droit = None

  def ajoute(self, valeur):
    if valeur < self.valeur:
      if self.gauche is None:
        self.gauche = ABR(valeur)
      else:
        self.gauche.ajoute(valeur)
    elif valeur > self.valeur:
      if self.droit is None:
        self.droit = ABR(valeur)
      else:
        self.droit.ajoute(valeur)

  def recherche(self, val):
    if val < self.valeur:
      return self.gauche.recherche(val) if self.gauche else False
    elif val > self.valeur:
      return self.droit.recherche(val) if self.droit else False

  def recherche1(self, val):
    while self.valeur is not None:
      if val < self.valeur:
        if not self.gauche: return False
        self = self.gauche
      elif val > self.valeur:
        if not self.droit: return False
        self = self.droit
      else:
        return True

  def min(self):
    s = self
    while s.gauche:
      s = s.gauche
    return s.valeur

  def max(self):
    s = self
    while s.droit:
      s = s.droit
    return s.valeur

  def __repr__(self):
    return str(self.valeur) + "\n | " + str(self.gauche)+ " | " +  str(self.droit)
    


arbre = ABR(17)
arbre.ajoute(10)
arbre.ajoute(23)
arbre.ajoute(19)
arbre.ajoute(25)
arbre.ajoute(20)

arbre.recherche(19)
arbre.recherche(18)