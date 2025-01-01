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

        self.phaseDebut(joueurActif)

        # 2. Phase principale
        print("Phase principale")
        self.phasePrincipale(joueurActif)

        # 3. Phase d’attaque (optionnel si séparée)
        print("Phase d'attaque")
        self.phaseAttaque(joueurActif)

        # Vérification de la fin de partie
        if not joueurActif.hero.isAlive():
            print(f"{joueurActif.name} a perdu !")
            self.finDePartie()
            return

    def phaseDebut(self, joueur):
        joueur.addManaMax(1)
        joueur.regenererMana()
        joueur.piocherCarte()

    def phasePrincipale(self, joueur):
        joueur.jouerCarte()

    def phaseAttaque(self, joueur):
        joueur.attaque()


