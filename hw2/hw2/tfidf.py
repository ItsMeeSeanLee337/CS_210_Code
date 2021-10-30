import re
import math

def top5(myDict):
    outputList = []
    subsetList = [] #holds all keys that are of same value
    
    for key in myDict: #get first key value
        currentVal = myDict[key]
        break
        
    for each_key in myDict:
        if myDict[each_key] == currentVal: #only want to append keys of same val
            subsetList.append(each_key)
            
        else: #once the value differs
            subsetList.sort() #sorted keys for current value alphabetically 
            for key in subsetList: 
                tup = (key, myDict[key])
                outputList.append(tup)
                if len(outputList) == 5: return outputList
            #if we added all keys for this value, move to next value
            subsetList = []
            subsetList.append(each_key)
            currentVal = myDict[each_key]

# Part 1: Preprocessing; works completely
stopwords = open("stopwords.txt", "r") # Creates a stopword list that we can reference
stopWordsList = stopwords.read().splitlines()

textfile = open("tfidf_docs.txt", "r")
documentNames = textfile.read().splitlines()
for document in documentNames:
    preprocDocString = "preproc_" + document.strip()
    with open(preprocDocString, "w") as preprocDoc: # Create a new preprocx.txt file for each document in tfidf_docs.txt
        for everyLine in open(document.strip(), "r"):
            words = everyLine.split() # Creates a word list that we can go through
            for eachWord in words:
                cleanWord = re.sub('[\W]+', '', eachWord) # Remove all characters that are not words or whitespaces
                cleanWord = cleanWord.strip() # Remove extra whitespaces
                cleanWord = cleanWord.lower() # Convert all the words to lowercase 
                if cleanWord in stopWordsList:
                    continue # If the word we are looking at is in the stop words list, we go to the next word
                elif cleanWord.startswith("https"):
                    continue # If the word , we go onto the next word
                elif cleanWord.startswith("https"):
                    continue # If the word , we go onto the next word
                elif cleanWord.endswith("ing"):
                    cleanWord  = cleanWord[:-3] # If the word ends with "ing", we remove the last three characters, place it into preprocDoc, and go on to the next word
                    preprocDoc.write(cleanWord + " ")
                elif cleanWord.endswith("ly"):
                    cleanWord  = cleanWord[:-2] # If the word ends with "ly", we remove the last two characters, place it into preprocDoc and go on to the next word
                    preprocDoc.write(cleanWord + " ")
                elif cleanWord.endswith("ment"):
                    cleanWord  = cleanWord[:-4] # If the word ends with "ment", we remove the last 4 characters, place it into preprocDoc and go on to the next word
                    preprocDoc.write(cleanWord + " ")
                else:
                    preprocDoc.write(cleanWord + " ") # Adds the word into the preproc doc with a single space if it passes all the previous if statements

# Part 2: Computing TF-IDF Scores 
numberOfDocumentsWordIsIn = {}
for document in documentNames: # This loop is to count the number of documents the word is in
    preprocDocString = "preproc_" + document.strip()
    preprocDoc = open(preprocDocString, "r") # Reads each preprocx.txt file for each document in tfidf_docs.txt
    preprocDocWords = preprocDoc.read().split()
    wordFrequency = {} # Creates a dictionary of the word frequency for each document
    for word in preprocDocWords:
        if word in wordFrequency: # If the word is already in the dictionary, increment the count, if not set the count to 1
            wordFrequency[word] += 1
        else:
            wordFrequency[word] = 1
    # Compute how many documents the word is in
    for word in wordFrequency: # We iterate through word frequency for each document to add to the numberOfDocumentsWordIsIn dictionary
        if word in numberOfDocumentsWordIsIn:
            numberOfDocumentsWordIsIn[word] += 1
        else:
            numberOfDocumentsWordIsIn[word] = 1

for document in documentNames: # This loop is to find the term frequency and IDF of each word
    termFrequency = {} # Sets TF and IDF to emtpy for the new document
    inverseDocumentFrequency = {}
    preprocDocString = "preproc_" + document.strip()
    preprocDoc = open(preprocDocString, "r") # Reads each preprocx.txt file for each document in tfidf_docs.txt
    preprocDocWords = preprocDoc.read().split()
    wordFrequency = {} # Creates a dictionary of the word frequency for each document
    for word in preprocDocWords:
        if word in wordFrequency: # If the word is already in the dictionary, increment the count, if not set the count to 1
            wordFrequency[word] += 1
        else:
            wordFrequency[word] = 1
    #Computing Term Frequency
    for word in wordFrequency:
        if word in termFrequency: # If the word is already in the term frequency dictionary, we go on to the next word, if not we comput the term frequency of the word and put it into the term frequency dictionary
            continue
        else:
            termFrequency[word] = (wordFrequency.get(word) / len(preprocDocWords))
    # Computing IDF
    for word in termFrequency:
        if numberOfDocumentsWordIsIn.get(word) == 0: # If the word is found in no document, the IDF value for that word is 0
            inverseDocumentFrequency[word] = 0
        else:
            inverseDocumentFrequency[word] = (math.log(len(documentNames) / numberOfDocumentsWordIsIn.get(word))) + 1
    # Computing TF*IDF, we now have a dictionary of the TF-IDF score for every word in the document we are looking at
    tfidfScoreForDoc = {} # Empties the tfidfScoreForDoc dictionary for the new document
    for word in termFrequency:
        tfidfScoreForDoc[word] = round((termFrequency.get(word) * inverseDocumentFrequency.get(word)), 2)        
    # Sorting the TF-IDF Score dictionary, the tfidfScoreDict is now sorted
    tfidfScoreList = sorted(tfidfScoreForDoc.items(), key=lambda x:x[1], reverse = True)
    tfidfScoreDict = dict(tfidfScoreList)
    tfidfDocString = "tfidf_" + document.strip()
    countOfWord = 0
    finalList = []
    usedKeysDictionary = {}
    first_pair = list(tfidfScoreDict.items())[0]
    wordToPrint = str(first_pair[0]) # Gets the word from the first pair
    valueToPrint = float(first_pair[1]) # Gets the tfidf score from the first pair
    with open(tfidfDocString, "w") as tfidfDoc:
        print(top5(tfidfScoreDict), file = tfidfDoc)

