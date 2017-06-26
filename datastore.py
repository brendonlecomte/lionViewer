from tinydb import TinyDB, Query

def strSearch(str):
    """prepend case insensitive flag and append wildcare for regex"""
    return "(?i)" + str + ".*"

class dataStore():
    def __init__(self):
        self.data = TinyDB("data/data.json")

    def runQuery(self, q):
        """execute a query"""
        return self.data.search(q)
       
    def getNamed(self, name):
        """returns an exact name match of an object. Used for returning exact objects"""
        q = Query()
        return self.runQuery(q.name == name)

    def findByName(self, name):
        """search DB by name, using case insensitive string and 
        wild card after the string for completion"""
        q = Query()
        return self.runQuery(q.name.matches(strSearch(name))) 

    def findByType(self, type, name=""):
        """ search for things by type (item, spell, monster) and by name.
        Name is optional. This allows searches to be a bit more complex"""
        q = Query()
        return self.runQuery((q.name.matches(strSearch(name))) & (q.object_type == type))


if __name__ == '__main__':
    warehouse = dataStore()
    res = warehouse.findByName("An")
    print(len(res))
    res = warehouse.findByType("item")
    print(len(res))
    # print(res)