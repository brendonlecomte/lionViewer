#!/python
import sys
import json
from datastore import dataStore
from treeUI import treeGroup, treeItem, treeView
from convertToReadable import convertToItem
from tabUI import tabManager
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QHBoxLayout

class Controller(QObject):
    def __init__(self):
        super().__init__()
        self.warehouse = dataStore()
        self.itemSelected = pyqtSignal(str)

    def openTab(self, group, name):
        obj = self.warehouse.find(name)
        return obj

    def getAllStore(self, store):
        return self.warehouse.getByStore(store)

class GMWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = Controller() #controller
        self.initUI()   
        # self.controller = Controller() #controller
        self.dbTreeView.itemDoubleClicked.connect(self.openItem)
    
    def initTrees(self):
        items = self.controller.getAllStore('Items')
        print(len(items))
        for i in items:
            itm = treeItem(self.itemGroup, i['name'])

        monst = self.controller.getAllStore('Monsters')
        print(len(monst))
        for j in monst:
            itm = treeItem(self.monsterGroup, j['name'])
        spell = self.controller.getAllStore('Spells')
        print(len(spell))
        for k in spell:
            itm = treeItem(self.spellGroup, k['name'])

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
            tab = self.controller.openTab(parent,name)
            if(parent == 'Items'):
                text = convertToItem(tab[0])
            else:
                text = json.dumps(tab[0])
            self.dataTabView.openTab(name, text)
        if(item.type() == 1003): #open search tab
            self.dataTabView.openSearch()


if __name__ == '__main__':
    app = QApplication(sys.argv) #QT application
    gmMainWindow = GMWindow() #view


    sys.exit(app.exec_())