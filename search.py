from datastore import dataStore
from tinydb import Query

class Search():
    def __init__(self):
        self.warehouse = dataStore()


    def search(self,text):
        q = Query()
        return self.warehouse.runQuery(q.name.matches(text+'*'))


if __name__ == '__main__':
    s = Search()

    test = "Burnt Oth"
    print(s.search(test))
