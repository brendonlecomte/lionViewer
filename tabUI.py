from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTabWidget, QTextBrowser, QListWidget, QTextEdit
from PyQt5.QtCore import QRect
# from PyQt5.QtWebKitWidgets import QWebViewx

class viewtab(QWidget):
    def __init__(self, parent,name,text):
        super().__init__()
        self.parent = parent
        self.initTab(name,text)

    def initTab(self,name,text):
        self.setObjectName(name)
        # self.dataTextView = QWebView(self)
        self.layout = QVBoxLayout(self)
        self.dataTextView = QTextBrowser(self)
        self.layout.addWidget(self.dataTextView) 
        self.dataTextView.setPlainText(text)


class searchTab(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.initTab()

    def initTab(self):
        self.setObjectName("Search")
        self.layout = QVBoxLayout(self)

        self.searchResult = QListWidget(self) 
        self.searchBar = QTextEdit(self)
        
        self.layout.addWidget(self.searchBar)
        self.layout.addWidget(self.searchResult)


    def resizeEvent(self, event):
        size = self.parent.size()

class tabManager(QTabWidget):
    def __init__(self):
        super().__init__()
        self.tabs =[]
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
