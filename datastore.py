from tinydb import TinyDB, Query

regexSpecialCharacters = ["\\", "^", "$", ".", "|", "?", "*", "+", "(", ")"]


def strSearch(str):
    regex = str
    """prepend case insensitive flag and append wildcare for regex"""
    for char in regexSpecialCharacters:  # protect against special characters
        if(char in regex):
            # print("found {}".format(char))
            regex = regex.replace(char, "\{}".format(char))
    return "(?i).*" + regex + ".*"


class dataStore():
    def __init__(self):
        self.data = TinyDB("data/data.json")

    def runQuery(self, q):
        """execute a query"""
        return self.data.search(q)

    def getNamed(self, t, name):
        """returns an exact name match of an object.
        Used for returning exact objects"""
        q = Query()
        return self.runQuery(q.name == name)

    def findByName(self, type, name):
        """search DB by name, using case insensitive string and
        wild card after the string for completion"""
        q = Query()
        return self.runQuery(q.name.matches(strSearch(name)))

    def findByType(self, t, name=""):
        """ search for things by type (item, spell, monster) and by name.
        Name is optional. This allows searches to be a bit more complex"""
        q = Query()
        return self.runQuery((q.name.matches(strSearch(name)))
                             & (q.object_type == t))


if __name__ == '__main__':
    warehouse = dataStore()
    res = warehouse.findByName("An")
    print(len(res))
    res = warehouse.findByType("item")
    print(len(res))
    # print(res)
