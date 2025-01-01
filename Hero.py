class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.imgPath = None
        self.hp = hp

    def getName(self):
        return self.name

    def getImgPath(self):
        print('le nom du hero est ' + self.name)
        return self.imgPath

    def setName(self, nvNom):
        oldName = self.name
        self.name = nvNom
        print('le nom du hero a ete change de ' + oldName + ' a ' + self.name)

    def setImgPath(self):
        print('le nom du hero est ' + self.name)
        return self.name

