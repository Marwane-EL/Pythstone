class NoeudArbre:
    def __init__(self, valeur):
        self.valeur = valeur
        self.enfants = []

    def ajouter_fils(self, enfant):
        self.enfants.append(enfant)

    def parcourir(self, profondeur=0):
        print("  " * profondeur + str(self.valeur))
        for enfant in self.enfants:
            enfant.parcourir(profondeur + 1)

class Arbre:
    def __init__(self, valeur_racine):
        self.racine = NoeudArbre(valeur_racine)

    def parcourir(self):
        if self.racine:
            self.racine.parcourir()
        else:
            print("L'arbre est vide.")
