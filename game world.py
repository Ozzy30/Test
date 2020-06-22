import gameobjects
import time

BOSSFIGHT = False
currentLayer = gameobjects.layer(1)
currentLayerLevel = -1

print("Dies soll ein Endlos Battler sein. Das ist das Tutorial.")
time.sleep(2)
player = gameobjects.Character(str(input("Wie heißt du? \n")))
time.sleep(1)
print(f"Dein Name ist also {player.name}.")
time.sleep(1)
print("Willst du das Tutorial überspringen?")
TutorialÜberspringen = str(input())
if TutorialÜberspringen == "Nein":
    print("Es ist sehr wichtig immer genau die gegebenen Wörter korrekt zu schreiben sonst funktioniert das Spiel nicht.")
    TestEbeneStats = input(f"Willst du deine Stats wissen? Ja/Nein \n")
    if TestEbeneStats == "Ja":
        gameobjects.statsAnzeigen(player)
    else:
        None
    time.sleep(2)
    print("Als erstes lernst du wie Kämpfe funkionieren")
    Tutorial = 1
    gameobjects.encounter(player, currentLayer, BOSSFIGHT)
    gameobjects.encounter(player, currentLayer, BOSSFIGHT)
    Tutorial = 2

gameobjects.ebenenWechsel(currentLayerLevel, currentLayer, gameobjects.encounter, player, gameobjects.bossfight, BOSSFIGHT)


'''

while player.aktHP>0:
    gameobjects.ebenenWechsel(currentLayerLevel, currentLayer, gameobjects.encounter, player)
'''

'''
player = gameobjects.Character("Ozzy")
gameobjects.statsAnzeigen(player)
player.aktXP += 300
gameobjects.XpCheck(player)
gameobjects.statsAnzeigen(player)
'''



