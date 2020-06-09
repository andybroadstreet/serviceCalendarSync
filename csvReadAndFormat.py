# for project

import csv
import time
from datetime import datetime, timedelta

# output to output.csv
outputFile = open('output.csv', 'w',)
outputWriter = csv.writer(outputFile)

# input from workbench schedule downloaded from Lightspeed
exampleFile = open('workBenchSchedule.csv')
exampleReader = csv.reader(exampleFile)
totalRows = 0

for row in exampleReader:
    
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
    totalRows = totalRows + 1

print('total rows = ' + str(totalRows))

exampleFile = open('workBenchSchedule.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)


loopLen = 1


while loopLen < totalRows:
    
    summary = str(exampleData[loopLen][0]) + '-' + str(exampleData[loopLen][1])
    print('Event Name: ' + summary)

    description = str(exampleData[loopLen][2]) + '-' + str(exampleData[loopLen][3])
    print('Description: ' + description)

    bikeCheckIn = (exampleData[loopLen][5])
    print('Check In: ' + str(bikeCheckIn))
    daysOver = (exampleData[loopLen][6])
    print('Days Over: ' + str(daysOver) + ' days')

    import time
    import datetime

    dt = time.time()
    print(dt)

    delta = datetime.timedelta(days=int(daysOver))
    #print(delta.total_seconds())

    chkIn = dt - delta.total_seconds()
    start = datetime.datetime.fromtimestamp(chkIn)

    start_time_str = start.strftime('%Y %d %B ') + str(bikeCheckIn)
    print(start_time_str)

    #duration = exampleData[loopLen][8]
    #print('Duration: ' + str(duration) +' hours')

    print(' ')

    d = int(daysOver)
	
    if d < 0:
    	outputWriter.writerow([summary, description, start_time_str])

    loopLen = loopLen + 1
    
    # check ID to see if event exisits
    # if event exisits update()
    # else create event()
    
    


    

