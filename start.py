import csv, json, sys, datetime
#if you are not using utf-8 files, remove the next line

# sys.setdefaultencoding("UTF-8") #set the encode to utf8

fileInput = 'data.txt'
fileOutput = 'info.csv'

inputFile = open(fileInput) #open json file
outputFile = open(fileOutput, 'w') #load csv file
data = json.load(inputFile) #load json content
inputFile.close() #close the input file
output = csv.writer(outputFile) #create a csv.write

for row in data:
    timestamp = datetime.datetime.fromtimestamp(row[0]/1000.0)
    output.writerow([timestamp, str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])])