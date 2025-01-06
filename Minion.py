from Card import card


class Minion(card) :
    def __init__(self, attackPoints, healthPoints, name, cost):
        super().init(name, cost)
        self.ap = attackPoints
        self.hp = healthPoints

    def changerAP(self, attackPoints):
        self.ap = attackPoints

    def changerHP(self, healthPoints):
        self.hp = healthPoints

    def getName(self) : 
        return self.name

    def getAP(self):
        print("l'attaque de cette carte est de : " + self.ap)

    def getHP(self):
        print("la vie de cette carte est de : " + self.hp)

    def attaquer(self, minion):
        self.hp -= minion.ap
        minion.hp -= self.hp

    def __str__(self):
        return f"| {self.name:<10} | Attaque: {self.ap:<2} | Défense: {self.hp:<2} | Coût: {self.cost:<2} |"

