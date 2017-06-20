spellText = """{level}: {name}
time: {time} | duration: {duration}
range: {range}
components: {components}

{text}
-----
{roll}"""

itemText = """{name}
Magic: {magic}
Value: {value}

{text}"""

monsterText = """{Name}
AC: {ac}
HP: {hp}
speed: {speed}

Str: {str} | Dex: {dex} | Con: {con}
Int: {int} | Wis: {wis} | Cha: {cha}

Actions:
{action}

{text}"""


def convertToSpell(obj):
    str =""""""
    if(obj.get('name') is not None):
        str += "{} \n".format(obj['name'])
    if(obj.get('magic') is not None):
        str += "Magic: {} \n".format(obj['magic'])
    if(obj.get('value') is not None):
        str += "Value: {} \n".format(obj['value'])

    if(obj.get('text') is not None):
        for chunk in obj['text']:
            if(chunk is not None):
                str += "{}\n\n".format(chunk)
    return str

def convertToMonster(obj):
    str =""""""
    if(obj.get('name') is not None):
        str += "{} \n".format(obj['name'])
    if(obj.get('ac') is not None):
        str += "AC: {} \n".format(obj['ac'])
    if(obj.get('hp') is not None):
        str += "HP: {} \n".format(obj['hp'])
    if(obj.get('speed') is not None):
        str += "Speed: {} \n".format(obj['speed'])

    if(obj.get('action') is not None):
        for chunk in obj['action']:
            if(chunk is not None):
                str += "{}\n\n".format(chunk)

    if(obj.get('text') is not None):
        for chunk in obj['text']:
            if(chunk is not None):
                str += "{}\n\n".format(chunk)
    return str

def convertToItem(obj):
    str =""""""
    if(obj.get('name') is not None):
        str += "{} \n".format(obj['name'])
    if(obj.get('magic') is not None):
        str += "Magic: {} \n".format(obj['magic'])
    if(obj.get('value') is not None):
        str += "Value: {} \n".format(obj['value'])

    if(obj.get('text') is not None):
        for chunk in obj['text']:
            if(chunk is not None):
                str += "{}\n\n".format(chunk)
    return str