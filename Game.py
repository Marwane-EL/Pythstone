from Les4StructureDeDonnees.ListeChainee import ListeChainee
from Hero import *
from Deck import *
from Minion import *
from Player import *

class Game:
    def __init__(self, joueur1, joueur2):
        self.joueurs = ListeChainee()
        self.joueurs.ajouter(joueur1)
        self.joueurs.ajouter(joueur2)
        self.tourActuel = self.joueurs.getNoeud(0).valeur  # Accède directement au joueur
        self.phase = "Draw"
        self.gagnant = None

    def changerTour(self):
        # Alterne entre les joueurs
        if self.tourActuel == self.joueurs.getNoeud(0).valeur:
            self.tourActuel = self.joueurs.getNoeud(1).valeur
        else:
            self.tourActuel = self.joueurs.getNoeud(0).valeur

    def demarrer(self):
        while not self.verifPartieTermine():
            print("\n#-------------------------------------------------------------------------#")
            print("#C'est au tour de", self.tourActuel.name)
            self.gererPhase()
            self.changerTour()
        print("Fin de la partie.")

    def verifPartieTermine(self):
        # Vérifie si le joueur actuel ou son adversaire a perdu
        if self.tourActuel.hero.hp <= 0:
            print(f"La partie est terminée ! {self.tourActuel.name} a perdu.")
            return True
        adversaire = self.getAdversaire()
        if adversaire.hero.hp <= 0:
            print(f"La partie est terminée ! {adversaire.name} a perdu.")
            return True
        return False

    def gererPhase(self):
        joueurActif = self.tourActuel
        self.phaseDebut(joueurActif)
        print("#\tPhase principale :")
        self.phasePrincipale(joueurActif)
        print("#\tPhase d'attaque :")
        self.phaseAttaque(joueurActif)

    def phaseDebut(self, joueur):
        joueur.addManaMax(1)  # Ajout de mana max
        joueur.regenererMana()  # Régénération du mana actuel
        joueur.drawCard()  # Pioche une carte

    def phasePrincipale(self, joueur):
        try:
            joueur.jouerCarte()  # Permet au joueur de jouer une carte
        except Exception as e:
            print("Erreur lors de la phase principale :", e)

    def phaseAttaque(self,joueur):
        try:
            joueur.setEnnemy(self.getAdversaire())
            joueur.attaque()  # Action d'attaque (à implémenter dans Player)
        except AttributeError:
            print(f"{joueur.name} n'a pas de méthode d'attaque définie.")
            print("#-------------------------------------------------------------------------#")

    def getAdversaire(self):
        return self.joueurs.getNoeud(1).valeur if self.tourActuel == self.joueurs.getNoeud(0).valeur else self.joueurs.getNoeud(0).valeur

#---------------------------------------------------------------------------#
#   Test de la classe Player
#---------------------------------------------------------------------------#

hero = Hero("Rexxar", 30)
hero2 = Hero("Jaina", 30)
#---------------------------------------------------------------------------#


#---------------------------------------------------------------------------#
#     Creation du deck :
#---------------------------------------------------------------------------#
deck = Deck("Deck joueur1", 30)
minion1 = Minion(2, 2, "Singe", 2)
minion2 = Minion(3, 4, "Rhino", 3)
minion3 = Minion(6, 8, "Paladin", 7)

deck2 = Deck("Deck joueur1", 30)
Lievre = Minion(1, 1, "Lievre", 1)
Sanglier = Minion(3, 6, "Sanglier", 4)
Golem = Minion(8, 8, "Golem", 7)

print("#-------------------------------------------------------------------------#")
print("#\tAjout des cartes : ")
print("#-------------------------------------------------------------------------#")
deck.ajouterCartes(minion1)
deck.ajouterCartes(minion2)
deck.ajouterCartes(minion3)

deck2.ajouterCartes(Lievre)
deck2.ajouterCartes(Sanglier)
deck2.ajouterCartes(Golem)
print("#-------------------------------------------------------------------------#")
#---------------------------------------------------------------------------#


#---------------------------------------------------------------------------#
#   Test des methodes de player :
#---------------------------------------------------------------------------#
joueur1 = Player(hero, deck, 1, "Marwane", 0)
joueur2 = Player(hero2, deck2, 1, "Farouk", 0)

joueur1.addManaMax(1)
joueur2.addManaMax(1)

print()
print("Affichage du mana de joueur1 :", joueur1.getManaMax())
print("Affichage du mana de joueur2 :", joueur2.getManaMax())
print()

print("Le joueur1 pioche deux cartes")
joueur1.drawCard()
joueur1.drawCard()

print("Le joueur2 pioche deux cartes")
joueur2.drawCard()
joueur2.drawCard()
print()

print("\nAffichage du deck du joueur1: ")
print(deck.afficherDeck())

print("\nAffichage du deck du joueur2: ")
print(deck2.afficherDeck())
print()

print
partie1 = Game(joueur1, joueur2)
print("#-------------------------------------------------------------------------#")
print("#\tDebut de la partie :")
print("#-------------------------------------------------------------------------#")
partie1.demarrer()
print("#-------------------------------------------------------------------------#")
#---------------------------------------------------------------------------#


