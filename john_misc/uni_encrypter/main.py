import random
import time
import re
def cs():
    a = "\n"*52
    return(a)

def encrypt(s):
    r = random.SystemRandom()
    seed = r.randint(0,10**len(s))
    random.seed(seed)
    seed = str(seed)
    seed = ("0"*(len(s)-len(seed))) + seed
    s = list(s)
    for i in range(len(s)):
        s[i] = ord(unicode(s[i]))
        print(s[i])
    for i in range(len(s)):
        j = int(random.random()*10000000)
        s[i] += j
        s[i] %= 10000000
    for i in range(len(s)):
        s[i] = str(s[i])
        s[i] = '0'*(7-len(s[i])) + s[i]
        s[i] = seed[i] + s[i]
    return("".join(s))

def decrypt(s):
    s = re.findall("[0-9]{8}",s)
    seed = ""
    for i in s:
        seed += i[0]
    seed = float(seed)
    random.seed(seed)
    for i in range(len(s)):
        s[i] = int(s[i])
        j = int(random.random()*10000000)
        s[i] -= j
        s[i] %= 10000000
    for i in range(len(s)):
        print(s[i])
        #s[i] = unichr(s[i])
    return("".join(s))

def add_note(s,title):
    s = encrypt(s)
    title = encrypt(title)
    print("\x07")
    f = open("/home/emilyblack/john_misc/uni_encrypter/msg.txt","a")
    f.write(s + " " + title + "\n")
    f.close()

def get_notes():
    f = open("/home/emilyblack/john_misc/uni_encrypter/msg.txt","r").read().strip().split("\n")
    d = {}
    for i in range(len(f)):
        f[i] = f[i].split(" ")
        f[i][0] = decrypt(f[i][0])
        f[i][1] = decrypt(f[i][1])
        count = 1
        f_ = f[i][1]
        while f[i][1] in d:
            f[i][1] = f_ + " (" + str(count) + ")"
            count += 1
        d[f[i][1]] = f[i][0]
        print(f[i][1])
    return(d)

inp = raw_input(cs() + "Do you want to Read (R) a note or Add (A) a note? ").upper()
while inp:
    while inp not in ["R","A"]:
        inp = raw_input(cs() + "Do you want to Read (R) a note or Add (A) a note? ").upper()
    if inp == "A":
        add_note(raw_input(cs() + "What is your note? "),raw_input(cs() + "What is your title? "))
        print(cs())
    elif inp == "R":
        print(cs())
        notes = get_notes()
        note = raw_input("Which note do you want to read? ")
        while note not in notes and note:
            print(cs())
            get_notes()
            note = raw_input("Which note do you want to read? ")
        if note:
            print(cs())
            print(notes[note])
        print
    inp = raw_input("Do you want to Read (R) a note or Add (A) a note? ").upper()