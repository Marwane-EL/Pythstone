from Hero import *
from Les4StructureDeDonnees.ListeChainee import ListeChainee
from Deck import *
from Minion import *

class Player:
    def __init__(self, hero, deck, mana, name, fatigue):
        self.hero = hero
        self.deck = deck
        self.hand = ListeChainee()
        self.mana = mana
        self.maxMana = 1
        self.name = name
        self.fatigue = fatigue
        self.board = ListeChainee()  # Correction ici

    def drawCard(self):
        if self.deck.taille() == 0:
            self.appliquerFatigue()
        else:
            self.hand.ajouter(self.deck.retirerCarte())

    def appliquerFatigue(self):
        self.fatigue += 1
        self.takeDamage(self.fatigue)
        print(f"{self.name} subit {self.fatigue} dégâts de fatigue !")

    def playCard(self, carte):
        self.board.ajouter(carte)
        self.hand.retirer(carte)  # Vérifie si la main est vide

    def takeDamage(self, amount):
        self.hero.hp -= amount

    def healHero(self, amount):
        self.hero.hp += amount

    def regenererMana(self):
        self.mana = self.maxMana

    def addManaMax(self, amount):
        self.maxMana += amount

    def getManaMax(self):
        return self.maxMana

    def getBoard(self):
        print("#-------------------------------------------------------------------------#")
        print("#\tAffichage du plateau :")
        print("#-------------------------------------------------------------------------#")
        self.board.afficher()
        print("#-------------------------------------------------------------------------#")

    def jouerCarte(self):
        if self.hand.taille() == 0 :
            return
        print("#-------------------------------------------------------------------------#")
        print("#\tAffichage de la main :")
        print("#-------------------------------------------------------------------------#")
        self.hand.afficher()
        print("#-------------------------------------------------------------------------#")
        try:
            num = int(input("#Veuillez jouer une carte (par son numéro) : "))
            carteJouee = self.hand.getNoeud(num)
            if carteJouee is None:
                print("#Indice invalide. Aucune carte n'a été jouée.\n")
                return
            self.board.ajouter(carteJouee.valeur)
            self.hand.supprimerNoeud(carteJouee)
            print(f"#La carte '{carteJouee.valeur}' a été jouée.")
            print("#-------------------------------------------------------------------------#")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un numéro valide.")

