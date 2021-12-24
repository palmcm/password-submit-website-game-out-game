import random
import copy
from Password import roomWithPassRaw, keypharse, seed

splitedRoomAndPass = roomWithPassRaw.split(" - ")

roomNames = splitedRoomAndPass[::2]
passwords = splitedRoomAndPass[1::2]

for i in range(len(roomNames)):
    roomNames[i] = roomNames[i].replace("\n", "")

roomKeyMap = {}
maxpassword = 0
minpassword = 20
for i in range(len(roomNames)):
    roomName = roomNames[i]
    password = passwords[i]
    maxpassword = max(maxpassword, len(password))
    minpassword = min(minpassword, len(password))
    roomKeyMap[roomName] = password
maxpassword+=10
minpassword+=3
#all possible word
f = open("words.txt")
words = set([i.strip() for i in f.readlines()])
wordscount = len(words)

allkey = [key.strip() for key in keypharse.split()]
for key in allkey:
    if key in words:
        words.remove(key)
    else:
        raise Exception("Key not found in words.txt")
wordslist = list(words)
random.shuffle(wordslist)

wordslist += [""] * len(allkey)

def insert_word(word,index):
    if wordslist[index%wordscount] in allkey:
        return False
    for i in range(1,len(wordslist)+1):
        if wordslist[-i] == "":
            wordslist[-i] = wordslist[index%wordscount]
            wordslist[index%wordscount] = word
            return True
    return False
    
def gen_range():
    a = random.randint(0,minpassword)
    b = random.randint(a+1,maxpassword)
    return [a,b]

def cal_index(room,rang):
    return sum([ord(i) for i in roomKeyMap[room][rang[0]:rang[1]]])

def random_word(word):
    room = []
    const = []
    randranges = []
    leftroom = copy.deepcopy(roomNames)
    addidx = 0
    while len(leftroom) > 0:
        sroom = random.choice(leftroom)
        leftroom.remove(sroom)
        ranrange = gen_range()
        con = random.randint(1,20)
        ind = cal_index(sroom,ranrange)
        addidx += con*ind
        room.append(sroom)
        const.append(con)
        randranges.append(ranrange)
    con = random.randint(0,wordscount)
    room.append("-")
    const.append(con)
    randranges.append([0,0])
    addidx += con
    insert_word(word,addidx)
    return {"room":room,"const":const,"range":randranges}

def add_key():
    gen = []
    for key in allkey:
        gen.append(random_word(key))
    return gen

if __name__ == "__main__":
    random.seed(seed)
    f1 = open("wordlist","w")
    f2 = open("encode","w")
    gen = add_key()
    f1.write(str(wordslist))
    f2.write(str(gen))
