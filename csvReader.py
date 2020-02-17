import csv
from Event import event
#reads csv and prints it
Events = []
with open('Homework.csv', newline = '') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        newEvent = event(row[0],row[1],row[2])
        Events.append(newEvent)

for currEvent in Events:      
    print (currEvent.name)
    print (currEvent.date)
    print (currEvent.time)
