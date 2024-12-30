class ListeChainee:
    class Noeud:
        def __init__(self, valeur):
            self.valeur = valeur
            self.suivant = None

    def __init__(self):
        self.tete = None

    def ajouter(self, valeur):
        nouveau = self.Noeud(valeur)
        if not self.tete:
            self.tete = nouveau
        else:
            courant = self.tete
            while courant.suivant:
                courant = courant.suivant
            courant.suivant = nouveau

    def retirer(self):
        if not self.tete:
            return None
        valeur = self.tete.valeur
        self.tete = self.tete.suivant
        return valeur

    def afficher(self):
        courant = self.tete
        while courant:
            print(courant.valeur, end=" -> ")
            courant = courant.suivant
        print("None")