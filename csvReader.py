import csv
from Event import event
#reads csv and prints it
with open('Homework.csv', newline = '') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        newEvent = event(row[0],row[1],row[2])
        print (newEvent.name)
        print (newEvent.date)
        print (newEvent.time)
