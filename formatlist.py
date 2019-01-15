f = open("yob2017.txt","r") #I made this to help format the last-names file. It was used on a *very* specific format, so it probably isin't useful.
print("File loaded.")
print("Press any button to start formating.")
input()
formated = ""
ff = f.readlines()
f.close()
f = open("f.txt","a")
for i in range(len(ff)-1):

    formated = ff[i].split(",")[0]+"\n"
    print(formated)
    f.write(formated)

f.close()
