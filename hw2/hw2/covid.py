#Last edit: 10/28 9:05PM





#FINAL FINAL EDIT 10/23 3:53PM
import csv

#Problem 2 part 3
def prob2Part3Helper(province): #returns avg of latitude/longitude values for the province
    with open("covidTrain.csv", 'r') as readFile:
        reader = csv.reader(readFile)
        
        latitude_sum = 0
        latitude_count = 0
        
        longitude_sum = 0
        longitude_count = 0
        
        for num, row in enumerate(reader):
            if num == 0: continue
            if row[4].strip().lower() == province.strip().lower(): #province
                
                if row[6] != "NaN": #latitude
                    latitude_sum += float(row[6])
                    latitude_count += 1
                    
                if row[7] != "NaN": #longtitude
                    longitude_sum += float(row[7])
                    longitude_count += 1
                    
        latAvg = round(latitude_sum / latitude_count, 2)
        longAvg = round(longitude_sum / longitude_count, 2)
        
        return latAvg, longAvg
    
    
def prob2Part4Helper(province): #returns most occuring city value in given province
    with open("covidTrain.csv", "r") as readFile:
        reader = csv.reader(readFile)
        
        outDict = {}
        for num, row in enumerate(reader):
            if num == 0 or row[3] == "NaN": continue
                
            if row[4].lower().strip() == province.lower().strip(): #if province matches
                city = row[3]
                if city in outDict:
                    outDict[city] = outDict[city] + 1
                else:
                    outDict[city] = 1
                    
                    
        #sorting
        outDictSorted = sorted(outDict.items(), reverse = True, key = lambda movie: movie[1])
        maxCount = outDictSorted[0][1]
        listOfTies = []
        for each_tuple in outDictSorted:
            if each_tuple[1] == maxCount:
                listOfTies.append(each_tuple[0])
        sortedListOfTies = sorted(listOfTies) #alphabetically
        return sortedListOfTies[0]
                
def prob2Part5Helper(province): #returns single most frequent symptom in the province
    with open("covidTrain.csv", "r") as readFile:
        reader = csv.reader(readFile)
        
        outDict = {}
        
        for num, row in enumerate(reader):
            if num == 0 or row[11] == "NaN": continue
            
            if row[4].lower().strip() == province.lower().strip(): #if province matches
                symptom = row[11]
                if ";" in symptom: #if u come across multiple symptoms for a single record, consider them individually for frequency counts
                    symptomList = symptom.split(";")
                    for eachSymptom in symptomList:
                        if eachSymptom.strip() in outDict:
                            outDict[eachSymptom.strip()] = outDict[eachSymptom.strip()] + 1
                        else:
                            outDict[eachSymptom.strip()] = 1
                else: #if its single record
                    if symptom in outDict:
                        outDict[symptom] = outDict[symptom] + 1
                    else:
                        outDict[symptom] = 1
        #sorting
        outDictSorted = sorted(outDict.items(), reverse = True, key = lambda movie: movie[1])
        maxCount = outDictSorted[0][1]
        listOfTies = []
        for each_tuple in outDictSorted:
            if each_tuple[1] == maxCount:
                listOfTies.append(each_tuple[0])
        sortedListOfTies = sorted(listOfTies) #alphabetically
        return sortedListOfTies[0]
        
                    
        
                
def prob2(): #Need to test this (and fill in the data values in new csv)
    with open("covidTrain.csv", 'r') as readFile:
        with open("covidResult.csv", 'w',newline='') as writeFile:
            reader = csv.reader(readFile)
            writer = csv.writer(writeFile, delimiter=',')
            
            for num1, row in enumerate(reader):
                if num1 == 0: 
                    writer.writerow(row)
                    continue
                    
                outList = []
                
                for num2, val in enumerate(row):
                    
                    if num2 == 1: #age
                        strAge = val.strip()
                        #floatAge = float(strAge)
                        age = strAge.split("-")
                        if len(age) == 1: #if age is in form of "15"
                            outList.append(int(strAge))
                        else: # age was in form '40-49'
                            ageRange = strAge.split("-")
                            lower = int(ageRange[0]) #40
                            upper = int(ageRange[1]) #49
                            roundedAvgVal = round(((lower + upper) / 2))
                            outList.append(roundedAvgVal)
                            
                    elif (num2 == 8 or num2 == 9) or num2 == 10: #date
                        orig_date = val.split(".")
                        dd = orig_date[0]
                        mm = orig_date[1]
                        yyyy = orig_date[2]
                        newDate = '.'.join([mm, dd, yyyy])
                        outList.append(newDate)
                        
                    elif num2 == 6 or num2 == 7: # long, lat
                        if val != "NaN": #if not missing
                            outList.append(val)
                        else: # if missing
                            latAvg, longAvg = prob2Part3Helper(row[4].strip().lower())
                            if num2 == 6: #latitude missing
                                outList.append(latAvg)
                            if num2 == 7: #longitude missing
                                outList.append(longAvg)
                    elif num2 == 3: #city
                        if val != "NaN": #not missing
                            outList.append(val)
                        else:
                            outList.append(prob2Part4Helper(row[4])) #4 is province
                    elif num2 == 11: #Symptoms
                        if val != "NaN": #not missing
                            outList.append(val)
                        else:
                            outList.append(prob2Part5Helper(row[4])) #4 is province
                    else:
                        outList.append(val)
                     
                writer.writerow(outList)
            
            
prob2()           
            
            