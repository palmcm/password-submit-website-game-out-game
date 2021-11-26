import re
from random import randrange

roomWithPassRaw = """X - EASYGAMEEZLIFEXUXNAHUF - 
B - URNOTALONE - 
E - cAn YoU ReVerSe This - 
U - MEMELORD - 
L - NowYouFinallySeeMe - 
F - CANYOUSEEME - 
V - In The Hallway!! - 
J - ThE Em1nEncE 1n Shadow - 
O - LogicGateIsEz - 
H - CANuW1N24117874978 - 
C - 8 - 
S - U Baka baka Hentai - 
A - HELLOWORLDFROMTECHCAST - 
R - never gonna give you up never gonna let you down"""

splitedRoomAndPass = roomWithPassRaw.split(" - ")

roomNames = splitedRoomAndPass[::2]
passwords = splitedRoomAndPass[1::2]

for i in range(len(roomNames)):
    roomNames[i] = roomNames[i].replace("\n", "")
    
def getAllKey(password):
    password = password.lower()
    noRepeatDict = {}
    for c in password:
        noRepeatDict[c] = True

    
    return "".join([*noRepeatDict])

roomKeyMap = {}
for i in range(len(roomNames)):
    roomName = roomNames[i]
    password = passwords[i]
    roomKeyMap[roomName] = getAllKey(password)


allKeys = getAllKey("".join(list(roomKeyMap.values())))

def findMatchRoomIndex(targetInput):
    allFoundTargets = []
    for i in range(len(roomNames)):
        roomName = roomNames[i]
        password = passwords[i]
        keys = roomKeyMap[roomName]
        indices = [i for i, x in enumerate(password.lower()) if x == targetInput]
        if targetInput in keys:
            for ind in indices:
                allFoundTargets.append(roomName + str(ind))

    return allFoundTargets

def randomRoom(rooms):
    ind = randrange(len(rooms))
    return rooms[ind]

def findAllMatch(keys):
    for key in keys:
        allMatchRoomAndIndex = findMatchRoomIndex(key)
        if len(allMatchRoomAndIndex) < 1:
            print(key, "- not found")
        else:
            target = randomRoom(allMatchRoomAndIndex)
            roomName = target[0]
            index = target[1:]
            print("keyPhrase += getCharacterFrom(pairs, \"{0}\", {1})".format(roomName, index))

findAllMatch("inter key phrase here")