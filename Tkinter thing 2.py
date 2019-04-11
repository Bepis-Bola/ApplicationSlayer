def printtext():
    global e
    string = e.get()
    try:
        print(int(string))
    except:
        print("Something went wrong")

from tkinter import *
root = Tk()

root.title('Hour')

e = Entry(root)
e.pack()
e.focus_set()

b = Button(root,text='okay',command=printtext)
b.pack(side='bottom')

root.title('Name')

e = Entry(root)
e.pack()
e.focus_set()

b = Button(root,text='okay',command=printtext)
b.pack(side='bottom')

root.mainloop()