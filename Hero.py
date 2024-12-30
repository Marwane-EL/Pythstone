class hero:
    def init(self, name, imgPath, hp, hand):
        self.name = name
        self.imgPath = imgPath
        self.hp == hp
        self.hand = hand


    def getName(self):
        print('le nom du hero est ' + self.name)
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