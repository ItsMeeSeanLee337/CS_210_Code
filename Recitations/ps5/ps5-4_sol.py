import re

f = open("html.txt", "r")
code = f.read()
f.close()

fout = open("task4output.txt", "w")

openingTags = re.findall('<[a-z0-9].*?>', code)
for x in openingTags:
  if re.search('class = ".*?"', x):
    res1 = re.findall('class = ".*?"', x)
    res2 = re.findall('".*"', res1[0])
    res3 = re.sub('\"', '', res2[0])

    res4 = re.sub('<', '', re.split(' ', x)[0])
    fout.write(','.join([res3,res4]) + "\n")