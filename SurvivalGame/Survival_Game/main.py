import time, random, sys, colorama
from colorama import Fore, init, Back, Style
init(autoreset=True)

# VARIABLES
money = 20
health = 10
xp = 0
trophies = 0
myAchievements = []
achievements = ['Making an Upgrade', 'Rich', 'Healthy', 'Monster Hunter']
fishLevel = 1
huntLevel = 1
fightLevel = 1
location = 'home'

# INTRO
print('Welcome to the game of life!!!')
print('Version ' + Fore.YELLOW + Style.BRIGHT + '0.5.0' + Fore.WHITE + Style.NORMAL)
print('What is your name?')
name = input()
print('Hello %s!' %(name))
print('Make money and survive!')

# DAMAGE
def damageMsg():
    print('You now have ' + Fore.RED + Style.BRIGHT +'%s' %(health) + Fore.WHITE + Style.NORMAL+ ' health.')

# TERMINATE
def terminate():
    print('Game Terminated. ' + Style.BRIGHT + Fore.BLUE + '%s' %(xp) + Style.NORMAL + Fore.WHITE + ' xp, ' + Style.BRIGHT + Fore.GREEN + '%s' %(money) + Style.NORMAL + Fore.WHITE + ' money, ' + Style.BRIGHT + Fore.RED + '%s' %(health) + Style.NORMAL + Fore.WHITE + ' health, and ' + Style.BRIGHT + '%s' %(trophies) + Style.NORMAL + ' trophies.')
    time.sleep(2)

# HEAL
def healMsg(heal):
    print('You healed ' + Fore.RED + Style.BRIGHT + '%s' %(heal) + Style.NORMAL + Fore.WHITE + '.')

# XPGAIN
def xpMsg(xpgain):
    print('You gained ' + Fore.BLUE + Style.BRIGHT + '%s' %(xpgain) + Style.NORMAL + Fore.WHITE + ' xp.')

# XP
def currentXp(xp):
    print('You now have ' + Fore.BLUE + Style.BRIGHT +'%s' %(xp) + Fore.WHITE + Style.NORMAL+ ' xp.')

# MONEYGAIN
def moneyMsg(sell):
    print('You gained ' + Fore.GREEN + Style.BRIGHT + '%s' %(sell) + Style.NORMAL + Fore.WHITE + ' money.')

# MONEY
def currentMon(money):
    print('You now have ' + Fore.GREEN + Style.BRIGHT +'%s' %(money) + Fore.WHITE + Style.NORMAL+ ' money.')

# TROPHY GAIN
def trophGain(amount):
    global trophies
    trophies += amount
    print('You gained ' + Style.BRIGHT + str(amount) + Style.NORMAL + ' trophies.')
    print('You now have ' + Style.BRIGHT + str(trophies) + Style.NORMAL + ' trophies.' )

# SPAWN
def spawnMsg(action, name):
    print('You ' + action + ' a ' + Fore.YELLOW + Style.BRIGHT + name + Fore.WHITE + Style.NORMAL + '.')

# DEAD
def dead():
    if health <= 0:
        print('YOU DIED!')
        terminate()
        sys.exit()
def broke():
    if money <= 0:
        print('YOU LOST ALL OF YOUR ASSETS, YOU ARE HOMELESS')
        terminate()
        sys.exit()

