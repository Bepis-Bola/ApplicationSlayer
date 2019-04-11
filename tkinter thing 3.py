from tkinter import *

def show_entry_fields():
   print("Hours: %s\nMinutes: %s\nSeconds: %s" % (e1.get(), e2.get(), e3.get()))
   Hours = (int(e1.get()))
   Minutes = (int(e2.get()))
   Seconds = (int(e3.get()))
   Time = Hours * 3600 + Minutes * 60 + Seconds
   print(Time)

master = Tk()
Label(master, text="Hours").grid(row=0)
Label(master, text="Minutes").grid(row=1)
Label(master, text="Seconds").grid(row=2)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )