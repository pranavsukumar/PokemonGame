import random
class Pokemon(object):
    def __init__(self, name, hp, ap):
        self.name = name
        self.hp = hp
        self.ap = ap
        self.attacks = {}
        self.maxHP = hp
    def __str__(self):
        return self.name + " " + str(self.hp) + "HP, " +  str(self.ap) + "AP"
    def getPokemonName(self):
        return self.name
    def isDead(self):
        return self.hp <= 0
    def get_attack_power(self):
        return self.ap
    def getAttacks(self):
        return self.attacks
    def getAttackNames(self):
        x = []
        for item in self.attacks:
            x.append(item)
        return x
    def attack(self, p, a):
        pp = self.attacks[a][0]
        attackPower = (pp+ self.get_attack_power()) / 2
        p.take_damage(attackPower)
    def take_damage(self, x):
        self.hp -= x
        if self.hp < 0:
            self.hp = 0
    def heal(self):
        self.hp += 20
        if self.hp > self.maxHP:
            self.hp = self.maxHP
    def pickChoice(self):
        while True:
            choice = raw_input("Do you want to: Attack, Heal, Switch?")
            if (choice == "Attack") and (not(self.isDead())):
                break
            if (choice == "Heal") and (not(self.isDead())):
                break
            if choice == "Switch":
                break
        return choice

class Grass(Pokemon):
    def __init__(self, name, hp, ap):
        Pokemon.__init__(self, name, hp, ap)
        self.attacks = {"Leaf Storm":[ 130, 90], "Mega Drain" : [50, 100], "Razor Leaf" : [55, 95]}

class Fire(Pokemon):
    def __init__(self, name, hp, ap):
        Pokemon.__init__(self, name, hp, ap)
        self.attacks = {"Ember" : [60, 100], "Fire Punch": [85, 80], "Flame Wheel" : [70, 99]}

class Water(Pokemon):
    def __init__(self, name, hp, ap):
        Pokemon.__init__(self, name, hp, ap)
        self.attacks = {"Bubble" : [40, 100], "Hydro Pump" : [185, 30], "Surf" : [70, 99]}

class User(object):
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.activePokemonIndex = -1
    def __str__(self):
        return self.name
    def getName(self):
        return self.name
    def attack(self):
        pass
    def heal(self):
        pass
    def add_pokemon(self, p):
        if p not in self.hand:
            (self.hand).append(p)
        else:
            return False
    def list_pokemon(self):
        x = []
        for item in self.hand:
            x.append(item.getPokemonName())
        return x
    def make_active_pokemon(self, n):
        if (n >= 0) and (n < len(self.hand)):
            self.activePokemonIndex = n
        else:
            print "Error in setting active Pokemon. Index out of bounds..."
    def get_active_pokemon(self):
        return self.hand[self.activePokemonIndex]
    def stats(self):
        i = 1
        for item in self.hand:
            print i, item
            i += 1
    def switch(self, n):
        self.stats()
        self.make_active_pokemon(n)
        return self.get_active_pokemon()
    def pokemon_to_activate(self):
        print "\nAvailable Pokemon's to activate/switch are:"
        self.stats()
        while True:
            choice = input("\nWhich Pokemon do you want to activate: 1, 2, or 3 ?")
            if (choice >= 1) and (choice <= 3):
                break
        return choice
    def is_end_game(self):
        for item in self.hand:
            if not(item.isDead()):
                return False
        return True

class Computer(User):
    def __init__(self, name):
        User.__init__(self, name)
    def switch(self):
        while True:
            self.make_active_pokemon(random.randint(0,2))
            if not (self.get_active_pokemon().isDead()):
                break

def pokemon_dict():
    bulbasoar = Grass("Bulbasoar", 60, 40)
    bellsprout = Grass("Bellsprout", 40, 60)
    oddish = Grass("Oddish", 50, 50)
    charmainder = Fire("Charmainder", 25, 70)
    ninetails = Fire("Ninetails", 30, 50)
    ponyta = Fire("Ponyta", 40, 60)
    squirtle = Water("Squirtle", 80, 20)
    psyduck = Water("Psyduck", 70, 40)
    polywag = Water("Polywag", 50, 50)
    return {1:bulbasoar, 2:bellsprout, 3:oddish, 4:charmainder, 5:ninetails, 6:ponyta, 7:squirtle, 8:psyduck, 9:polywag}

def pick_number(n,maxNum,pickList):
    while True:
        i = input("Choose Pokemon #" + str (n) + ": ")
        if (i in pickList) or (i <= 0) or (i > maxNum):
            print "Wrong input. Try Again..."
        else:
            return i
            break