# FISH
def fish():
    global xp
    global health
    global money
    global fishLevel
    print('Casting...')
    time.sleep(5/fishLevel)
    fishint = random.randint(0, 19)
    sell = 0
    heal = 0
    if fishint == 0:
        print('You caught ' + Fore.YELLOW + Style.BRIGHT + 'nothing' + Fore.WHITE + Style.NORMAL + '.')
        sell = 0
        heal = 0
        xpgain = 0
    if fishint == 1:
        spawnMsg('caught', 'Boot')
        sell = 0
        heal = -5
        xpgain = 0
    elif fishint == 2:
        spawnMsg('caught', 'Can')
        sell = 0
        heal = -5
        xpgain = 0
    elif fishint == 3:
        spawnMsg('caught', 'Goldfish')
        sell = 1
        heal = 1
        xpgain = 1
    elif fishint == 4:
        spawnMsg('caught', 'Catfish')
        sell = 11
        heal = 23
        xpgain = 5
    elif fishint == 5:
        spawnMsg('caught', 'Trout')
        sell = 1
        heal = 3
        xpgain = 1
    elif fishint == 6:
        spawnMsg('caught', 'Minnow')
        sell = 1
        heal = 1
        xpgain = 1
    elif fishint == 7:
        spawnMsg('caught', 'Mahi-Mahi')
        sell = 7
        heal = 12
        xpgain = 3
    elif fishint == 8:
        spawnMsg('caught', 'Patagonian Toothfish')
        sell = 20
        heal = 10
        xpgain = 3
    elif fishint == 9:
        spawnMsg('caught', 'Salmon')
        sell = 5
        heal = 13
        xpgain = 3
    elif fishint == 10:
        spawnMsg('caught', 'Yellowfin Tuna')
        sell = 5
        heal = 10
        xpgain = 4
    elif fishint == 11:
        spawnMsg('caught', 'Cod')
        sell = 5
        heal = 7
        xpgain = 3
    elif fishint == 12:
        spawnMsg('caught', 'Wells Catfish')
        catint = random.randint(1, 4)
        if catint == 4:
            health -= 30
            sell = 0
            heal = 0
            xpgain = 0
            print('You were attacked by the Wells Catfish')
            damageMsg()
            dead()
        else:
            sell = 8
            heal = 13
            xpgain = 3
    elif fishint == 13:
        spawnMsg('caught', 'Mackerel')
        sell = 7
        heal = 13
        xpgain = 3
    elif fishint == 14:
        spawnMsg('caught', 'Stonefish')
        sell = 2
        heal = -666
        xpgain = 2
    elif fishint == 15:
        spawnMsg('caught', 'Tilefish')
        sell = 4
        heal = -17
        xpgain = 2
    elif fishint == 16:
        spawnMsg('caught', 'Goliath Grouper')
        sell = 5
        heal = 20
        xpgain = 5
    elif fishint == 17:
        spawnMsg('caught', 'Sturgeon')
        sell = 18
        heal = 30
        xpgain = 5
    elif fishint == 18:
        spawnMsg('caught', 'Pufferfish')
        sell = 2
        heal = -19
        xpgain = 4
    elif fishint == 19:
        spawnMsg('caught', 'Trout')
        sell = 1
        heal = 3
        xpgain = 1
    print('Would you like to (s)ell or (e)at?')
    action = input()
    if action == 's':
        money += sell
        moneyMsg(sell)
        currentMon(money)
    elif action == 'e':
        health += heal
        healMsg(heal)
        damageMsg()
        dead()
    else:
        print('You destroyed the item.')
    xp += xpgain
    xpMsg(xpgain)
    currentXp(xp)


