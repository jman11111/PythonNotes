from tkinter import *

window = Tk()
window.title("GUI")

top_frame = Frame(window).pack()
bottom_frame = Frame(window).pack(side = "bottom")

label = Label(top_frame, text = "Calendar").pack()
btn1 = Button(bottom_frame, text = "1", bg = "red").pack(side = "left")
btn2 = Button(bottom_frame, text = "2").pack(side = "left")
btn3 = Button(bottom_frame, text = "3").pack(side = "left")
btn4 = Button(bottom_frame, text = "4").pack(side = "left")
btn5 = Button(bottom_frame, text = "5").pack(side = "left")

mainloop()