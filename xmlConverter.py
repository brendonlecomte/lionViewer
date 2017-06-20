import xml.etree.ElementTree as ET
import xmltodict
import json 

def convertXmltoDict(xmlFile):
    f = open(xmlFile, "rb")
    d = xmltodict.parse(f, xml_attribs=False)
    f.close()
    return d

def itemToDict(xmlFile):
    ''' based on current format of item compendium for 5e Lionsden app'''
    items = convertXmltoDict(xmlFile)['compendium']['item']
    return items

def spellsToDict(xmlFile):
    ''' based on current format of spells compendium for 5e Lionsden app'''
    spells = convertXmltoDict(xmlFile)['compendium']['spell']
    return spells

def monsterToDict(xmlFile):
    ''' based on current format of monster compendium for 5e Lionsden app'''
    monsters = convertXmltoDict(xmlFile)['compendium']['monster']
    return monsters

def compendiumByType(xmlFile, type):
    return convertXmltoDict(xmlFile)['compendium'][type]

def xmlToJson(xml):
    return json.dumps(xml)

if __name__ == '__main__':
    items = itemToDict(xml_file)
    # print(len(items))

    print(json.dumps(items[0]))

