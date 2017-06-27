#!/python
import sys
import json
from datastore import dataStore
from treeUI import treeGroup, treeItem, treeView
from convertToReadable import convertToItem, convertToMonster, convertToSpell
from tabUI import tabManager
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QHBoxLayout

class Controller(QObject):
    """interface between DB and the UI"""
    def __init__(self):
        super().__init__()
        self.warehouse = dataStore()
        self.itemSelected = pyqtSignal(str)

    def getObject(self, name):
        """gets an exact named object"""
        obj = self.warehouse.getNamed(name)
        return obj

    def search(self, name):
        return self.warehouse.findByName(name)

    def getItems(self):
        return self.warehouse.findByType("item")

    def getSpells(self):
        return self.warehouse.findByType("spell")

    def getMonsters(self):
        return self.warehouse.findByType("monster")



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

    def addToTree(self, group, items):
        for item in items:
            treeItem(group, item['name'])

    def initUI(self):
        self.resize(500, 500)
        self.center()
        self.layout = QHBoxLayout(self)
        self.setWindowTitle("World Viewer")
        self.dbTreeView = treeView()
        self.layout.addWidget(self.dbTreeView)

        self.seachOption = treeItem(None,"Search",type=1003)
        self.itemGroup = treeGroup("Items")
        self.monsterGroup = treeGroup("Monsters")
        self.spellGroup = treeGroup("Spells")

        self.initTrees()
        self.dbTreeView.addGroup(self.seachOption)
        self.dbTreeView.addGroup(self.monsterGroup)
        self.dbTreeView.addGroup(self.itemGroup)
        self.dbTreeView.addGroup(self.spellGroup)

        self.dataTabView = tabManager(self.controller)
        self.layout.addWidget(self.dataTabView)
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
            tab = self.controller.getObject(name)
            if(parent == 'Items'):
                text = convertToItem(tab[0])
            elif(parent == 'Monsters'):
                text = convertToMonster(tab[0])
            elif(parent == 'Spells'):
                text = convertToSpell(tab[0])
            else:
                text = json.dumps(tab[0])
            self.dataTabView.openTab(name, text)
        if(item.type() == 1003): #open search tab
            self.dataTabView.openSearch()


if __name__ == '__main__':
    app = QApplication(sys.argv) #QT application
    gmMainWindow = GMWindow() #view


    sys.exit(app.exec_())