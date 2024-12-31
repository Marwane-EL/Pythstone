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

    def regenerMana(self):
        self.mana = self.maxMana
