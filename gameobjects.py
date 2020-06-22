import random
import time

#Klassen

#Charakter Klasse
class Character(object):
    def __init__(self, name,):
        self.name = name
        self.level = 1
        self.klasse = None
        self.maxHP = 300 + random.randint(0, 50)
        self.aktHP = self.maxHP
        self.maxMP = 100 + random.randint(0, 20)
        self.aktMP = self.maxMP
        self.strength = 30
        self.defense = 20
        self.dodge = 1
        self.luck = 2
        self.maxXP = 100
        self.aktXP = 0
        self.abilities = ["schlag", "heal"]
    def schadenNehmen(self, schaden):
        schaden = schaden - round(0.5*self.defense)
        self.aktHP = self.aktHP - schaden
        
    def levelUp(self):
        print("Du bist ein Level aufgestiegen")
        self.level = self.level + 1
        self.maxXP += 30
        HpUp = 20 + random.randint(0, 20)
        self.maxHP += HpUp
        self.aktHP += HpUp
        MpUp = 10 + random.randint(0, 10)
        self.maxMP += MpUp
        self.aktMP += MpUp
        if self.level%2 == 0:
            self.strength += 10
        if self.level%2 == 0:
            self.defense += 10
        for i in range (0, self.luck):
            if random.randint(0, 10) == 10:
                self.luck += 1
        print("Du kannst jetzt noch einen Level Punkt an deine Stats vergeben.")
        time.sleep(2)
        print("An welchen Stat willst du diesen Punkt vergeben?")
        time.sleep(2)
        print("1 = Leben  2 = Mana  3 = Stärke  4 = Verteidigung  5 = Glück")
        Auswahl = str(input())
        if Auswahl == "1":
            self.maxHP += 30 
        elif Auswahl == "2":
            self.maxMP += 20
        elif Auswahl == "3":
            self.strength += 10
        elif Auswahl == "4":
            self.defense += 10
        elif Auswahl == "5":
            self.luck += 1
        else:
            time.sleep(0.5)
            print("Du willst dir das Spiel also schwerer machen? Ok.")
        time.sleep(2)
        print("Dies sind deine aktuellen Stats.")
        time.sleep(2)
        print(f"Level = {self.level} Leben = {self.maxHP} Mana =  {self.maxMP} Stärke = {self.strength} Verteidigung = {self.defense} Glück = {self.luck}")
        if self.level == 3:
            self.abilities += ["starkerSchlag"]
        
#Gegner Klasse
class enemy(object):
    def __init__(self, nummer, currentLayer):
        self.nummer = nummer
        if self.nummer == 1:
            self.name = "Goblin"
            self.maxHP = round((75 + 15*currentLayerLevel)*currentLayer.enemyBuff)
            self.aktHP = self.maxHP
            self.strength = round((30 + 2*currentLayerLevel)*currentLayer.enemyBuff)
            self.defense = round((25 + 2*currentLayerLevel)*currentLayer.enemyBuff)
            self.XP = round((70 + 5*currentLayerLevel)*currentLayer.enemyBuff)
        elif self.nummer == 2:
            self.name = "Slime"
            self.maxHP = round((100 + 20*currentLayerLevel)*currentLayer.enemyBuff)
            self.aktHP = self.maxHP
            self.strength = round((20 + 1*currentLayerLevel)*currentLayer.enemyBuff)
            self.defense = round((35 + 3*currentLayerLevel)*currentLayer.enemyBuff)
            self.XP = round((70 + 5*currentLayerLevel)*currentLayer.enemyBuff)
        elif self.nummer == 3:
            self.name = "Wolf"
            self.maxHP = round((50 + 10*currentLayerLevel)*currentLayer.enemyBuff)
            self.aktHP = self.maxHP
            self.strength = round((40 + 3*currentLayerLevel)*currentLayer.enemyBuff)
            self.defense = round((15 + 1*currentLayerLevel)*currentLayer.enemyBuff)
            self.XP = round((70 + 5*currentLayerLevel)*currentLayer.enemyBuff)
        elif self.nummer == 4:
            self.name = "Dämonen König"
            self.maxHP = 1000
            self.aktHP = self.maxHP
            self.strength = 100
            self.defense = 100
            self.XP = 10000
            
    def schadenNehmen(self, schaden):
        schaden = schaden - round(0.5*self.defense)
        self.aktHP = self.aktHP - schaden 
        
#Ebenen Klasse
       
class layer(object):
    def __init__(self, nummer):
        self.nummer = nummer
        if self.nummer == 1:
            self.name = "Flachland"
            self.encounter = 0.5
            self.treasure = 0.5
            self.npc = 1
            self.enemyBuff = 1
        elif self.nummer == 2:
            self.name = "Ruinen"
            self.encounter = 0.5
            self.treasure = 0.8
            self.npc = 1
            self.enemyBuff = 1.2
        elif self.nummer == 3:
            self.name = "Sumpf"
            self.encounter = 0.5
            self.treasure = 0.9
            self.npc = 1
            self.enemyBuff = 1.4
        elif self.nummer == 4:
            self.name = "Höhle"
            self.encounter = 0.5
            self.treasure = 1
            self.npc = 1
            self.enemyBuff = 1.6

currentLayerLevel = 0

#Ebenen Wechsel

