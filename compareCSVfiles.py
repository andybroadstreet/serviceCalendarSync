# csvReadAndFormat.py
# read csv file of incoming events to upload (output.csv)
# 
# read csv file of events exisiting in calendar (outputUpcomingEvents.csv)
# check gCalendarEvents.csv to see if incoming event from workBench.csv exisits.
# if exisits.. do nothing.. else create event

import csv

# final file to output uncreated data event to
outputNewCalendarEvents = open('outputNewCalendarEvents.csv', 'w')
outputNewCalendarEventsWriter = csv.writer(outputNewCalendarEvents)

# open csv with information parsed from lightspeed export
workBenchSchedule = open('output.csv')
workBenchReader = csv.reader(workBenchSchedule)
workBenchData = list(workBenchReader)

totalRowsX = 0
totalRowsY = 0

workBenchSchedule = open('output.csv')
workBenchReader = csv.reader(workBenchSchedule)

for row in workBenchReader:
    
    # print('Row #' + str(workBenchReader.line_num) + ' ' + str(row))
    totalRowsX = totalRowsX + 1

print('total rows in output.csv = ' + str(totalRowsX))


# open csv with information parsed from google calendar
googleCalendarEvents = open('outputUpcomingEvents.csv')
googleCalendarReader = csv.reader(googleCalendarEvents)
googleCalendarData = list(googleCalendarReader)

googleCalendarEvents = open('outputUpcomingEvents.csv')
googleCalendarReader = csv.reader(googleCalendarEvents)

for row in googleCalendarReader:
    
    # print('Row #' + str(workBenchReader.line_num) + ' ' + str(row))
    totalRowsY = totalRowsY + 1

print('total rows in outputUpcomingEvents.csv = ' + str(totalRowsY))


x = 0
y = 0

exisitingEventFlag = 0

while x < totalRowsX:

    print("Comparing....")
    while y < totalRowsY:
        
        print(workBenchData[x][0], '-->', googleCalendarData[y][0])

        if workBenchData[x][0] == googleCalendarData[y][0]:
            #print ("same...")
            exisitingEventFlag = 1
        #else:
            #print ("diff...")

        y = y + 1

    if exisitingEventFlag == 0:
        print("Event", workBenchData[x][0], "does not exisit! Uploading...")
        outputNewCalendarEventsWriter.writerow([workBenchData[x][0], workBenchData[x][1], workBenchData[x][2]])
        print(workBenchData[x][0], workBenchData[x][1], workBenchData[x][2])
    else: 
        print('Event exisits! Do nothing')
        exisitingEventFlag = 0
    y = 0
    x = x + 1

    

