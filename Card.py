class card :
    def init(self, name, cost):
        self.name = name
        self.cost = cost

    def __str__(self):
        print(self.name, " ", self.cost)

