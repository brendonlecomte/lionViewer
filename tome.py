#!/python
import sys
import json
from datastore import dataStore
from treeUI import treeGroup, treeItem, treeView
from convertToReadable import *
from tabUI import tabManager
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QHBoxLayout
from PyQt5.QtGui import QPixmap, QIcon

types={"Races":'race',
        "Spells":'spell',
        "Items":'item',
        "Classes":'class',
        "Feats":'feat',
        "Monsters":'monster',
        "Backgrounds":'background'
        }

conversions = {'item':convertToItem,
                'monster':convertToMonster,
                'spell':convertToSpell,
                'race' : convertToRace,
                'background': convertToBackground,
                'feat':convertToFeat,
                'class':convertToClass}

class Controller(QObject):
    """interface between DB and the UI"""
    def __init__(self):
        super().__init__()
        self.warehouse = dataStore()

    def getObject(self, t, name):
        """gets an exact named object"""
        return self.warehouse.findByType(t, name)

    def getExact(self, t, name):
        return self.warehouse.getNamed(t, name)

    def convertToUI(self, obj):
        if(len(obj) == 0):
            return ""
        text = conversions[obj[0]['object_type']](obj[0])
        return text

    def search(self, name):
        return self.warehouse.findByName("*",name)

    def getItems(self):
        return self.warehouse.findByType("item")

    def getSpells(self):
        return self.warehouse.findByType("spell")

    def getMonsters(self):
        return self.warehouse.findByType("monster")
    
    def getRaces(self):
        return self.warehouse.findByType("race")
    
    def getFeats(self):
        return self.warehouse.findByType("feat")
    
    def getBackgrounds(self):
        return self.warehouse.findByType("background")
    
    def getClasses(self):
        clss = self.warehouse.findByType("class")
        return clss


class GMWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = Controller() #controller
        self.initUI()
        self.dbTreeView.itemDoubleClicked.connect(self.openItem)

    
    def initTrees(self):
        items = self.controller.getItems()
        print("Items found: {}".format(len(items)))
        self.addToTree(self.itemGroup, items)

        monsters = self.controller.getMonsters()
        print("Monsters found: {}".format(len(monsters)))
        self.addToTree(self.monsterGroup, monsters)

        spells = self.controller.getSpells()
        print("Spells found: {}".format(len(spells)))
        self.addToTree(self.spellGroup, spells)

        races = self.controller.getRaces()
        print("Races found: {}".format(len(races)))
        self.addToTree(self.raceGroup, races)

        feats = self.controller.getFeats()
        print("Feats found: {}".format(len(feats)))
        self.addToTree(self.featGroup, feats)

        backgrounds = self.controller.getBackgrounds()
        print("Backgrounds found: {}".format(len(backgrounds)))
        self.addToTree(self.backgroundGroup, backgrounds)

        classes = self.controller.getClasses()
        print("Classes found: {}".format(len(classes)))
        self.addToTree(self.classGroup, classes)

    def addToTree(self, group, items):
        for item in items:
            treeItem(group, item['name'])

    def initUI(self):
        self.resize(500, 500)
        screen = QDesktopWidget().screenGeometry()
        # self.setMaximumSize(screen.width()/2,screen.height()/2) #reconsider this....
        self.center()
        self.layout = QHBoxLayout(self)
        self.setWindowTitle("Tome of Knowledge")
        self.dbTreeView = treeView()
        self.layout.addWidget(self.dbTreeView)

        self.seachOption = treeItem(None,"Search",type=1003)
        self.itemGroup = treeGroup("Items")
        self.monsterGroup = treeGroup("Monsters")
        self.spellGroup = treeGroup("Spells")
        self.raceGroup = treeGroup("Races")
        self.backgroundGroup = treeGroup("Backgrounds")
        self.featGroup = treeGroup("Feats")
        self.classGroup = treeGroup("Classes")

        self.initTrees()
        self.dbTreeView.addGroup(self.seachOption)
        self.dbTreeView.addGroup(self.monsterGroup)
        self.dbTreeView.addGroup(self.itemGroup)
        self.dbTreeView.addGroup(self.spellGroup)
        self.dbTreeView.addGroup(self.raceGroup)
        self.dbTreeView.addGroup(self.backgroundGroup)
        self.dbTreeView.addGroup(self.featGroup)
        self.dbTreeView.addGroup(self.classGroup)

        self.dataTabView = tabManager(self.controller)
        self.layout.addWidget(self.dataTabView)
        self.layout.setStretch(0,10)
        self.layout.setStretch(1,40)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def openItem(self,item, column):
        if(item.type() == 1002):
            name = item.text(0)
            parent = item.parent().text(0)
            selectedType = types[parent]
            obj = self.controller.getObject(selectedType,name)
            text = self.controller.convertToUI(obj)
            self.dataTabView.openTab(name, text)

        if(item.type() == 1003): #open search tab
            self.dataTabView.openSearch()

    def keyPressEvent(self, event):
        # print("Key pressed {} ".format(event.key()))
        if(event.key() == 87):
            self.dataTabView.closeCurrent()
            
if __name__ == '__main__':
    app = QApplication(sys.argv) #QT application  
    app.setWindowIcon(QIcon('icon_tome.ico'))      
    gmMainWindow = GMWindow() #view


    sys.exit(app.exec_())