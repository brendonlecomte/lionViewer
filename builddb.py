from tinydb import TinyDB, Query
import xmlConverter

pathToDB = "test.db"
xmlFile = "test.xml"


def openOrCreateDb(path):
    db = TinyDB(path)
    return db


def populateSpellsDb():
    xmlFile = "data/Spells Compendium 1.3.0.xml"
    dbFile = "data/spells.db"
    db = openOrCreateDb(dbFile)
    xmlObjs = xmlConverter.compendiumByType(xmlFile, 'spell')
    for i in xmlObjs:
        db.insert(i)
    print("{} Succesfully added to {}".format(len(db.all()),dbFile))

def populateItemDb():
    xmlFile = "data/Items Compendium 1.7.0.xml"
    dbFile = "data/items.db"
    db = openOrCreateDb(dbFile)
    xmlObjs = xmlConverter.compendiumByType(xmlFile, 'item')
    for i in xmlObjs:
        db.insert(i)
    print("{} Succesfully added to {}".format(len(db.all()),dbFile))

def populateMonsterDb():
    xmlFile = "data/Bestiary Compendium 2.1.0.xml"
    dbFile = "data/monsters.db"
    db = openOrCreateDb(dbFile)
    xmlObjs = xmlConverter.compendiumByType(xmlFile, 'monster')
    for i in xmlObjs:
        db.insert(i)
    print("{} Succesfully added to {}".format(len(db.all()),dbFile))

if __name__ == '__main__':
    print("Creating all DB's from data")
    populateMonsterDb()
    populateItemDb()
    populateSpellsDb()
    print("----------------------------")


