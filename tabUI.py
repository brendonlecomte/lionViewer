from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTabWidget, QTextBrowser, QListWidget, QTextEdit
from PyQt5.QtCore import QRect
import json
# from PyQt5.QtWebKitWidgets import QWebViewx

class viewtab(QWidget):
    def __init__(self, parent,name,text):
        super().__init__()
        self.parent = parent
        self._initTab(name,text)

    def _initTab(self,name,text):
        self.setObjectName(name)
        self.layout = QVBoxLayout(self)
        self.dataTextView = QTextBrowser(self)
        self.layout.addWidget(self.dataTextView) 
        self.dataTextView.insertHtml(text)


class searchTab(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self._initTab()

    def _initTab(self):
        self.setObjectName("Search")
        self.layout = QVBoxLayout(self)
        self.searchResult = QListWidget(self) 
        self.searchBar = QTextEdit(self)
        self.searchBar.textChanged.connect(self._textChanged)
        self.searchResult.doubleClicked.connect(self._open)
        self.layout.addWidget(self.searchBar)
        self.layout.addWidget(self.searchResult)

    def _textChanged(self):
        text = self.searchBar.toPlainText()
        self.searchResult.clear()
        if text is not "":
            print(text)
            res = self.parent.controller.search(text)
            for i in res:
                self.searchResult.addItem(i['name'])

    def _open(self):
        name = self.searchResult.currentItem().text()
        obj = self.parent.controller.getObject(name)
        text = json.dumps(obj[0])
        self.parent.openTab(name, text)

    def resizeEvent(self, event):
        size = self.parent.size()


class tabManager(QTabWidget):
    def __init__(self, controller):
        super().__init__()
        self.tabs =[]
        self.controller = controller
        self.setTabsClosable(True)
        self.setObjectName("dataTabView")
        self.tabCloseRequested.connect(self.closeTab)

    def closeTab(self, index):
        self.removeTab(index)

    def openTab(self,name,text):
        newTab = viewtab(self,name,text)
        self.addTab(newTab, name)
        self.setCurrentWidget(newTab)

    def openSearch(self):
        newTab = searchTab(self)
        self.addTab(newTab, "Search")
        self.setCurrentWidget(newTab)
