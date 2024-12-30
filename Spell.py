from Card import card

class spell(card) :
    def init(self, effect, name, cost):
        super().init(name, cost)
        self.effect = effect

    def changerEffect(self, effect):
        self.effect = effect

    def getEffect(self):
        print("l'effet de la carte est : " + self.effect)

    def str(self):
            print("la carte " + self.name + " a pour coût " + self.cost + " mana et a pour effet de " + self.effect)