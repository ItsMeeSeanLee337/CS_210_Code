from collections import defaultdict
import re

f = open("sampleSentences.txt", "r")
lines = f.readlines()
f.close()

fout = open("task3output.txt", "w")


for text in lines:
    wordCount = defaultdict(int)

    words = re.split(" ", text)

    for i in range(len(words)):
        words[i] = re.sub('\W','',words[i])
        words[i] = re.sub(words[i], words[i].lower(), words[i])
        
    flag = True

    if len(words) >= 6:
        start = words[0]
        end = words[-1]
        if re.match(re.sub('\W','',end), start):
            for word in words:
                wordCount[word] += 1
                if ((word == start and wordCount[word] > 2) or (word != start and wordCount[word] > 1)):
                    flag = False
                    break
            if flag:
                fout.write(text)