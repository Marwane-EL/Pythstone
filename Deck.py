from Les4StructureDeDonnees.Pile import *

class Deck :
    def __init__(self, nom, taille_max):
        self.nom = nom
        self.cartes = Pile()
        self.tailleMax = taille_max

    def ajouterCartes(self, carte):
        self.cartes.empiler(carte)
        print("Carte ajoutee avec succes dans", self.nom, " : ", carte)

    def retirerCarte(self):
        carteRetirer = self.cartes.depiler()
        return carteRetirer

    def afficherDeck(self):
        self.cartes.afficher()

    def estVide(self):
        if self.cartes.estVide() == True:
            return True
        else :
            return False

    def taille(self):
        return self.cartes.taille()

