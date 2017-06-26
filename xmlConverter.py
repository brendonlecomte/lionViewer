import xml.etree.ElementTree as ET
import xmltodict
import json 
from tinydb import TinyDB, Query

def convertXmltoDict(xmlFile):
    f = open(xmlFile, "rb")
    d = xmltodict.parse(f, xml_attribs=False)
    f.close()
    return d

def convertCompendiumToList(compendium):
    convertedList = []
    for i in compendium['compendium']:
        type=i
        for j in compendium['compendium'][i]:
            j['object_type'] = i
            convertedList.append(j)
        print("Converted: {} {}".format(len(convertedList), i))
    return convertedList
            
def databaseify(xml):
    dataBase = TinyDB("data/data.json")
    for element in xml:
        # print(json.dumps(block)) #add this to show JSON being added to DB  
        try:
            dataBase.insert(element)
        except:
            print(element.type())
    print(len(dataBase.all()))

if __name__ == '__main__':
    """This runs against the compendiums in the data folder and generates a base DB for use
    with the GM Reference tool. The data is dumped into a giant DB with a tag object_type identifying
    what kind of element it is. This makes searching for things across all types easier"""
    itemsFile = "data/Items Compendium 1.7.0.xml"
    spellsFile = "data/Spells Compendium 1.3.0.xml"
    monsterFile = "data/Bestiary Compendium 2.1.0.xml"

    itemDict = convertXmltoDict(itemsFile)
    spellDict = convertXmltoDict(spellsFile)
    monsterDict = convertXmltoDict(monsterFile)

    conList = convertCompendiumToList(itemDict)
    conList += convertCompendiumToList(spellDict)
    conList += convertCompendiumToList(monsterDict)
    databaseify(conList)
