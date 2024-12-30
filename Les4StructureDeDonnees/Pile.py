class Pile:
    def __init__(self):
        self.elements = []

    def empiler(self, valeur):
        self.elements.append(valeur)

    def depiler(self):
        if self.est_vide():
            print("La pile est vide.")
            return None
        return self.elements.pop()

    def sommet(self):
        if self.est_vide():
            print("La pile est vide.")
            return None
        return self.elements[-1]

    def est_vide(self):
        return len(self.elements) == 0
