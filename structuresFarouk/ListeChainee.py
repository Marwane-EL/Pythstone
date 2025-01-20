#Auteur : Farouk Mohamed Bendeddouche
class ListeChainee:
    class Chaine:
        def __init__(self,valeur, suivant=None):
            self.valeur = valeur
            self.suivant = suivant

        def getValeur(self):
            return self.valeur
        
        def getSuivant(self):
            return self.suivant
        
        def setValeur(self, nvValeur):
            self.valeur = nvValeur

        def setSuivant(self,nvSuivant):
            self.suivant = nvSuivant

        def __str__(self) -> str:
            return f"Valeur: {self.valeur}, Suivant: {self.suivant}"


    def __init__(self):
        self.tete = None

    def longeur(self) -> int:
        currentChaine = self.tete
        longeur = 0
        while currentChaine != None:
            currentChaine = currentChaine.suivant
            longeur +=1
        return longeur

    def add(self,valeur,pos: int = None) -> bool: #si position est null alors par default on ajoute la valeur à la fin et le :int veut dire que le type de pos est un int
        longeur = self.longeur()
        if pos == None or self.tete == None: # par default ou si la liste est vide la methode add ajoute la valeur a la premiere position
            if pos != None:
                print("la liste chainee est vide donc votre valeur est ajouter a la premiere position")
            self.tete = self.Chaine(valeur)
        elif pos < 1 :
            print("la valeur doit être comprise entre 1 et la position de la derniere valeur qui est de " + longeur)
            return False
        else:
            currentPos = 0
            currentChaine = self.tete
        
            while currentPos != pos:
                currentChaine = currentChaine.suivant
                currentPos += 1
            
            #ici on arrive a la chaine avant la position voulu
            oldPosChaine = currentChaine.suivant #on sauvegarde l'ancienne chaine sur la position Pos
            currentChaine = self.Chaine(valeur, oldPosChaine) #on insere la valeur donnee a la postition Pos en continuant la liste avec l'ancienne chaine  
        
        return True
    
    def pop(self,valeur = None) -> bool: #true : pop reussi ;false : pop non reussi
        if self.tete == None:
                print("la liste chainee est vide donc aucune valeur n'a etait supprimer")
        elif valeur == None: #supprime la derniere valeur ajouter (donc la premiere chaine)
            self.tete.valeur = self.tete.suivant
        else:
            currentChaine = self.tete
        
            while currentChaine.valeur != valeur and currentChaine.valeur != None:
                currentChaine = currentChaine.suivant
            
            if currentChaine.valeur == None:
               print("votre valeur n'est pas presente dans la liste donc aucune valeur n'a etait supprimer") 
            else:
                currentChaine.valeur = currentChaine.suivant
                return True
        return False
    
    def getValeur(self,pos:int):
        longeur = self.longeur()
        if pos == None or self.tete == None: # par default ou si la liste est vide la methode add ajoute la valeur a la premiere position
            if pos != None:
                print("la liste chainee est vide")
                return None
            return self.tete.valeur
        elif pos < 1 :
            print("la postition doit etre entre 1 et " + longeur + " compris")
            return None
        else:
            currentPos = 1
            currentChaine = self.tete
        
            while currentPos != pos:
                currentChaine = currentChaine.suivant
                currentPos += 1
            
            #ici on arrive a la chaine de la position voulu
            return currentChaine.valeur
    
    def __str__(self):  
        return str(self.tete)