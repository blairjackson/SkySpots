def writeCSV(filename, columns):
    #adjust filename to not overwrite the original
    filename = adjustFileName(filename)
    with open(filename, 'w') as csvfile:
        #add headers to file
        headers = ('Channel','datetime','Spot Length','cost','Position in Programme','audience impressions','Cptrate','Creative Identifier\n')
        csvfile.write(','.join(headers))
        for line in columns:
            # convert tuple to string and write each line to the file
            line = ','.join(line)
            csvfile.write(line + '\n')
        return filename

def adjustFileName(file):
    #add 'adjusted' to filename
    file = file.split('.')
    file = file[0] + 'adjusted.' + file[1]
    return file