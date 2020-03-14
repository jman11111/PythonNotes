import csv
from Event import event
from datetime import date
#reads csv and prints it
#Get current Month from date string
today = date.today().strftime("%m/%d/%y")
currentMonth = int(today.split("/")[0])

#construct months(28-31 days)
January = [[] for i in range(31)]
February = [[] for i in range(28)]
March = [[] for i in range(31)]
April = [[] for i in range(30)]
May = [[] for i in range(31)]
June = [[] for i in range(29)]
July = [[] for i in range(31)]
August = [[] for i in range(31)]
September = [[] for i in range(30)]
October = [[] for i in range(31)]
November = [[] for i in range(30)]
December = [[] for i in range(31)]

#construct year(12 months)
Calendar = [January,February,March,April,May,June,July,August,September,October,November,December]

Events = []
#Gets all events in month(int) given and returns array
def getEventsInMonth(month):
    inMonth = []
    for day in range(len(Calendar[month])):
        for event in Calendar[month][day]:
            inMonth.append(event)

    return inMonth

#Gets all events in a month(int) and prints them
def printEventsInMonth(month):
    for event in getEventsInMonth(month):
        print(event.name + " is on " + event.date + " at " + event.time)

#read in all events from csv and store them in Events array
with open('Homework.csv', newline = '') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        newEvent = event(row[0],row[1],row[2])
        Events.append(newEvent)

#take all events and put them into Calendar 3D array
for currEvent in Events:
    date = currEvent.date.split("/")
    dateMonth = int(date[0])
    dateDay = int(date[1])
    Calendar[dateMonth][dateDay].append(currEvent)

print("\nEvents Happening in this Month: \n")
printEventsInMonth(currentMonth)
