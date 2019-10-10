import convertDateTime, lookup

def readCSV(filename):
    with open(filename) as csvFile:
        #strip first 3 lines of csv
        columns = []
        for x in range (3):
            next(csvFile)
        for line in csvFile:
            #split the columns, keep the required ones
            splitLine = line.split(',')
            #convert date and time to our format
            if len(splitLine) == 26:
                date = convertDateTime.convertDate(splitLine[5])
                time = convertDateTime.convertTime(splitLine[6])
                dateTime = (date + 'T' + time)
                channel = lookup.barbCheck(splitLine[3])#pulling a 0 from somewhere form bar code, not in file
                cost = '0'
                cpt = ''

                #take only the necessary info
                row = [channel.rstrip(), dateTime, splitLine[7], cost, splitLine[13], splitLine[15], cpt,
                       splitLine[25].rstrip()]
                columns.append(row)
        return columns



