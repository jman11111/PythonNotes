import csv
from Event import event
#reads csv and prints it
#construct months(28-31 days)
January = [[] * 5 for i in range(31)]
February = []
March = []
April = []
May = []
June = []
July = []
August = []
September = []
October = []
November = []
December = []

#construct year(12 months)
Calendar = [January,February,March,April,May,June,July,August,September,October,November,December]

Events = []
with open('Homework.csv', newline = '') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        newEvent = event(row[0],row[1],row[2])
        Events.append(newEvent)

for currEvent in Events:
    date = currEvent.date.split("/")
    dateMonth = date[0]
    dateDay = date[1]
    print(dateMonth)
    print(dateDay)
    #print (currEvent.name)
    #print (currEvent.date)
    #print (currEvent.time)
