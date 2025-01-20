#autheur: Farouk Bendeddouche
class File:
    class Noeud:
        def __init__(self, valeur, suivant=None):
            self.valeur = valeur
            self.suivant = suivant

    def __init__(self):
        self.debut = None
        self.fin = None

    def est_vide(self) -> bool:
        """Vérifie si la file est vide."""
        return self.debut is None

    def taille(self) -> int:
        """Retourne le nombre d'éléments dans la file."""
        count = 0
        courant = self.debut
        while courant:
            count += 1
            courant = courant.suivant
        return count

    def enfiler(self, valeur):
        """Ajoute un élément à la fin de la file."""
        nouveau = self.Noeud(valeur)
        if self.est_vide():
            self.debut = self.fin = nouveau
        else:
            self.fin.suivant = nouveau
            self.fin = nouveau

    def defiler(self):
        """Retire et retourne l'élément au début de la file."""
        if self.est_vide():
            print("La file est vide, impossible de défiler.")
            return None
        valeur = self.debut.valeur
        self.debut = self.debut.suivant
        if self.debut is None:
            self.fin = None  # La file est vide maintenant
        return valeur

    def sommet(self):
        """Retourne l'élément au début de la file sans le retirer."""
        if self.est_vide():
            print("La file est vide.")
            return None
        return self.debut.valeur

    def afficher(self):
        """Affiche les éléments de la file."""
        if self.est_vide():
            print("La file est vide.")
        else:
            courant = self.debut
            result = ""
            while courant:
                result += str(courant.valeur) + " -> "
                courant = courant.suivant
            print(result[:-4])  # Enlève le dernier " -> "

    def __str__(self) -> str:
        """Retourne une représentation en chaîne des éléments de la file."""
        if self.est_vide():
            return "File vide"
        courant = self.debut
        result = ""
        while courant:
            result += str(courant.valeur) + " -> "
            courant = courant.suivant
        return result[:-4]  # Enlève le dernier " -> "

    def __str__(self) -> str:
        """Retourne une représentation en chaîne des éléments de la file."""
        if self.est_vide():
            return "File vide"

        result = ""
        for e in self.elements:
            result += str(e) + " -> "

        # On enlève le dernier " -> " ajouté à la fin
        return result[:-4]