#HUNT
def hunt():
    global money
    global health
    global huntLevel
    global xp
    print('Searching...')
    time.sleep(5/huntLevel)
    huntint = random.randint(0, 14)
    sell = 0
    heal = 0
    if huntint == 0:
        print('You got ' + Fore.YELLOW + Style.BRIGHT + 'nothing' + Fore.WHITE + Style.NORMAL + '.')
        sell = 0
        heal = 0
        xpgain = 0
    elif huntint == 1:
        spawnMsg('got', 'Deer')
        sell = 15
        heal = 16
        xpgain = 4
    elif huntint == 2:
        spawnMsg('got', 'Bear')
        sell = 30
        heal = 11
        xpgain = 5
    elif huntint == 3:
        spawnMsg('got', 'Chicken')
        sell = 6
        heal = 5
        xpgain = 2
    elif huntint == 4:
        spawnMsg('got', 'Pig')
        sell = 7
        heal = 8
        xpgain = 3
    elif huntint == 5:
        spawnMsg('got', 'Duck')
        sell = 3
        heal = 3
        xpgain = 1
    elif huntint == 6:
        spawnMsg('got', 'Crocodile')
        crocint = random.randint(1, 4)
        if crocint == 4:
            health -= 15
            sell = 0
            heal = 0
            xpgain = 0
            print('You were attacked by the Crocodile and lost 15 health.')
            damageMsg()
            dead()
        else:
            sell = 15
            heal = 1
            xpgain = 4
    elif huntint == 7:
        spawnMsg('got', 'Rabbit')
        sell = 4
        heal = 2
        xpgain = 1
    elif huntint == 8:
        spawnMsg('got', 'Rabbit')
        sell = 4
        heal = 2
        xpgain = 1
    elif huntint == 9:
        spawnMsg('got', 'Squirrel')
        sell = 2
        heal = 2
        xpgain = 1
    elif huntint == 10:
        spawnMsg('got', 'Squirrel')
        sell = 2
        heal = 2
        xpgain = 1
    elif huntint == 11:
        spawnMsg('got', 'Moose')
        mooseint = random.randint(1, 4)
        if mooseint == 4:
            health -= 4
            sell = 0
            heal = 0
            xpgain = 0
            print('You were attacked by the Moose and lost 4 health.')
            damageMsg()
            dead()
        else:
            sell = 17
            heal = 27
            xpgain = 5
    elif huntint == 12:
        spawnMsg('got', 'Elk')
        mooseint = random.randint(1, 4)
        if mooseint == 4:
            health -= 8
            sell = 0
            heal = 0
            xpgain = 0
            print('You were attacked by the Elk and lost 8 health.')
            damageMsg()
            dead()
        else:
            sell = 20
            heal = 25
            xpgain = 5
    elif huntint == 13:
        spawnMsg('got', 'Goose')
        sell = 12
        heal = 3
        xpgain = 2
    elif huntint == 14:
        spawnMsg('got', 'Boar')
        sell = 8
        heal = 4
        xpgain = 1
    print('Would you like to (s)ell or (e)at?')
    action = input()
    if action == 's':
        money += sell
        moneyMsg(sell)
        currentMon(money)
    elif action == 'e':
        health += heal
        healMsg(heal)
        damageMsg()
        dead()
    else:
        print('You destroyed the item.')
    xp += xpgain
    xpMsg(xpgain)
    currentXp(xp)

# BATTLE
def battle(damage, hp, xpgain):
    global fightLevel
    global health
    global xp
    while hp > 0:
        print('The monster did %s damage.' %(damage))
        if location == 'dark forest':
            atkint = random.randint(1, 20)
            if atkint == 20:
                damage *= 2
            elif atkint == 1 or atkint == 2 or atkint == 3 or atkint == 4 or atkint == 5:
                damage += 10
        else:
            atkint = random.randint(1, 3)
            if atkint == 3:
                damage += 2
            elif atkint == 2:
                damage -= 1
        health -= damage
        damageMsg()
        dead()
        print("Enter 'a' to attack.")
        attack = input()
        if attack == 'a':
            print('Attacking...')
            time.sleep(1)
            hp -= fightLevel * 3
            print('You did %s damage.' %(fightLevel * 3))
            print('The monster now has %s health.' %(hp))
    xp += xpgain
    xpMsg(xpgain)
    currentXp(xp)

