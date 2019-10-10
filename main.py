import convertExtension,splitFile,write, sftp

#convert .amb extension to csv
file = convertExtension.convert()
#return the required columns along with matched channels from barb
columns = splitFile.readCSV(file)
#write to new file
newFile = write.writeCSV(file, columns)
#drop file via SFTP
#sftp.upload(newFile)
