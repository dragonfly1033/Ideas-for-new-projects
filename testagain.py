#ANCHOR TASK:::::::::::::::::::::::::::::::::::::
# RPG character simulator 

# Planet of Fightcraft wants you to build character classes for their new game. 

# Each character will have the following things: 
# – Name 
# – Type (Barbarian, Elf, Wizard, Dragon, Knight)
# – Health 
# – Power
# – Special attack power 
# – Speed 
# - All characters start with 100 health 
# - Different creatures have different power ratings (B: 70, E: 30, W: 50, D: 90, K: 60) 
# - Different creatures have different special attack power ratings (B: 20, E: 60, W: 70, D: 40, K: 10)
#  - Different creatures have different speed ratings (B: 50, E: 10, W: 30, D: 50, K: 60) 

# 1. Generate a random name: en-da-fu and el-kar-tuk could be names, so you could make a name generator which sticks together three syllables from ‘word banks’ 
# 2. Create the generic character class. Test to see if you can create multiple characters 
# 3. Create subclasses corresponding to different types of creature (B, E, W, D & K) 
# 4. Make a program that randomly generates 10 of these creatures to add into a list 
# 5. Make a method in the character class that enables printing out of each character’s stats to the console 
# 6. Create a menu system that lets you add and delete characters and print out the list until you are happy with the team 
# 7. Create methods to let you edit any character’s stats and add this to your menu system 

# Extension Tasks
# 8. Create a way to save your team to a file and load it up again using SQL:  http://pythonschool.net/category/databases.html 
# 9. Add an interface using Pygame (Youtube Videos)
#ANCHOR CODE:::::::::::::::::::::::::::::::::::::
import random, sqlite3, os
#ANCHOR CLASSES:::::::::::::::::::::::::::::::::::::
class GenericCharacter:
    def __init__(self, name, hp=100, power=100, SApower=100, speed=100):
        self._name = self._makeName()
        self._hp = hp
        self._power = power
        self._SApower = SApower
        self._speed = speed
        self.type = 'Generic'

    def _makeName(self):
        valid = False
        while not valid:
            name = ''
            for i in random.choices(syllables, k=3): name += f'{i}-'
            name = name[:-1]
            print(name)
            if(name not in [member.getVal('name') for member in party]):
                valid = True
        return name

    def displayStats(self):
        print(f'::::::::::::::::::::\nName: {self._name},\nType: {self._type},\nHp: {self._hp},\nPwr: {self._power},\nSp. Atk: {self._SApower},\nSpeed: {self._speed}\n::::::::::::::::::::')

    def edit(self, stat, new):
        if(stat == '1'):
            self._name = new
        elif(stat == '2'):
            self._hp = new
        elif(stat == '3'):
            self._power = new
        elif(stat == '4'):
            self._SApower = new
        elif(stat == '5'):
            self._speed = new

    def getVal(self, attr):
        if(attr not in ['name','hp','SApower','power','speed','type']):
            print('Invalid attribute')
            raise ValueError
        else:
            if(attr == 'name'):
                return self._name
            elif(attr == 'hp'):
                return self._hp
            elif(attr == 'SApower'):
                return self._SApower
            elif(attr == 'power'):
                return self._power
            elif(attr == 'type'):
                return self._type
            elif(attr == 'speed'):
                return self._speed


class Barbarian(GenericCharacter):
    def __init__(self, power=70, SApower=20, speed=50):
        super().__init__()
        self._name = self._makeName()
        self._type = 'Barbarian'
        self._power = power
        self._SApower = SApower
        self._speed = speed

class Elf(GenericCharacter):
    def __init__(self, power=30, SApower=60, speed=10):
        super().__init__()
        self._name = self._makeName()
        self._type = 'Elf'
        self._power = power
        self._SApower = SApower
        self._speed = speed

class Wizard(GenericCharacter):
    def __init__(self, power=50, SApower=70, speed=30):
        super().__init__()
        self._name = self._makeName()
        self._type = 'Wizard'
        self._power = power
        self._SApower = SApower
        self._speed = speed

class Dragon(GenericCharacter):
    def __init__(self, power=90, SApower=40, speed=50):
        super().__init__()
        self._name = self._makeName()
        self._type = 'Dragon'
        self._power = power
        self._SApower = SApower
        self._speed = speed

class Knight(GenericCharacter):
    def __init__(self, power=60, SApower=10, speed=60):
        super().__init__()
        self._name = self._makeName()
        self._type = 'Knight'
        self._power = power
        self._SApower = SApower
        self._speed = speed


#ANCHOR SUBPROGRAMS:::::::::::::::::::::::::::::::::::::
def mainMenu():
    print(':::::::::: RPG Character Simulator ::::::::::')
    print('')
    print('Options:')
    print('Show Party (1)')
    print('Edit Party (2)')
    print('Edit Member Stats (3)')
    print('Quit (4)')

