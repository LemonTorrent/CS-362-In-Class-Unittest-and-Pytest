def wordCount( countstr ):
    #numWords = 0
    #for i in range(len(countstr)):
        #if (countstr[i] == ' '):
            #numWords += 1

    numWords = len(countstr.split())
    return numWords

countstr = input()

print("numWords:", wordCount(countstr))

countstr = input()

print("numWords:", wordCount(countstr))
