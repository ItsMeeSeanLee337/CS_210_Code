#Last edit: 10/28 9:03PM





#FINAL FINAL EDIT 10/23 3:53PM

#WHEN YOU TEST YOUR CODE, TEST IT WITH 1/3 OF VALUES SINCE ORIGINAL FILE IS TOO MUCH




import csv
from collections import defaultdict

#Problem 1 Part 1
def prob1Part1(file):
    with open(file, 'r') as inputFile: #open returns file object and we name it inputFile
        reader = csv.reader(inputFile) #think of reader as a list of all rows
        totalFireType = 0
        totalFireTypeAbove40 = 0
        for num, row in enumerate(reader): #iterate thru each row, represented by list
            if num == 0: continue #this is header, so we don't care
            typeOfPoke = row[4]
            level = float(row[2])
            if typeOfPoke.strip().lower() == "fire":
                totalFireType += 1
                if level >= 40:
                    totalFireTypeAbove40 += 1
        percentage = round((totalFireTypeAbove40 / totalFireType) * 100)
        #print(f'Percentage of fire type Pokemons at or above level 40 = {percentage}')
        
        outputFile = open('pokemon1.txt', 'w') #open file in write mode
        outputFile.write(f'Percentage of fire type Pokemons at or above level 40 = {percentage}\n')
        outputFile.close()

prob1Part1('pokemonTrain.csv')
#Percentage of fire type Pokemons at or above level 40 = 50








#Problem 1 part 2 and 3

def aboveThreshold(attribute):
    with open("pokemonTrain.csv", 'r') as readFile:
        reader = csv.reader(readFile)
        
        numbOfPokemonsAboveThreshold = 0
        sum = 0
        indexOfAttribute = 0
        
        for num, row in enumerate(reader): #row is list
            for index, column_name in enumerate(row):
                if column_name.strip().lower() == attribute.strip().lower():
                    indexOfAttribute = index
            if num == 0: continue
                
            if float(row[2]) > 40: #if current row's level is > 40
                if row[indexOfAttribute] != 'NaN': #if atk value not missing
                    numbOfPokemonsAboveThreshold += 1
                    sum += float(row[indexOfAttribute])
        avg = sum / numbOfPokemonsAboveThreshold
        return round(avg, 1)
    
#print(aboveThreshold("atk")) #98.9
#print(aboveThreshold("def")) #127.9          
#print(aboveThreshold("hp"))  #113.5 

def belowThreshold(attribute):
    with open("pokemonTrain.csv", 'r') as readFile:
        reader = csv.reader(readFile)
        
        numbOfPokemonsAboveThreshold = 0
        sum = 0
        indexOfAttribute = 0
        
        for num, row in enumerate(reader): #row is list
            for index, column_name in enumerate(row):
                if column_name.strip().lower() == attribute.strip().lower():
                    indexOfAttribute = index
            if num == 0: continue
                
            if float(row[2]) <= 40: #if current row's level is <= 40
                if row[indexOfAttribute] != 'NaN': #if atk value not missing
                    numbOfPokemonsAboveThreshold += 1
                    sum += float(row[indexOfAttribute])
        avg = sum / numbOfPokemonsAboveThreshold
        return round(avg, 1)
    
#print(belowThreshold("atk")) #100.2
#print(belowThreshold("def")) #119.1        
#print(belowThreshold("hp"))  #111.4


def prob1Part2Helper(file, weakness): #returns most common type of this weakness
    dictForWeakness = {}
    with open(file, 'r') as inputFile:
        reader = csv.reader(inputFile)
        for num, row in enumerate(reader): #row is list
            if num == 0: continue
            pokeType = row[4].strip()
            pokeWeakness = row[5].strip().lower()
            if pokeWeakness == weakness.strip().lower() and pokeType != 'NaN': #if the row matches weaknesss we're looking for
                if pokeType in dictForWeakness:
                    dictForWeakness[pokeType] = dictForWeakness[pokeType] + 1
                else: #first time adding
                    dictForWeakness[pokeType] = 1
        dictForWeakness_sorted_list = sorted(dictForWeakness.items(), reverse = True, key = lambda movie: movie[1])
        maxCount = dictForWeakness_sorted_list[0][1]
        listOfTies = []
        for each_tuple in dictForWeakness_sorted_list:
            if each_tuple[1] == maxCount:
                listOfTies.append(each_tuple[0])
        sortedListOfTies = sorted(listOfTies) #alphabetically
        return sortedListOfTies[0]
    
