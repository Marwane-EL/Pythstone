from Card import card
from Les4StructureDeDonnees.File import *


class Minion(card) :
    def __init__(self, attackPoints, healthPoints, name, cost):
        super().init(name, cost)
        self.ap = attackPoints
        self.hp = healthPoints
        self.effet = File()

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
        self.hp = self.hp - minion.ap
        minion.hp = minion.hp - self.ap

    def attaquerHero(self, hero):
        hero.hp -= self.ap

    def __str__(self):
        return f"| {self.name:<10} | Attaque: {self.ap:<2} | Défense: {self.hp:<2} | Coût: {self.cost:<2} |"

    def ajouterEffet(self, effet):
        self.effet.enfiler(effet)