from tinydb import TinyDB, Query

class dataStore():
    def __init__(self):
        self.stores = {}
        self.addStore('Items',"data/items.db")
        self.addStore('Monsters',"data/monsters.db")
        self.addStore('Spells',"data/spells.db")


    def addStore(self, name, storePath):
        self.stores[name] = (TinyDB(storePath))

    def find(self, name):
        q = Query()
        res = []
        for storeName in self.stores:
            out = self.stores[storeName].search(q.name == name)
            if(out is not None):
                res += out
        return res


    def runQuery(self, q):
        res = []
        for storeName in self.stores:
            out = self.stores[storeName].search(q)
            if(out is not None):
                res += out
        return res

    def findByName(self, store, name):
        q = Query()
        return self.stores[store].search(q.name == name)

    def getByStore(self, store):
        return self.stores[store].all()

if __name__ == '__main__':
    warehouse = dataStore()
    res = warehouse.findByName('Items',"Burnt Othur Fumes (Inhaled)")
    print(len(res))
    print(res)