def op2Menu():
    print(':::::::Editor:::::::')
    print('What would you like to do?')
    print('Add Character (1)')
    print('Delete Character (2)')

def addMenu():
    print(':::::::Add Menu:::::::')
    print('Barbarian (1)')
    print('Elf (2)')
    print('Wizard (3)')
    print('Dragon (4)')
    print('Knight (5)')

def validate(accepted):
    valid = False
    while not valid:
        try:
            option = int(input('Enter option: '))
            if(option not in accepted):
                raise ValueError
            valid = True
        except ValueError:
            print(f'Enter valid option({str(accepted)[1:-1]})')
    return option

def addMember(typee):
    party.append(globals()[typee]())
    name = party[-1].getVal('name')
    hp = party[-1].getVal('hp')
    power = party[-1].getVal('power')
    SApower = party[-1].getVal('SApower')
    speed = party[-1].getVal('speed')

    with sqlite3.connect('party.db') as db:
        cursor = sqlite3.cursor(db)
        cursor.execute(f"INSERT INTO MEMBERS VALUES('{name}', '{hp}', '{power}', '{SApower}', '{speed}', '{typee}')")  
        db.commit()

def delMember(member):
    name = member.getVal('name')
    party.remove(member)
    with sqlite3.connect('party.db') as db:
        cursor = sqlite3.cursor(db)
        cursor.execute(f"DELETE FROM MEMBERS WHERE name='{name}'")  
        db.commit()

#ANCHOR VARIABLES/CONSTANTS:::::::::::::::::::::::::::::::::::::
syllables = ['a', 'ai', 'ame', 'an', 'ana', 'ang', 'ao', 'ba', 'bai', 'ban', 'bang', 'bao', 'be', 'bei', 'ben', 'beng', 'bi', 'bian','biang', 'biao', 'bie', 'bin', 'bing', 'bo', 'bu', 'bya', 'byo', 'byu', 'ca', 'cai', 'can', 'cang', 'cao', 'ce', 'cei', 'cen', 'ceng', 'cha', 'chai', 'chan', 'chang', 'chao', 'che', 'chen', 'cheng', 'chi', 'chong','chou', 'chu', 'chua', 'chuai', 'chuan', 'chuang', 'chui', 'chun', 'chuo', 'chya', 'chyo', 'chyu', 'ci','cong', 'cou', 'cu', 'cuan', 'cui', 'cun', 'cuo', 'da', 'dai', 'dan', 'dang', 'dao', 'de', 'dei', 'den','deng', 'deo', 'di', 'dian', 'diao', 'die', 'ding', 'diu', 'do', 'dong', 'dou', 'du', 'duan', 'dui','dun', 'duo', 'e', 'ei', 'en', 'eng', 'er', 'fa', 'fan', 'fang', 'fei', 'fen', 'feng', 'fo', 'fou', 'fu', 'ga', 'gai', 'gan', 'gang', 'gao', 'ge', 'gei', 'gen', 'geng', 'gi', 'go', 'gong', 'gou', 'gu', 'gua', 'guai', 'guan', 'guang', 'gui', 'gun', 'guo', 'gya', 'gyo', 'gyu', 'ha', 'hai', 'han', 'hang','hao', 'he', 'hei', 'hen', 'heng', 'hi', 'hiri', 'ho', 'hong', 'hou', 'hu', 'hua', 'huai', 'huan', 'huang', 'hui', 'hun', 'huo', 'hya', 'hyo', 'hyu', 'i', 'ion', 'ios', 'ji', 'jia', 'jian', 'jiang', 'jiao', 'jie', 'jin', 'jing', 'jiong', 'jiu', 'ju', 'juan', 'jue', 'jun', 'jya', 'jyo', 'jyu', 'ka','kai', 'kan', 'kang', 'kao', 'ke', 'kei', 'ken', 'keng', 'ki', 'ko', 'kong', 'kou', 'ku', 'kua', 'kuai', 'kuan', 'kuang', 'kui', 'kun', 'kuo', 'kya', 'kyo', 'kyu', 'la', 'lai', 'lan', 'lang', 'lao', 'le', 'lei','leng', 'li', 'lia', 'lian', 'liang', 'liao', 'lie', 'lin', 'ling', 'liu', 'lo', 'long', 'lou', 'lu', 'lu','luan', 'lue', 'lun', 'luo', 'ma', 'mai', 'man', 'mang', 'mao', 'me', 'mei', 'men', 'meng', 'mi', 'mian', 'miao', 'mie', 'min', 'ming', 'miu', 'mo', 'mou', 'mu', 'mui', 'mya', 'myo', 'myu', 'na', 'nai', 'nan',  'nang', 'nao', 'ne', 'nei', 'nen', 'neng', 'ni', 'nian', 'niang', 'niao', 'nie', 'nin', 'ning', 'niu', 'no', 'nong', 'nou', 'nu', 'nuan', 'nuo', 'nya', 'nyo', 'nyu', 'nü', 'nüe', 'o', 'ou', 'pa', 'pai', 'pan', 'pang', 'pao', 'pe', 'pei', 'pen', 'peng', 'pi', 'pian', 'piao', 'pie', 'pin', 'ping', 'po', 'pou', 'pu', 'pya', 'pyo', 'pyu', 'qi', 'qia', 'qian', 'qiang', 'qiao', 'qie', 'qin', 'qing',  'qiong', 'qiu', 'qu', 'quan', 'que', 'qun', 'ra', 'ran', 'rang', 'rao', 're', 'ren', 'reng', 'ri', 'ro', 'rong', 'rou', 'ru', 'rua', 'ruan', 'rui', 'run', 'ruo', 'rya', 'ryo', 'ryu', 'sa', 'sai', 'san', 'sang', 'sao', 'se', 'sen', 'seng', 'sept', 'sha', 'shai', 'shan', 'shang', 'shao', 'she', 'shei', 'shen', 'sheng', 'shi', 'shou', 'shu', 'shua', 'shuai', 'shuan', 'shuang', 'shui', 'shun', 'shuo', 'shya', 'shyo', 'shyu', 'si', 'sil', 'so', 'song', 'sou', 'su', 'suan', 'sui', 'sun', 'suo', 'ta', 'tai', 'tan', 'tang', 'tao', 'te', 'teng', 'ti', 'tian', 'tiao', 'tie', 'ting', 'to', 'tong', 'tou', 'tsu', 'tu', 'tuan', 'tui', 'tun', 'tuo', 'u', 'wa', 'wai', 'wan', 'wang', 'wei', 'wen', 'weng', 'wo', 'wu', 'xi', 'xia', 'xian', 'xiang', 'xiao', 'xie', 'xin', 'xing', 'xiong', 'xiu', 'xu', 'xuan', 'xue', 'xun', 'ya', 'yan', 'yang', 'yao', 'ye', 'yi', 'yin',  'ying', 'yo', 'yong', 'you', 'yu', 'yuan', 'yue', 'yun', 'za', 'zai', 'zan', 'zang', 'zao', 'ze', 'zei', 'zen', 'zeng', 'zha', 'zhai', 'zhan', 'zhang', 'zhao', 'zhe', 'zhei', 'zhen', 'zheng', 'zhi', 'zhong', 'zhou', 'zhu', 'zhua', 'zhuai', 'zhuan', 'zhuang', 'zhui', 'zhun', 'zhuo', 'zi', 'zo', 'zong', 'zou', 'zu', 'zuan', 'zui', 'zun', 'zuo']