#Auswahl
def ebenenWechsel(currentLayerLevel, currentLayer, encounter, player, bossfight, BOSSFIGHT):
    Wochen = 0
    while Wochen<=4:
        Wochen += 1
        currentLayerLevel += 1
        player.aktHP = player.maxHP
        player.aktMP = player.maxMP
        currentLayer = layer(random.randint(1, 4))
        print(f"Du bist in {currentLayer.name}.")
        Tag = 0
        while Tag<=7:
            Tag += 1
            event = random.random()
            if event<currentLayer.encounter:
                encounter(player, currentLayer, BOSSFIGHT)
            elif currentLayer.encounter<event<currentLayer.treasure:
                #treasure()
                print("Schatz")
            elif currentLayer.treasure<event<currentLayer.npc:
                #npcEncounter()
                print("NPC")
    bossfight(encounter, player, currentLayer, BOSSFIGHT)
    



#Statabhängige Sachen

#Stats Anzeigen lassen
def statsAnzeigen(player):
    print(f"Dein Name ist {player.name}.")
    print(f"Du bist Level {player.level}.")
    print(f"Du bist ein {player.klasse}.")
    print(f"Du hast aktuell {player.aktHP} von {player.maxHP} Leben.")
    print(f"Du hast aktuell {player.aktMP} von {player.maxMP} Mana.")
    print(f"Deine Stärke beträgt {player.strength}.")
    print(f"Du hast {player.defense} Verteitigung.")
    print(f"Du hast aktuell {player.aktXP} Erfahrung.")
    print(f"Deine Fähigkeiten sind {player.abilities}.")

#Xp bekommen
def XpGain(player, currentEnemy):
    player.aktXP += currentEnemy.XP
    XpCheck(player)
    
#Xp Check
def XpCheck(player):
    while player.aktXP>=player.maxXP:
        player.aktXP -= player.maxXP
        player.levelUp()
        
 
#Teil eines Kampfes
    
#Begegnung
def encounter(player, currentLayer, BOSSFIGHT):
    if BOSSFIGHT == True:
        currentEnemy = enemy(4, currentLayer)
    else:
        currentEnemy = enemy(random.randint(1,3), currentLayer)
    time.sleep(2)
    print("Du wirst von einem " + currentEnemy.name + " angegriffen!")
    #print("                      ^")
    #print("Hier -----------------| wird die angegeben gegen welchen Gegner nur kämpfst.")
    time.sleep(2)
    matchRound = 0
    while player.aktHP>0 and currentEnemy.aktHP>0:
        matchRound+=1
        time.sleep(1)
        print(f"Runde {matchRound} ")
        time.sleep(2)
        print(f"Deine Leben: {player.aktHP} Leben des Gegners: {currentEnemy.aktHP}")
        time.sleep(1)
        abilityAuswählen(player, currentEnemy)
        time.sleep(0.5)
        if currentEnemy.aktHP<=0:
            continue
        enemySchlag(currentEnemy, player)
            #if matchRound == 3:
             #   print("springe ueber...............................")
              #  continue
            
            
    if player.aktHP>0:
        print("Du hast deinen Gegner besiegt.")
        XpGain(player, currentEnemy)
    else:
        print(f"{player.name} ist gestorben.")
        del player
        print("Starte das Programm neu um es nochmal zu versuchen.")
        exit

#Auswählen einer Fähigkeit
def abilityAuswählen(player, currentEnemy):
    print(player.abilities)
    print("Welche Fähigkeit willst du nutzen?")
    currentAbility = str(input())
    abilityChoose(currentAbility, currentEnemy, player)
    
#Ausgeählte Fähigkeit
def abilityChoose(currentAbility, currentEnemy, player):
    if currentAbility == "schlag":
        schlag(currentEnemy, player)
    elif currentAbility == "heal":
        heal(currentEnemy, player)
    elif currentAbility == "starkerSchlag":
        starkerSchlag(currentEnemy, player)
    #elif
    #elif
    #elif
    #elif
    #elif
    #elif
    #elif
    #elif
    #elif
    #elif
    
def bossfight(encounter, player, currentLayer, BOSSFIGHT):
    BOSSFIGHT = True
    encounter(player, currentLayer, BOSSFIGHT)
    
#Fähigkeiten

#Schlag
def schlag(currentEnemy, player):
    if "schlag" in player.abilities:
        currentEnemy.schadenNehmen(player.strength)
        print("Du hast deinen Gegner für " + str(player.strength - round(0.5*currentEnemy.defense)) + " Schaden getroffen")
    else:
        abilityAuswählen(player, currentEnemy)
        
#Heal   
def heal(currentEnemy, player):
    if "heal" in player.abilities:
        if player.aktMP>40:
            player.aktMP -= 40
            player.aktHP += 40
            print(f"Du hast dich für 20 Leben geheilt und besitzt nun {player.aktHP} Leben.")
        else:
            print("Du verfügst über zu wenig Mana.")
            print(f"Du hast {player.aktMP} Mana.")
            abilityAuswählen(player, currentEnemy)
    else:
        abilityAuswählen(player, currentEnemy)

#Starker Schlag
def starkerSchlag(currentEnemy, player):
    if "starkerSchlag" in player.abilities:
        if player.aktMP>30:
            player.aktMP -= 30
            currentEnemy.schadenNehmen((player.strength + 20))
            print("Du hast deinen Gegner für " + str(player.strength + 20 - round(0.5*currentEnemy.defense )) + " Schaden getroffen")
        else:
            print("Du verfügst über zu wenig Mana.")
            print(f"Du hast {player.aktMP} Mana.")
            abilityAuswählen(player, currentEnemy)
    else:
        abilityAuswählen(player, currentEnemy)



def enemySchlag(currentEnemy, player):
    player.schadenNehmen(currentEnemy.strength)
    print("Dein Gegner trifft dich für " + str(currentEnemy.strength - round(0.5*player.defense)) + " Schaden")


    
    
    
    
    







