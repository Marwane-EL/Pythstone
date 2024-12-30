class File:
    def __init__(self):
        self.elements = []

    def enfiler(self, valeur):
        self.elements.append(valeur)

    def defiler(self):
        if self.est_vide():
            print("La file est vide.")
            return None
        return self.elements.pop(0)

    def est_vide(self):
        return len(self.elements) == 0

    def afficher(self):
        print(" -> ".join(map(str, self.elements)))
