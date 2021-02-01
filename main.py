import random as rand


def main():
    hello = input(
        "Enter\"1\"to translate English to Mark. Enter\"2\"to translate Mark to English: ")
    if hello == "1":
        translateToMark()
    elif hello == "2":
        translateToEnglish()
    else:
        print("Please enter a valid value.\nPress enter to continue: ")
        hi = input()
        if hi != "dudwgiuwdegiagiwagdshjhfdjuhfaqodjoifhuhf#frGgiuhfuf8uhvuv":
            main()


def translateToMark():
    randomInteger = rand.randint(1, 4)
    randomInteger2 = rand.randint(1, 4)
    print("Please enter text you desire to be translated to Mark: ")
    value = input()
    newValue = split(value)
    for x in newValue:
        myAscii = list(map(ord, newValue))
    z = 0
    printvalue = []
    def first(myAscii, z, randomInteger, randomInteger2):
        if z == len(myAscii):
            return myAscii
        if z % 2 == 0:
            myAscii[z] += randomInteger
            z += 1
            first(myAscii, z, randomInteger, randomInteger2)
        else:
            myAscii[z] += randomInteger2
            z += 1
            first(myAscii, z, randomInteger, randomInteger2)
    first(myAscii, z, randomInteger, randomInteger2)
    finalvalue = ""
    for x in myAscii:
        myFinalArray = list(map(chr, myAscii))
    joiner = ''.join(myFinalArray)
    finalvalue = joiner+str(randomInteger)+str(randomInteger2)
    print(finalvalue)
    hi = input()
    if hi != "dudwgiuwdegiagiwagdshjhfdjuhfaqodjoifhuhf#frGgiuhfuf8uhvuv":
        main()


def translateToEnglish():
    print("Please enter text you desire to be translated to English: ")
    value2 = input()
    newValue2 = split(value2)
    z1 = 0 
    for x in newValue2:
        myAsciis = list(map(ord, newValue2))
    int2 = newValue2[-2:-1]
    int3 = newValue2[-1:]
    randomInteger =  int(int2[0])
    randomInteger2 = int(int3[0])
    myAscii1 = myAsciis[0:-2]
    def second(myAscii1, z1, randomInteger, randomInteger2):
        if z1 == len(myAscii1):
            print('activated')
            return myAscii1
        if z1 % 2 == 0:
            myAscii1[z1] -= randomInteger
            z1 += 1
            second(myAscii1, z1, randomInteger, randomInteger2)
        else:
            myAscii1[z1] -= randomInteger2
            z1 += 1
            second(myAscii1, z1, randomInteger, randomInteger2)
    second(myAscii1, z1, randomInteger, randomInteger2)
    finalvalue = ""
    for x in myAscii1:
        myFinalArray = list(map(chr, myAscii1))
    joiner2 = ''.join(myFinalArray)
    print(joiner2)
    hi = input()
    if hi != "dudwgiuwdegiagiwagdshjhfdjuhfaqodjoifhuhf#frGgiuhfuf8uhvuv":
        main()

def split(word):
    return [char for char in word]



main()
