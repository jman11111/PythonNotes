import csv
from Event import event
from datetime import date
from tkinter import *
#reads csv and prints it

class calendar:

    def __init__(self):
        #Get current Month from date string
        today = date.today().strftime("%m/%d/%y")
        self.currentMonth = int(today.split("/")[0])

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
        self.Calendar = [January,February,March,April,May,June,July,August,September,October,November,December]

        self.Events = []

        self.readEvents()
        self.fillCalendar()
        self.printEventsInMonth(3)

    #Gets all events in month(int) given and returns array
    def getEventsInMonth(self,month):
        inMonth = []
        for day in range(len(self.Calendar[month])):
            for event in self.Calendar[month][day]:
                inMonth.append(event)

        return inMonth

    #Gets all events in a month(int) and prints them
    def printEventsInMonth(self,month):
        for event in self.getEventsInMonth(month):
            print(event.name + " is on " + event.date + " at " + event.time)

    #read in all events from csv and store them in Events array
    def readEvents(self):
        with open('Homework.csv', newline = '') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                newEvent = event(row[0],row[1],row[2])
                self.Events.append(newEvent)

    #take all events and put them into Calendar 3D array
    def fillCalendar(self):
        for currEvent in self.Events:
            date = currEvent.date.split("/")
            dateMonth = int(date[0])
            dateDay = int(date[1])
            self.Calendar[dateMonth][dateDay].append(currEvent)