# FIGHT
def fight():
    global xp
    print('Finding...')
    time.sleep(3)
    if location == 'home':
        trophgain = 2
        monstint = random.randint(1, 5)
        if monstint == 1:
            spawnMsg('found', 'wild Mini-Mon')
            damage = 2
            hp = 6
            xpgain = 6
        if monstint == 2:
            spawnMsg('found', 'wild Gilrock')
            damage = 5
            hp = 5
            xpgain = 4
        if monstint == 3:
            spawnMsg('found', 'wild Bastick')
            damage = 10
            hp = 6
            xpgain = 10
        if monstint == 4:
            spawnMsg('found', 'wild Fuzz-Wuzz')
            damage = 3
            hp = 15
            xpgain = 8
        if monstint == 5:
            spawnMsg('found', 'wild Sneaky')
            damage = 4
            hp = 8
            xpgain = 8
    if location == 'ocean':
        trophgain = 3
        monstint = random.randint(1, 5)
        if monstint == 1:
            spawnMsg('found', 'wild Splashier')
            damage = 6
            hp = 45
            xpgain = 20
        if monstint == 2:
            spawnMsg('found', 'wild Surfskim')
            damage = 8
            hp = 13
            xpgain = 15
        if monstint == 3:
            spawnMsg('found', 'wild Torpedan')
            damage = 22
            hp = 10
            xpgain = 19
        if monstint == 4:
            spawnMsg('found', 'wild Gilypede')
            damage = 14
            hp = 14
            xpgain = 17
        if monstint == 5:
            spawnMsg('found', 'wild Merpish')
            damage = 7
            hp = 17
            xpgain = 11
    if location == 'forest':
        trophgain = 3
        monstint = random.randint(1, 5)
        if monstint == 1:
            spawnMsg('found', 'wild Large-Mon')
            damage = 14
            hp = 26
            xpgain = 20
        if monstint == 2:
            spawnMsg('found', 'wild Zegerbon')
            damage = 15
            hp = 16
            xpgain = 14
        if monstint == 3:
            spawnMsg('found', 'wild Tekeris')
            damage = 20
            hp = 13
            xpgain = 19
        if monstint == 4:
            spawnMsg('found', 'wild Fuzzy-Wuzzy')
            damage = 15
            hp = 20
            xpgain = 17
        if monstint == 5:
            spawnMsg('found', 'wild Cloakshade')
            damage = 21
            hp = 17
            xpgain = 20
    if location == 'dark forest':
        trophgain = 10
        monstint = random.randint(1, 5)
        if monstint == 1:
            spawnMsg('found', 'wild Gigantic-Mon')
            damage = 25
            hp = 45
            xpgain = 35
        if monstint == 2:
            spawnMsg('found', 'wild Masher')
            damage = 30
            hp = 20
            xpgain = 40
        if monstint == 3:
            spawnMsg('found', 'wild Bagindree')
            damage = 28
            hp = 30
            xpgain = 30
        if monstint == 4:
            spawnMsg('found', 'wild Mega Fuzzy-Wuzzy')
            damage = 30
            hp = 35
            xpgain = 40
        if monstint == 5:
            spawnMsg('found', 'wild Mega Sneaky-Cloakshade')
            damage = 40
            hp = 33
            xpgain = 50
    if location == 'sea floor':
        trophgain = 7
        monstint = random.randint(1, 5)
        if monstint == 1:
            spawnMsg('found', 'wild Crabiler')
            damage = 15
            hp = 25
            xpgain = 20
        if monstint == 2:
            spawnMsg('found', 'wild Sandskim')
            damage = 20
            hp = 20
            xpgain = 25
        if monstint == 3:
            spawnMsg('found', 'wild Torentapede')
            damage = 30
            hp = 16
            xpgain = 28
        if monstint == 4:
            spawnMsg('found', 'wild Gilawar')
            damage = 26
            hp = 24
            xpgain = 32
        if monstint == 5:
            spawnMsg('found', 'wild Mega Merpish')
            damage = 25
            hp = 30
            xpgain = 45
    battle(damage, hp, xpgain)
    trophGain(trophgain)
    if (achievements[3] not in myAchievements):
        print('You received an achievement: %s' %(achievements[3]))
        xp += 50
        currentXp(xp)
        myAchievements.append(achievements[3])

#TRAVEL
def travel():
    global location
    global money
    print('You are at %s.')
    print('Would you like to go to (h)ome, (o)cean, (f)orest, (d)ark forest, (s)ea floor')
    where = input()
    if where == 'o':
        location = 'ocean'
    if where == 'f':
        location = 'forest'
    if where == 'h':
        location = 'home'
    if where == 'd':
        location = 'dark forest'
    if where == 's':
        location == 'sea floor'
    print('Travelling...')
    time.sleep(10)
    print('You traveled to %s.' %(location))
    money -= 50
    print('You spent ' + Fore.GREEN + Style.BRIGHT + '50' + Fore.WHITE + Style.NORMAL + ' money.')
    currentMon(money)
    broke()

