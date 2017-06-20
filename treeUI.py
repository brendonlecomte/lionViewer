from PyQt5.QtWidgets import  QTreeWidget, QTreeWidgetItem


class treeView(QTreeWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("dbTreeView")
        self.headerItem().setText(0, "GM Items")
        # self.itemDoubleClicked.connect(self.clicked)

    def addGroup(self, obj):
        self.addTopLevelItem(obj)
        pass

    def addItem(self, group):
        self.addItem
        pass

class treeGroup(QTreeWidgetItem):
    def __init__(self,name):
        super().__init__(1001)
        self.setText(0, name)

class treeItem(QTreeWidgetItem):
    def __init__(self, parent, name, type=1002):
        super().__init__(parent,type)
        self.setText(0, name)
