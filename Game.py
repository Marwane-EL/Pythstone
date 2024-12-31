from Les4StructureDeDonnees.ListeChainee import ListeChainee


class Game:
    def __init__(self,joueur1, joueur2,):
        self.joueurs = ListeChainee()
        self.joueurs.ajouter(joueur1)
        self.joueurs.ajouter(joueur2)
        self.tourActuel = self.joueurs.getNoeud(0)
        self.phase = "Draw"
        self.gagnant = None
        self.deck = ListeChainee()

    def changerTour(self):
        if self.tourActuel == self.joueurs.getNoeud(0) :
            self.tourActuel = self.joueurs.getNoeud(1)
        else :
            self.tourActuel = self.joueurs.getNoeud(0)

    def demarrer(self):
        while not self.verifPartieTermine() :
            print("C'est au tour de ", self.tourActuel.name)
            self.gererPhase()
            self.changerTour()

    def gererPhase(self):
        joueurActif = self.tourActuel

        joueurActif.addMana(1)
