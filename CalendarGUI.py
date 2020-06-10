from tkinter import *
from Calendar import calendar

def generateDaysofMonth(calendar, container, clear, delta):
    counterDay = 1
    counterRow = 1
    counterColumn = 1
    month = calendar.currentMonth
    clear()
    for day in range(len(calendar.Calendar[month+delta-1])):
        if (len(calendar.Calendar[month+delta-1][day]) > 0):
            btn1 = Button(container, text = counterDay, bg = "red").grid(ipadx=13,ipady=10,row=counterRow,column=counterColumn)
        else:
            btn1 = Button(container, text = counterDay).grid(ipadx=13,ipady=10,row=counterRow,column=counterColumn)
        if(counterColumn == 7):
            counterColumn = 1
            counterRow = counterRow + 1
        else:
            counterColumn = counterColumn + 1
        counterDay = counterDay + 1
    calendar.currentMonth = calendar.currentMonth + delta

currentCalendar = calendar()

window = Tk()
window.title("GUI")

top_frame = Frame(window)
top_frame.grid(row=0, column=0)
bottom_frame = Frame(window)
bottom_frame.grid(row=1, column=0)
event_frame = Frame(window)
event_frame.grid(row=0,rowspan = 2,column = 1)

def clear():
    list = bottom_frame.winfo_children()
    for l in list:
        l.destroy()

btnNextMonth = Button(top_frame, text = "-->",command = lambda: generateDaysofMonth(currentCalendar,bottom_frame,clear,1))
btnNextMonth.grid(row=0,column=8)
btnPreviousMonth = Button(top_frame, text = "<--",command = lambda: generateDaysofMonth(currentCalendar,bottom_frame,clear,-1))
btnPreviousMonth.grid(row=0,column=0)

label = Label(top_frame, text = "Calendar")
label.grid(row=0,column=1,ipadx=40)

eventtitlelabel = Label(event_frame, text = "Events:")
eventtitlelabel.grid(row=0,column=0,ipadx=40)
eventslabel = Label(event_frame, text = "test")
eventslabel.grid(row=1,column=0,ipadx=40)

generateDaysofMonth(currentCalendar,bottom_frame,clear,0)

mainloop()