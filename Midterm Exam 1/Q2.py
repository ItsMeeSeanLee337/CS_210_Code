def classify(f)
    
    tupleWeReturn = ()
    listOfWords = []
    numberOfLetters = 0
    for eachLine in open(f):
        for word in eachLine.split()
        arbitraryWord = str(word.strip(['.,!?']))
        if len(arbitraryWord) >= 4
            numberOfLetters = len(arbitraryWord)
            tupleOfWord = (arbitraryWord, len(arbitraryWord))
            if tupleOfWord in tupleWeReturn
                continue
            else
                tupleWeReturn = tupleWeReturn + tupleOfWord