#SHOP
def shop():
    global money
    global fishLevel
    global huntLevel
    global fightLevel
    print('Would you like to upgrade (f)ishing, (h)unting?, (x)fighting, or (e)xit?')
    upgrade = input()
    if upgrade == 'f':
        fishLevel += 1
        money -= fishLevel * 10
        broke()
        print('You upgraded fishing. You are now at fishing level %s.' %(fishLevel))
    elif upgrade == 'h':
        huntLevel += 1
        money -= huntLevel * 10
        broke()
        print('You upgraded hunting. You are now at hunting level %s.' %(huntLevel))
    elif upgrade == 'x':
        fightLevel += 1
        money -= fightLevel * 15
        broke()
        print('You upgraded fighting. You are now at fighting level %s.' %(fightLevel))
    else:
        return

def market():
    global money
    global health
    print('Enter an item to purchase.')
    item = input()
    if item == 'medkit':
        health += 30
        healMsg(30)
        damageMsg()
        money -= 70
        print('You paid ' + Fore.GREEN + Style.BRIGHT + '70' + Style.NORMAL + Fore.WHITE + ' money.')
        currentMon(money)
        broke()

# GIVES ACHIEVEMENTS
def checkAchieve():
    global money
    global fishLevel
    global huntLevel
    global xp
    global health
    if (achievements[0] not in myAchievements) and (fishLevel > 1 or huntLevel > 1 or fightLevel > 1):
        print('You received an achievement: %s' %(achievements[0]))
        xp += 50
        currentXp(xp)
        myAchievements.append(achievements[0])
    if (achievements[1] not in myAchievements) and (money >= 100):
        print('You received an achievement: %s' %(achievements[1]))
        xp += 100
        currentXp(xp)
        myAchievements.append(achievements[1])
    if (achievements[2] not in myAchievements) and (health >= 50):
        print('You received an achievement: %s' %(achievements[2]))
        xp += 100
        currentXp(xp)
        myAchievements.append(achievements[2])

# DISPLAYS ACHIEVEMENTS
def achieveList():
    print('Available achievements: ' + str(achievements))
    print('Your achievements: ' + str(myAchievements))

# GAME LOOP
while True:
    try:
        broke()
        dead()
        checkAchieve()
        oof = random.randint(1, 6)
        if oof == 6 and not move == 'stats':
            health -= 5
            print('You are getting hungry and lost ' + Fore.RED + Style.BRIGHT + '5' + Fore.WHITE + Style.NORMAL + ' health.')
            damageMsg()
            dead()
        taxrand = random.randint(1, 6)
        if taxrand == 6  and not move == 'stats':
            taxint = random.randint(1, 2)
            if taxint == 1:
                money -= 5
                print('You were taxed and lost ' + Fore.GREEN + Style.BRIGHT + '5' + Fore.WHITE + Style.NORMAL + ' money.')
                currentMon(money)
            elif taxint == 2:
                tax = round(money * 0.25)
                money -= tax
                print('You were taxed and lost ' + Fore.GREEN + Style.BRIGHT + '%s' %(tax) + Fore.WHITE + Style.NORMAL + ' money.')
                currentMon(money)
            broke()
        move = input()
        if move == 'fish':
            fish()
        elif move == 'hunt':
            hunt()
        elif move == 'shop':
            shop()
        elif move == 'a':
            achieveList()
        elif move == 'quit':
            terminate()
            sys.exit()
        elif move == 'stats':
            print('Game Terminated. ' + Style.BRIGHT + Fore.BLUE + '%s' %(xp) + Style.NORMAL + Fore.WHITE + ' xp, ' + Style.BRIGHT + Fore.GREEN + '%s' %(money) + Style.NORMAL + Fore.WHITE + ' money, ' + Style.BRIGHT + Fore.RED + '%s' %(health) + Style.NORMAL + Fore.WHITE + ' health, and ' + Style.BRIGHT + '%s' %(trophies) + Style.NORMAL + ' trophies.')
        elif move == 'fight':
            fight()
        elif move == 'travel':
            travel()
        elif move == 'market':
            market()
        else: 
            print('You just wasted an action.')
    except KeyboardInterrupt:
        terminate()
        sys.exit()