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
        str += "<b>{}</b> <br/>".format(obj['name'])
    if(obj.get('level') is not None):
        str += "Level: {} <br/><br/>".format(obj['level'])
    if(obj.get('magic') is not None):
        str += "Magic: {} \<br/><br/>".format(obj['magic'])
    if(obj.get('value') is not None):
        str += "Value: {} <br/><br/>".format(obj['value'])

    if(obj.get('text') is not None):
        for chunk in obj['text']:
            if(chunk is not None):
                str += "{}<br/><br/>".format(chunk)
    return str

def convertToMonster(obj):
    str =""""""
    if(obj.get('name') is not None):
        str += "<b>{}</b>".format(obj['name'])

    str += _statBlock(obj)
    str += _traits(obj)


    if(obj.get('action') is not None):
        for act in obj['action']:
            for line in act:
                if(line is not None):
                    str += "{}<br/><br/>".format(line)

    if(obj.get('text') is not None):
        for chunk in obj['text']:
            if(chunk is not None):
                str += "{}<br/><br/>".format(chunk)
    return str

def convertToItem(obj):
    str =""""""
    if(obj.get('name') is not None):
        str += "<b>{}</b> <br/>".format(obj['name'])
    if(obj.get('magic') is not None):
        str += "Magic: {} <br/>".format(obj['magic'])
    if(obj.get('value') is not None):
        str += "Value: {} <br/>".format(obj['value'])

    if(obj.get('text') is not None):
        for chunk in obj['text']:
            if(chunk is not None):
                str += "{}<br/><br/>".format(chunk)
    return 

def _statBlock(obj):
    str = """<p>"""
    if(obj.get('ac') is not None):
        str += "<b>AC</b>: {}<br/>".format(obj['ac'])
    if(obj.get('hp') is not None):
        str += "<b>HP</b>: {} <br/>".format(obj['hp'])
    if(obj.get('speed') is not None):
        str += "<b>Speed</b>: {} <br/>".format(obj['speed'])
    str += "</p>"
    return str    

def _text(text):
    str = """"""
    if(isinstance(text, list)):
        for line in text:
            if(line is not None):
                str += "{}<br/>".format(line)
    else:
        str += "{} <br/>".format(text)
    return str

def _traits(obj):
    str = """<p>"""
    if(obj.get('trait') is not None):
        traits = obj['trait']
        if(isinstance(traits, list)):
            for trait in traits:
                str += _trait(trait)
        else:
            str += _trait(traits)
        str += "</p>"
    return str

def _trait(trait):
    str ="""<p>"""
    print(trait)
    str += "<b>{}</b><br/>".format(trait['name'])
    str += _text(trait['text'])
    str+= "</p>"
    return str