party=[]

types = ['Barbarian', 'Elf', 'Wizard', 'Dragon', 'Knight']

#ANCHOR MAIN CODE:::::::::::::::::::::::::::::::::::::

if(not os.path.isfile('./party.db')):
    with s.connect('party.db') as db:
        c = s.Cursor(db)
        c.execute('CREATE TABLE MEMBERS(name text, hp integer, power integer, SApower integer, speed integer, type text)')
        db.commit()
    for i in range(10):
        randClass = random.choice(types)
        addMember(randClass)
else:


running = True
while running:
    print()
    mainMenu()
    option = validate([1,2,3,4])
    if(option == 1): #show party
        print()
        for member in party:
            member.displayStats()
            print()
    elif(option == 2): #edit party
        print()
        op2Menu()
        option = validate([1,2])
        if(option == 1): #add member
            print()
            addMenu()
            option = validate([1,2,3,4,5])
            addMember(types[option-1])
        else: #delete member
            names = [member.getVal('name') for member in party]
            print()
            print(':::::::Delete Menu:::::::')
            for index, name in enumerate(names):
                print(f'{name} ({index+1})')
            option = validate([i+1 for i in range(len(names))])
            delMember(party[option-1])

    elif(option == 3): #edit member stats
        print()
        print(':::::::Edit Character:::::::')
        names = [member.getVal('name') for member in party]
        for index, name in enumerate(names):
            print(f'{name} ({index+1})')
        option = validate([i+1 for i in range(len(names))])
        member = party[option-1]
        print()
        print(':::::Stats::::::')
        print('Name (1)\nHp (2)\nPower (3)\nSp. Atk (4)\nSpeed (5)')
        option = validate([1,2,3,4,5])
        if(option != 1): #hp, power, sp atk, speed
            valid = False
            while not valid:
                try:
                    new = int(input('Enter new value: '))
                    if(new < 0):
                        raise ValueError
                    valid = True
                except ValueError:
                    print('Enter valid positive integer.')
        else: #name
            new = input('Enter new value: ')
        member.edit(str(option), new)    

    elif(option == 4): #exit
        running = False

        

