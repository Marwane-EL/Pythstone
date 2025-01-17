class File:
    def __init__(self):
        self.elements = []
        self.debut = 0
        self.fin = 0

    def enfiler(self, valeur):
        """Ajoute un élément à la fin de la file."""
        self.elements.append(valeur)
        self.fin += 1  # Augmente la position du dernier élément

    def defiler(self):
        """Retire et retourne l'élément en tête de la file."""
        if self.est_vide():
            print("La file est vide.")
            return None
        valeur = self.elements[self.debut]
        self.debut += 1
        return valeur

    def est_vide(self):
        """Vérifie si la file est vide."""
        return self.debut == self.fin

    def taille(self):
        return self.fin - self.debut

    def afficher(self):
        """Affiche les éléments de la file."""
        if self.est_vide():
            print("La file est vide.")
        else:
            courant = self.debut
            compteur = 0
            while courant < self.fin:
                print("Num :", compteur, " ", self.elements[courant])
                courant += 1
                compteur += 1

    def tete(self):
        """Retourne l'élément en tête de la file sans le retirer."""
        if self.est_vide():
            print("La file est vide.")
            return None
        return self.elements[self.debut]
