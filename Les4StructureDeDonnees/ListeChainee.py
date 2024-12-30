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

    def taille(self):
        courant = self.tete
        compteur = 0
        while courant :
            compteur += 1
            courant = courant.suivant

    def supprimerNoeud(self, noeud_a_supprimer):
        if self.tete is None:
            print("La liste est vide.")
            return

        if self.tete == noeud_a_supprimer:
            self.tete = self.tete.suivant
            return

        courant = self.tete
        while courant.suivant is not None:
            if courant.suivant == noeud_a_supprimer:
                courant.suivant = courant.suivant.suivant
                return
            courant = courant.suivant

        # Si le nœud n'est pas trouvé
        print("Le nœud spécifié n'a pas été trouvé dans la liste.")

    def getNoeud(self, indice):
        courant = self.tete
        compteur = 0
        while courant:
            if compteur == indice:
                return courant  # Retourne le noeud à l'indice donné
            courant = courant.suivant
            compteur += 1
        return None  # Si l'indice est invalide (hors de portée)
