myDict = {"Denis": 2000}
print(myDict)
print(myDict["Denis"])
print(myDict.get("Anton"))
myDict.update({"Demid": 2001, "sasha": 2002})
print(myDict)
a = myDict.pop("Denis")
print(myDict)
print(a)
mySet = {1, 2, 3, 4, 3, "Denis", "Denis", True, True}
print(mySet)
mySet.update({5, "Artyr"})
print(mySet)
mySet.discard(2)
print(mySet)
