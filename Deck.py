from Les4StructureDeDonnees.ListeChainee import *

class deck :
    def __init__(self, nom, cartes, taille_max):
        self.nom = nom
        self.cartes = cartes
        self.tailleMax = taille_max

    def ajouterCartes(self, carte):
        self.cartes.ajouter(carte)

    def retirerCarte(self):
        self.cartes.retirer()

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
        self.cartes.taille()

