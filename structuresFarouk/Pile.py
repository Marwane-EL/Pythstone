# Auteur : Farouk Mohamed Bendeddouche
class Pile:
    class Noeud:
        def __init__(self, valeur, suivant=None):
            self.valeur = valeur
            self.suivant = suivant

    def __init__(self):
        self.sommet = None

    def est_vide(self) -> bool:
        """Vérifie si la pile est vide."""
        return self.sommet is None

    def taille(self) -> int:
        """Retourne le nombre d'éléments dans la pile."""
        count = 0
        courant = self.sommet
        while courant:
            count += 1
            courant = courant.suivant
        return count

    def empiler(self, valeur):
        """Ajoute un élément au sommet de la pile."""
        nouveau = self.Noeud(valeur)
        if self.est_vide():
            self.sommet = nouveau
        else:
            nouveau.suivant = self.sommet
            self.sommet = nouveau

    def depiler(self):
        """Retire et retourne l'élément au sommet de la pile."""
        if self.est_vide():
            print("La pile est vide, impossible de dépiler.")
            return None
        valeur = self.sommet.valeur
        self.sommet = self.sommet.suivant
        return valeur

    def sommet(self):
        """Retourne l'élément au sommet de la pile sans le retirer."""
        if self.est_vide():
            print("La pile est vide.")
            return None
        return self.sommet.valeur

    def afficher(self):
        """Affiche les éléments de la pile."""
        if self.est_vide():
            print("La pile est vide.")
        else:
            courant = self.sommet
            result = ""
            while courant:
                result += str(courant.valeur) + " -> "
                courant = courant.suivant
            print(result[:-4])  # Enlève le dernier " -> "

    def __str__(self) -> str:
        """Retourne une représentation en chaîne des éléments de la pile."""
        if self.est_vide():
            return "Pile vide"
        courant = self.sommet
        result = ""
        while courant:
            result += str(courant.valeur) + " -> "
            courant = courant.suivant
        return result[:-4]  # Enlève le dernier " -> "
