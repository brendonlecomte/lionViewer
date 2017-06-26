from tinydb import TinyDB, Query

def strSearch(str):
    return "(?i)" + str + ".*"

class dataStore():
    def __init__(self):
        self.data = TinyDB("data/data.json")

    def runQuery(self, q):
        return self.data.search(q)
       
    def getNamed(self, name):
        q = Query()
        return self.runQuery(q.name == name)

    def findByName(self, name):
        q = Query()
        return self.runQuery(q.name.matches(strSearch(name))) 

    def findByType(self, type, name=""):
        q = Query()
        return self.runQuery((q.name.matches(strSearch(name))) & (q.object_type == type))


if __name__ == '__main__':
    warehouse = dataStore()
    res = warehouse.findByName("An")
    print(len(res))
    res = warehouse.findByType("item")
    print(len(res))
    # print(res)