def create_u_c():
    u1 = raw_input("What is the user's name?")
    c1 = raw_input("What is the computer's name?")
    u = User(u1)
    c = Computer(c1)
    print "The user's name is ", u
    print "The computer's name is ", c
    d = pokemon_dict()
    l = len(d)
    count = 1
    print "\nAvailable Pokemon:"
    for key in d:
        print str(count) + " ", (d[key])
        count +=1
    pl = []
    for x in range(1,4):
        up = pick_number(x, l, pl)
        u.add_pokemon(d[up])
        pl.append(up)
    for x in range(1,4):
        while True:
            cp = random.randint(1,l)
            if not ((cp in pl) or (cp <= 0) or (cp > l)):
                break
        c.add_pokemon(d[cp])
        pl.append(cp)
    print "\n" + u.getName() + "'s pokemon are:"
    u.stats()
    print "\n" + c.getName() + "'s pokemon are:"
    c.stats()
    activeChoiceU = u.pokemon_to_activate() - 1
    activeChoiceC = random.randint(0,2)
    u.make_active_pokemon(activeChoiceU)
    c.make_active_pokemon(activeChoiceC)
    print u.getName() + "'s active pokemon is: " + u.get_active_pokemon().getPokemonName()
    print c.getName() + "'s active pokemon is: " + c.get_active_pokemon().getPokemonName()
    return [u,c]

def game_loop():
    players = create_u_c()
    u = players[0]
    c = players[1]
    u1 = u.getName()
    c1 = c.getName()
    while True:
        print "\n"
        if not(u.is_end_game()):
            uap = u.get_active_pokemon()
            cap = c.get_active_pokemon()
            uChoice = uap.pickChoice()
            if uChoice == "Attack":
                print str(uap) + "   is attacking    " + str(cap)
                print uap.getAttacks()
                while True:
                    a = raw_input("What attack do you want?")
                    if a in uap.getAttackNames() :
                       break
                uap.attack(cap, a)
                print u1 + "'s stats after attack: " + str(uap)
                print c1 + "'s stats after attack: " + str(cap)
            elif uChoice == "Heal":
                print str(uap) + "   is healing"
                uap.heal()
                print u1 + "'s stats after heal: " + str(uap)
            elif uChoice == "Switch":
                print str(uap) + "   is switching"
                switchValue = u.pokemon_to_activate() - 1
                u.switch(switchValue)
                uap = u.get_active_pokemon()
                print u1 + "'s active pokemon is now " + str(uap)
        else:
            break
        if not(c.is_end_game()):
            uap = u.get_active_pokemon()
            cap = c.get_active_pokemon()
            cChoice = random.randint(1,6)
            if (cap.isDead()) or (cChoice == 1):
                if (cap.isDead()):
                    print str(cap) + " has fainted and is switching"
                else:
                    print str(cap) + "   is switching"
                c.switch()
                cap = c.get_active_pokemon()
                print c1 + "'s active pokemon is now " + str(cap)
            elif cChoice <= 2:
                print str(cap) + "   is healing"
                cap.heal()
                print c1 + "'s stats after heal: " + str(cap)
            elif cChoice >=3:
                print str(cap) + "   is attacking    " + str(uap)
                listOfAttacksComputer = cap.getAttackNames()
                computerAttackChoice = random.randint(0,2)
                computerPick = listOfAttacksComputer[computerAttackChoice]
                cap.attack(uap, computerPick)
                print c1 + " is using: ", computerPick
                print c1 + "'s stats after attack: " + str(cap)
                print u1 + "'s stats after attack: " + str(uap)
        else:
            break
    print "Game Over..."
    print u1 + "'s stats:"
    u.stats()
    print c1 + "'s stats:"
    c.stats()
    if u.is_end_game():
        print c1 + " Wins!"
    elif c.is_end_game():
        print u1 + " Wins!"

game_loop()

"""
print "Testing Pokemon creation..."
bulbasoar = Grass("Bulbasoar", 60, 40)
bellsprout = Grass("Bellsprout", 40, 60)
oddish = Grass("Oddish", 50, 50)
charmainder = Fire("Charmainder", 25, 70)
ninetails = Fire("Ninetails", 30, 50)
ponyta = Fire("Ponyta", 40, 60)
squirtle = Water("Squirtle", 80, 20)
psyduck = Water("Psyduck", 70, 40)
polywag = Water("Polywag", 50, 50)
print bulbasoar
print bellsprout
print oddish
print charmainder
print ninetails
print ponyta
print squirtle
print psyduck
print polywag
print bulbasoar.getAttackNames()
print charmainder.getAttackNames()
print squirtle.getAttackNames()
print charmainder.get_attack_power()

print "Testing User creation..."
u = User("Pranav")
c = Computer("Sukumar")
print u
print c

print "\nTesting User methods..."
u.add_pokemon(bulbasoar)
u.add_pokemon(charmainder)
u.add_pokemon(squirtle)
print "list of pokemon"
print u.list_pokemon()
u.stats()
u.make_active_pokemon(0)
print "Active Pokemon", u.get_active_pokemon()
u.make_active_pokemon(3)
print "Active Pokemon", u.get_active_pokemon()
u.make_active_pokemon(1)
print "Active Pokemon", u.get_active_pokemon()
print "Switch Pokemon", u.switch(2)
print "Active Pokemon", u.get_active_pokemon()

print "\nTesting Pokemon methods..."
print charmainder
charmainder.heal()
print charmainder
charmainder.take_damage(5)
print charmainder
print bulbasoar
charmainder.attack(bulbasoar, "Ember")
print charmainder
print bulbasoar

print isinstance(bulbasoar, Grass)
print isinstance(bulbasoar, Fire)
print isinstance(bulbasoar, Pokemon)
print isinstance(bulbasoar, User)
"""