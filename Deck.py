from Les4StructureDeDonnees.ListeChainee import *

class Deck :
    def __init__(self, nom, taille_max):
        self.nom = nom
        self.cartes = ListeChainee()
        self.tailleMax = taille_max

    def ajouterCartes(self, carte):
        self.cartes.ajouter(carte)
        print("Carte ajoutee avec succes dans", self.nom, " : ", carte)

    def retirerCarte(self):
        carteRetirer = self.cartes.retirer()
        return carteRetirer

    '''
    def melanger(self):
    '''

    def afficherDeck(self):
        self.cartes.afficher()

    def estVide(self):
        if self.tete == None :
            return True
        else :
            return False

    def taille(self):
        return self.cartes.taille()

    def estVide(self):
        return self.cartes.tete is None

