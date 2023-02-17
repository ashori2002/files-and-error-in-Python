names = []
with open("test.txt","r") as myFile:
    for name in myFile:
        names.append(name)

print(names)

