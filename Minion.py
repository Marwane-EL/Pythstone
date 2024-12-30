from Card import card


class minion(card) :
    def init(self, attackPoints, healthPoints, name, cost):
        super().init(name, cost)
        self.ap = attackPoints
        self.hp = healthPoints

    def changerAP(self, attackPoints):
        self.ap = attackPoints

    def changerHP(self, healthPoints):
        self.hp = healthPoints

    def getAP(self):
        print("l'attaque de cette carte est de : " + self.ap)

    def getHP(self):
        print("la vie de cette carte est de : " + self.hp)

    def str(self):
        print("la carte " + self.name + " a pour coût " + self.cost + " mana et a " + self.ap + " points attaques et " + self.hp + " points de vie")
