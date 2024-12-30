from Les4StructureDeDonnees.ListeChainee import *

class Main :
    def __init__(self, nom, cartes, joueur):
        self.nom = nom
        self.cartes = cartes
        self.joueur = joueur

    def ajouterCartes(self, carte):
        self.cartes.ajouter(carte)

    def retirerCarte(self, carte):
        self.cartes.supprimerNoeud(carte)

    def piocher(self, deck):
        self.cartes.ajouter(deck.retirer())

    def estPleine(self):
        if self.taille >= 10 :
            return True
        else :
            return False

