schoolsOfMagic = {'A': 'Abjuration',
                  'T': 'Transmutation',
                  'EV': 'Evocation',
                  'EN': 'Enchantment',
                  'D': 'Divination',
                  'C': 'Cantrip',
                  'N': 'Necromancy',
                  'I': 'Illusion'}

level_tags = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']

def convertToFeat(obj):
    str =""""""
    if(obj.get('name') is not None):
        str += "<b>{}</b> <br/>".format(obj['name'])
    str += _text(obj)
    return str

def convertToRace(obj):
    str =""""""
    if(obj.get('name') is not None):
        str += "<b>{}</b> <br/>".format(obj['name'])
    if(obj.get('size') is not None):
        str += "<b>Size:</b> {} <br/>".format(obj['size'])
    if(obj.get('speed') is not None):
        str += "<b>Speed:</b> {} <br/>".format(obj['speed'])
    if(obj.get('ability') is not None):
        str += "<b>Stats:</b> {} <br/>".format(obj['ability'])
    str += _traits(obj)
    str += _text(obj)
    return str

def convertToBackground(obj):
    str =""""""
    if(obj.get('name') is not None):
        str += "<b>{}</b> <br/>".format(obj['name'])
    str += _traits(obj)
    str += _text(obj)
    return str

def convertToClass(obj):
    # print(obj)s
    str =""""""
    if(obj.get('name') is not None):
        str += "<b>{}</b> <br/>".format(obj['name'])
    if(obj.get('hd') is not None):
        str += "<b>Hit Dice:</b> 1d{} <br/>".format(obj['hd'])
    if(obj.get('proficiency') is not None):
        str += "<b>Saving Throws:</b> {} <br/>".format(obj['proficiency'])
    for lvl in level_tags:
        print("{}".format( lvl))
        # str += "------------- Level {} --------------".format(lvl)
        for x in obj['autolevel']:
            if(obj.get('@level') is not None):
                l = obj['@level']
                print("{} - {}".format(l, lvl))
                if(l is not lvl):
                    continue
            
            if(x.get('slots') is not None):
                str += x['slots']
            elif(x.get('feature') is not None):
                str += _feature(x)
        # "-------------------------------------"
    str += _text(obj)
    return str

def convertToSpell(obj):
    str =""""""
    if(obj.get('name') is not None):
        str += "<b>{}</b> <br/>".format(obj['name'])
    if(obj.get('level') is not None):
        str += "<b>Level</b>: {} <br/>".format(obj['level'])
    if(obj.get('school') is not None):
        str += "<b>School</b>: {}<br/><br/>".format(schoolsOfMagic[obj['school']])
    if(obj.get('time') is not None):
        str += "<b>Time</b>: {} <br/>".format(obj['time'])
    if(obj.get('range') is not None):
        str += "<b>Range</b>: {} <br/>".format(obj['range'])
    if(obj.get('component') is not None):
        str += "<b>Component</b>: {} <br/>".format(obj['component'])
    if(obj.get('duration') is not None):
        str += "<b>Duration</b>: {} <br/>".format(obj['duration'])
    str += _text(obj)
    return str

def convertToMonster(obj):
    str =""""""
    if(obj.get('name') is not None):
        str += "<b>{}</b>".format(obj['name'])

    str += _statBlock(obj)
    str += _traits(obj)
    str += _actions(obj)

    str += _text(obj)
    return str

def convertToItem(obj):
    str =""""""
    if(obj.get('name') is not None):
        str += "<b>{}</b> <br/>".format(obj['name'])
    if(obj.get('magic') is not None and obj.get('magic') == '1'):
        str += "<b>Magical</b><br/>"
    if(obj.get('value') is not None):
        str += "<b>Value</b>: {} <br/>".format(obj['value'])
    str +=  _text(obj)
    return str

def _feature(obj):
    str = """<p>"""
    if(obj.get('feature') is not None):
        features = obj['feature']
        for f in features:
            try:
                if(f.get('name') is not None):
                    str += "<b>{}</b> <br/>".format(f['name'])
                str += _text(f)
            except:
                pass
    str += "</p>"
    return str

def _statBlock(obj):
    str = """<p>"""

    if(obj.get('cr') is not None):
        str += "<b>CR</b>: {}<br/>".format(obj['cr'])
    
    if(obj.get('ac') is not None):
        str += "<b>AC</b>: {}<br/>".format(obj['ac'])
    if(obj.get('hp') is not None):
        str += "<b>HP</b>: {} <br/>".format(obj['hp'])
    if(obj.get('speed') is not None):
        str += "<b>Speed</b>: {} <br/>".format(obj['speed'])

    str+= "<b>STR</b>:{}    <b>DEX</b>:{}   <b>CON</b>:{}<br/>".format(obj['str'],obj['dex'],obj['con'])
    str+= "<b>INT</b>:{}    <b>WIS</b>:{}   <b>CHA</b>:{}".format(obj['int'],obj['wis'],obj['cha'])
    str += "</p>"
    return str    

def _text(obj):
    str = """<p>"""
    if(obj.get('text') is not None):
        text = obj['text']
        if(isinstance(text, list)):
            for line in text:
                if(line is not None):
                    str += "{}<br/>".format(line)
        else:
            str += "{} <br/>".format(text)
    return str +"</p>"

def _roll(obj):
    str = """<p><b>Rolls</b>:"""
    if(obj.get('roll') is not None):
        rolls = obj['roll']
        if(isinstance(rolls, list)):
            for roll in rolls:
                str += "{},".format(roll)
        else:
            str += "{}".format(rolls)
        str += "</p>"
    else:
        str = ""
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
    str += "<b>{}:</b>".format(trait['name'])
    str += _text(trait)
    str+= "</p>"
    return str

def _actions(obj):
    str = """<p>"""
    if(obj.get('action') is not None):
        actions = obj['action']
        if(isinstance(actions, list)):
            for action in actions:
                str += _action(action)
        else:
            str += _action(actions)
        str += "</p>"
    return str

def _action(action):
    str ="""<p>"""
    str += "<b>{}</b><br/>".format(action['name'])
    str += _text(action)
    if(action.get('attack' is not None)):
        str += "{}".format(action['attack'])
    str+= "</p>"
    return str

if __name__ == '__main__':
    t =  {'feature': [{'name': 'Starting Proficiencies','text': ['You are proficient with the following items, in addition to any proficiencies provided by your race or background.', 'Armor: light armor, medium armor, shields', 'Weapons: simple weapons, martial weapons', 'Tools: none', 'Skills: Choose two from Animal Handling, Athletics, Intimidation, Nature, Perception, and Survival']},{'name': 'Starting Equipment', 'text': ['You start with the following items, plus anything provided by your background.', None, '• (a) a greataxe or (b) any martial melee weapon', '• (a) two handaxes or (b) any simple weapon', "• An explorer's pack, and four javelins", None, 'Alternatively, you may start with 2d4 x 10 gp to buy your own equipment.']}]}
    print(_feature(t))