def prob1Part2and3():
    with open("pokemonTrain.csv", 'r') as readFile:
        with open('pokemonResult.csv','w',newline='') as writeFile:  
            level_threshold = 40
            abv_thresh_atk = aboveThreshold("atk")
            abv_thresh_def = aboveThreshold("def")
            abv_thresh_hp = aboveThreshold("hp")

            blw_thresh_atk = belowThreshold("atk")
            blw_thresh_def = belowThreshold("def")
            blw_thresh_hp= belowThreshold("hp")
            
            writer = csv.writer(writeFile, delimiter=',') 
            reader = csv.reader(readFile)
            
            for num, row in enumerate(reader): #row is list
                if num == 0:
                    writer.writerow(row)  #include header
                    continue #continue to next row
                
                outrow = []
                pokemon_level = float(row[2]) #current row's level
                
                for num2, val in enumerate(row): #iterate thru each value in current row
                    
                    if num2 == 4: #if we're dealing with type values
                        if val == 'NaN':
                            outrow.append(prob1Part2Helper("pokemonTrain.csv", row[num2 + 1]))
                        else: 
                            outrow.append(val)   
                    elif num2 == 6: #h atk        
                        if val == "NaN":
                            if pokemon_level > 40:
                                outrow.append(abv_thresh_atk)
                            else:
                                outrow.append(blw_thresh_atk)
                        else:
                            outrow.append(val)
                    elif num2 == 7: #def
                        if val == "NaN":
                            if pokemon_level > 40:
                                outrow.append(abv_thresh_def)
                            else:
                                outrow.append(blw_thresh_def)
                        else:
                            outrow.append(val)   
                    elif num2 == 8: #hp
                        if val == "NaN":
                            if pokemon_level > 40:
                                outrow.append(abv_thresh_hp)
                            else:
                                outrow.append(blw_thresh_hp)
                        else:
                            outrow.append(val)
                    else:
                        outrow.append(val)
                        
                writer.writerow(outrow)
                

prob1Part2and3()









        
        
        
        
        
#Problem 1 Part 4
def prob1Part4():
    output_dict = {} #maps types to personalities
    with open("pokemonResult.csv", 'r') as readFile:
        reader = csv.reader(readFile)
        
        for num, row in enumerate(reader):
            if num == 0: continue
            pokemon_type = row[4].strip()
            poke_personality = row[3].strip()
            
            if pokemon_type in output_dict: 
                if poke_personality in output_dict[pokemon_type]:
                    continue
                else: 
                    #print(num)
                    output_dict[pokemon_type].append(poke_personality)
            else:
                output_dict[pokemon_type] = [poke_personality]   
    
    #Sorting keys alphabetically
    output_dict_sorted = dict(sorted(output_dict.items(), key=lambda movie: movie[0]))
    
    #sorting values list
    for keys in output_dict_sorted:
        output_dict_sorted[keys] = sorted(output_dict_sorted[keys])

    
    #printing dictionary to file
    outputFile = open('pokemon4.txt', 'w') #open file in write mode
    outputFile.write("Pokemon type to personality mapping: \n")
    outputFile.write("\n")
    for keys in output_dict_sorted: #for each key
        
        outputFile.write("\t")
        outputFile.write(keys + ": ")
        
        for num, val in enumerate(output_dict_sorted[keys]):
            if num != len(output_dict_sorted[keys]) - 1:
                outputFile.write(val + ", ")
            else:
                outputFile.write(val)
        outputFile.write("\n")
    outputFile.close()
        
prob1Part4()




#Problem 1 Part 5 
def prob1Part5():
    with open("pokemonResult.csv", 'r') as readFile:
        hpSum = 0
        numbOfPokeStgThree = 0
        reader = csv.reader(readFile)
        for num, row in enumerate(reader):
            if num == 0: continue #skip header
            if float(row[9]) == 3: #if stage is 3 for this pokemon
                hpSum += float(row[8])
                numbOfPokeStgThree += 1
                
        avg = round(hpSum / numbOfPokeStgThree)
        
        outputFile = open('pokemon5.txt', 'w') #open file in write mode
        outputFile.write(f'Average hit point for Pokemons of stage 3.0 = {avg}')
        outputFile.close()

prob1Part5()



        
        
   
                    
                    
                    
                    
                        
            
                
                