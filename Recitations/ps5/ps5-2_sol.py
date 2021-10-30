import re

f = open("sampleSentences.txt", "r")
lines = f.readlines()
f.close()

counts = {}
for line in lines:
    for f in re.findall("([A-Z]+)", line):
        line = line.replace(f, f.lower())
    words = re.split(" ", line)


    for word in words:
        if word[0].isalpha():
            if word[0] in counts:
                counts[word[0]] += 1
            else:
                counts[word[0]] = 1

f = open("task2output.txt", "w")
for x in counts:
    f.write(x+":"+str(counts[x])+"\n")

f.close()
