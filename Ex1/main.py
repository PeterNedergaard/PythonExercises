import math

# ------ 1A ------
print("\nTask 1A: ")

nameList = ["Henning", "Birger", "Rasmus", "Jonathan", "Henrik"]
sortedNameList = [name for name in nameList if name.casefold().startswith("h")]

print(*sortedNameList, sep=", ")


# ------ 1B ------
print("\nTask 1B: ")

powerList = [number ** 3 for number in range(1, 101)]

print(powerList)


# ------ 1C ------
print("\nTask 1C: ")

tupleList = [(len(name), name) for name in nameList]

print(*tupleList)


# ------ 1D ------
print("\nTask 1D: ")

aString = "1random2string3"
numericList = [char for char in aString if char.isnumeric()]

print(*numericList)


# ------ 1E ------
print("\nTask 1E: ")

allDiceCombinations = [(dice1, dice2) for dice1 in range(1, 7) for dice2 in range(1, 7)]
uniqueDiceCombinations = [(dice1, dice2) for dice1 in range(1, 7) for dice2 in range(1, 7) if dice2 >= dice1]

print("All combinations: " + str(allDiceCombinations))
print("Unique combinations: " + str(uniqueDiceCombinations))


# ------ 2A ------
print("\nTask 2A: ")

dictNames = {name: len(name) for name in nameList}

print(dictNames)


# ------ 2B ------
print("\nTask 2B: ")

dictNumbers = {number: math.sqrt(number) for number in range(1,11)}

print(dictNumbers)


# ------ EXTRA ------
print("\nEXTRA: ")

diceCombinationChances = {str(dice1)+"-"+str(dice2): str(round(2/36*100, 2))+"%" if dice1 != dice2 else str(round(1/36*100, 2))+"%" for dice1 in range(1, 7) for dice2 in range(1, 7) if dice2 >= dice1}

print(diceCombinationChances)

