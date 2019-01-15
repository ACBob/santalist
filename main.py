import random # Quite random

f = open("names.txt","r")
names = f.read().split("\n")
f.close()
f = open("lastnames.txt","r")
lastnames = f.read().split("\n") # Ok this is just variable shit
non = ""
ii = ""

for i in range(50): # Bring me loops brother
    l = names[i]
    ii = random.randint(0,len(lastnames)-1)
    ii = lastnames[ii]
    if random.randint(0,2) == 0: # The cursed random-picker.
        non = ",  Nice."
    elif random.randint(0,2) == 1:
        non = ",  Naughty."
    else:
        non = ", Undecided."
    print(l.upper() +"_"+ ii.upper() + non.upper()) # I mean i could just assign a variable.
