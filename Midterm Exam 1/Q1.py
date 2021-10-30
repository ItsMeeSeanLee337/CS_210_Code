def getShots(f, lowerBound = 10000, upperBound = 500000)
    
    dateShotsVaccineTuple = ()
    listOfShotsWithinbounds = []
    
    for eachLine in open(f):
        currentLine = eachLine.split(":")
        date = str(currentLine[0].strip())
        numberOfShots = int(currentLine[1].strip())
        vaccine = str(currentLine[0].strip())
        
        if numberOfShots >= lowerBound and numberOfShots <= upperBound:
            dateShotsVaccineTuple = (date, numberOfShots, vaccine)
            listOfShotsWithinbound.append(dateShotsVaccineTuple)
            dateShotsVaccineTuple = ()
        else:
            continue
            
    return listOfShotsWithinBounds