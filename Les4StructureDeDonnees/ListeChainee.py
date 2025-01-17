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
        compteur = 1
        while courant:
            print("Num : ", compteur, " ", courant.valeur)
            courant = courant.suivant
            compteur += 1

    def taille(self):
        courant = self.tete
        compteur = 0
        while courant:
            compteur += 1
            courant = courant.suivant
        return compteur

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

    def supprimer_noeudIndice(self, indice):
        # Cas 1 : Liste vide
        if self.tete is None:
            print("La liste est vide, rien à supprimer.")
            return

        # Cas 2 : Suppression de la tête
        if indice == 0:
            self.tete = self.tete.suivant
            return

        # Cas 3 : Suppression d'un autre nœud
        courant = self.tete
        precedent = None
        compteur = 0

        while courant is not None and compteur < indice:
            precedent = courant
            courant = courant.suivant
            compteur += 1

        # Si l'indice est hors limites
        if courant is None:
            print("Indice hors limites.")
            return

        precedent.suivant = courant.suivant
