from tkinter import *

#creating window
window = Tk()
window.geometry('1000x800') #window size
window.title('File finder') #window title

#text above entry box
L1 = Label(window, text="Enter a PATH")
L1.pack()

#entry box
E1 = Entry(window)
# E1.geometry('200x200')
E1.pack()

window.mainloop()