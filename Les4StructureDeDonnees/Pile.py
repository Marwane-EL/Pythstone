class Pile:
    def __init__(self):
        self.elements = []

    def empiler(self, valeur):
        self.elements.append(valeur)

    def depiler(self):
        if self.estVide():
            print("La pile est vide.")
            return None
        return self.elements.pop()

    def sommet(self):
        if self.estVide():
            print("La pile est vide.")
            return None
        return self.elements[-1]

    def estVide(self):
        return len(self.elements) == 0

    def afficher(self):
        temp = Pile()  # Pour eviter de detruire la pile d'origine
        compteur = 0

        while not self.estVide():
            valeur = self.depiler()
            print("Num :", compteur, " ", valeur)
            temp.empiler(valeur)
            compteur += 1

        while not temp.estVide():
            self.empiler(temp.depiler())

    def taille(self):
        compteur = 0
        temp = Pile()  #Pour sauvegarder les éléments

        while not self.estVide():
            temp.empiler(self.depiler())
            compteur += 1

        while not temp.estVide():
            self.empiler(temp.depiler())

        return compteur

