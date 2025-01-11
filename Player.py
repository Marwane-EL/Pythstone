from Hero import *
from Les4StructureDeDonnees.ListeChainee import ListeChainee
from Deck import *
from Minion import *

class Player:
    def __init__(self, hero, deck, mana, name, fatigue):
        self.hero = hero
        self.deck = deck
        self.hand = ListeChainee()
        self.mana = mana
        self.maxMana = 1
        self.name = name
        self.fatigue = fatigue
        self.board = ListeChainee()  # Correction ici
        self.ennemy = None

    def drawCard(self):
        if self.deck.taille() == 0:
            self.appliquerFatigue()
        else:
            self.hand.ajouter(self.deck.retirerCarte())

    def appliquerFatigue(self):
        self.fatigue += 1
        self.takeDamage(self.fatigue)
        print(f"{self.name} subit {self.fatigue} dégâts de fatigue !")

    def takeDamage(self, amount):
        self.hero.hp -= amount

    def healHero(self, amount):
        self.hero.hp += amount

    def regenererMana(self):
        self.mana = self.maxMana

    def addManaMax(self, amount):
        self.maxMana += amount

    def getManaMax(self):
        return self.maxMana
    
    def getEnnemy(self) :
        return self.ennemy

    def setEnnemy(self, ennemy):
        self.ennemy = ennemy


    def getBoard(self):
        print("#-------------------------------------------------------------------------#")
        print("#\tAffichage du plateau :")
        print("#-------------------------------------------------------------------------#")
        self.board.afficher()
        print("#-------------------------------------------------------------------------#")

    def attaque(self):
        if self.board.taille() == 0 :
            print(f"{self.name} n'a pas de serviteurs.")
            return
        
        if self.ennemy.board.taille() == 0:
            print(f"{self.ennemy.name} n'a pas de serviteurs.")
            return 
        
        print("Serviteurs disponibles pour attaquer :")
        self.getBoard()

        # Choisir un attaquant
        choix_attaquant = input("Choisissez un serviteur pour attaquer : ")
        try:
            choix_attaquant = int(choix_attaquant)
        except ValueError:
            print("Entrée invalide. Action annulée.")
            return

        if 0 <= choix_attaquant <= self.board.taille():
            attaquant = self.board.getNoeud(choix_attaquant).valeur
        else:
            print("Choix invalide. Action annulée.")
            return

        # Choisir une cible
        print("Choisissez une cible parmi les serviteurs ennemis ou le héros adverse.")
        adversaire = self.getEnnemy()  # Méthode à implémenter pour obtenir l'adversaire
        print("Serviteurs ennemis disponibles :")
        self.ennemy.getBoard()

        choix_cible = input("Entrez le numéro de la cible : ")
        try:
            choix_cible = int(choix_cible)
        except ValueError:
            return

        if 0 <= choix_cible <= adversaire.board.taille():
            cible = adversaire.board.getNoeud(choix_cible).valeur
            #Faut rajouter le fait d'attaquer le heros d'en face
        else:
            print("Choix invalide. Action annulée.")
            return

        print(f"{attaquant.name} attaque {cible.name} !")
        attaquant.attaquer(cible)  # Méthode à définir dans `Hero` et `Minion`
        
        # Supprimer les serviteurs morts
        self.nettoyerPlateau(self.board)
        adversaire.nettoyerPlateau(adversaire.board)

    def jouerCarte(self):
        if self.hand.taille() == 0 :
            return
        print("#-------------------------------------------------------------------------#")
        print("#\tAffichage de la main :")
        print("#-------------------------------------------------------------------------#")
        self.hand.afficher()
        print("#-------------------------------------------------------------------------#")
        try:
            num = int(input("#Veuillez jouer une carte (par son numéro) : "))
            carteJouee = self.hand.getNoeud(num)
            if carteJouee is None:
                print("#Indice invalide. Aucune carte n'a été jouée.\n")
                return

            # Accéder à la valeur pour l'ajouter au plateau
            self.board.ajouter(carteJouee.valeur)

            # Supprimer le nœud de la main
            self.hand.supprimerNoeud(carteJouee)
            print(f"#La carte '{carteJouee.valeur.getName()}' a été jouée.")

            print("#-------------------------------------------------------------------------#")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un numéro valide.")

    def nettoyerPlateau(self, board):
        """
        Supprime tous les nœuds du board (ListeChainee) correspondant à des minions morts.

        :param board: Le plateau (ListeChainee) à nettoyer.
        """
        courant = board.tete
        precedent = None

        while courant is not None:
            # On vérifie si le minion est mort (exemple : HP <= 0)
            if courant.valeur.hp <= 0:
                print(courant.valeur.name, " a péri")
                if precedent is None:  # Le nœud courant est la tête
                    board.tete = courant.suivant
                else:  # On connecte le précédent au suivant
                    precedent.suivant = courant.suivant
            else:
                precedent = courant  # On avance le précédent uniquement si le nœud n'a pas été supprimé

            courant = courant.suivant  # On passe au nœud suivant




