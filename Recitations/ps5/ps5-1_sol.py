import re

f = open("task1data.txt", "r")
lines = f.readlines()
f.close()

fout = open("task1output.txt", "w")

for text in lines:
    data = re.split("\n", text)
    for x in data:
        columns = re.split(",", x)
        # print(columns)
        if re.match("^a", columns[0]) and re.match("^student$", columns[1]):

            fout.write(','.join(columns)+"\n")