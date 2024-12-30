class card :
    def init(self, name, cost):
        self.name = name
        self.cost = cost

    def str(self):
        print("la carte " + self.name + " a pour coût " + self.cost + " mana")

