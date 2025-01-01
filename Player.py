
from Hero import *
from Les4StructureDeDonnees.ListeChainee import ListeChainee

class Player :
    def __init__(self, hero, deck, hand, mana, name, fatigue):
        self.hero = hero
        self.deck = deck
        self.hand = hand
        self.mana = mana
        self.maxMana = 1
        self.name = name
        self.fatigue = fatigue
        self.board = ListeChainee

    def drawCard(self):
        if self.deck.taille() == 0 :
            self.appliquerFatigue()
        else :
            self.hand.ajouter(self.deck.retirerCarte())

    def playCard(self, carte):
        self.board.ajouter(carte)
        self.hand.retirer(carte) #Verifier si la main est vide

    def takeDamage(self, amount):
        self.hero.hp -= amount

    def healHero(self, amount):
        self.hero.hp += amount

    def regenererMana(self):
        self.mana = self.maxMana

    def addManaMax(self, amount):
        self.maxMana += amount

    def getManaMax(self):
        print("Le montant du mana de " + self.hero.getName() + " est de ",self.maxMana + "\n")

    def jouerCarte(self):
        self.hand.afficher()
        num = input("Veuillez joueur une carte (par son numero) : ")
        carteJouee = self.hand.getNoeudIndice(num)
        self.board.ajouter(carteJouee)
        self.hand.supprimerNoeud(carteJouee)

hero = Hero("Rexxar", 30)

deck = ListeChainee()
deck.ajouter(1)
deck.ajouter(2)
deck.ajouter(3)

hand = ListeChainee()
deck.ajouter(4)
deck.ajouter(5)
deck.ajouter(6)


joueur1 = Player(hero, deck, hand, 1, "Marwane", 0)
joueur1.addManaMax(1)
joueur1.getManaMax()




