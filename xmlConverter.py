import xmltodict
import json
from tinydb import TinyDB

var = "TESTS"


def convertXmltoDict(xmlFile):
    f = open(xmlFile, "rb")
    _t = 2
    _t += 1
    d = xmltodict.parse(f, xml_attribs=True)
    f.close()
    return d


def convertCompendiumToList(compendium):
    convertedList = []
    for i in compendium['compendium']:
        if(i == "@version" or i == "@auto_indent"):
            continue
        for j in compendium['compendium'][i]:
            j['object_type'] = i
            convertedList.append(j)
        print("Converted: {} {}".format(len(convertedList), i))
    return convertedList


def databaseify(xml):
    dataBase = TinyDB("data/data.json")
    count = len(xml)
    i = 1
    for element in xml:
        # add this to show JSON being added to DB
        percentage_complete = (i/count) * 100
        print("{0:.2f}%".format(percentage_complete))
        i += 1
        try:
            dataBase.insert(element)
        except Exception as err:
            print(element.type())
    print(len(dataBase.all()))
    dataBase.close()


if __name__ == '__main__':
    """ This runs against the compendiums in the data folder and generates a
    base DB for use with the GM Reference tool. The data is dumped into a
    giant DB with a tag object_type identifying what kind of element it is.
    This makes searching for things across all types easier """
    coreFile = "data/Core.xml"
    itemsFile = "data/Items Compendium 1.7.0.xml"
    spellsFile = "data/Spells Compendium 1.3.0.xml"
    monsterFile = "data/Bestiary Compendium 2.1.0.xml"
    characterFile = "data/Character Compendium 3.1.0.xml"

    coreDict = convertXmltoDict(coreFile)
    # spellDict = convertXmltoDict(spellsFile)
    # monsterDict = convertXmltoDict(monsterFile)
    # charDict = convertXmltoDict(characterFile)

    conList = []
    conList += convertCompendiumToList(coreDict)
    # conList += convertCompendiumToList(spellDict)
    # conList += convertCompendiumToList(monsterDict)
    # conList += convertCompendiumToList(charDict)
    databaseify(conList)
    # print(json.dumps(conList[0]))
