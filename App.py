import psutil
import os
import signal
import time
import tkinter as tk
from tkinter import *
from _thread import start_new_thread

RemTime = 3600
MachID = "0000000"

#print(psutil.pids())
isOn = True
isOn2 = False
count = 0

def message():
    top = Toplevel()
    top.title("Stop")
    msg = Message(top, text='stop')
    msg.pack()
    button = Button(top, text="ok", command=top.destroy)
    button.pack()

def on():
    global isOn
    global RemTime
    while True:
        time.sleep(5)
        #print("isOn:" + str(isOn))
        if isOn:
            #print("Start")
            try:
                p_list = []
                for pid in psutil.pids():
                    p = psutil.Process(pid)
                    p_list.append(p.name())

                for pid in psutil.pids():
                    p = psutil.Process(pid)

                    # print(p.name())
                    # if "" in p_list:
                    #     if "" in p.name():
                    #         os.kill(pid, signal.SIGTERM)
                    #         print ("Killed app")
                    #         message()
                    if "MinecraftLauncher.exe" in p_list or "Minecraft.exe" in p_list:
                        if "javaw" in p.name():
                            os.kill(pid, signal.SIGTERM)
                            print ("Killed app")
                            message()
                    if "Twitch.exe" in p_list:
                        if "minecraft" in p.name():
                            os.kill(pid, signal.SIGTERM)
                            print("Killed app")
                            message()
                        elif "javaw" in p.name():
                            os.kill(pid, signal.SIGTERM)
                            print("Killed app")
                            message()
                    if "Fortnite" in p.name():
                        os.kill(pid, signal.SIGTERM)
                        print("Killed app")
                        message()
                    if "steamwebhelper.exe" in p_list:
                        if "Fallout" in p.name():
                            os.kill(pid, signal.SIGTERM)
                            print("Killed app")
                            message()
                        elif "SkyrimSE.exe" in p.name():
                            os.kill(pid, signal.SIGTERM)
                            print("Killed app")
                            message()
                        elif "Stardew" in p.name():
                            os.kill(pid, signal.SIGTERM)
                            print("Killed app")
                            message()
                        elif "CorpseParty" in p.name():
                            os.kill(pid, signal.SIGTERM)
                            print("Killed app")
                            message()
                        elif "hl" in p.name():
                            os.kill(pid, signal.SIGTERM)
                            print("Killed app")
                            message()
                        elif "Life" in p.name():
                            os.kill(pid, signal.SIGTERM)
                            print("Killed app")
                            message()
                        elif "lisa" in p.name():
                            os.kill(pid, signal.SIGTERM)
                            print("Killed app")
                            message()
                        elif "ornflakestein" in p.name():
                            os.kill(pid, signal.SIGTERM)
                            print("Killed app")
                            message()
                        elif "TESV" in p.name():
                            os.kill(pid, signal.SIGTERM)
                            print("Killed app")
                            message()
                        elif "Chrono" in p.name():
                            os.kill(pid, signal.SIGTERM)
                            print("Killed app")
                            message()
                        elif "Civilization" in p.name():
                            os.kill(pid, signal.SIGTERM)
                            print("Killed app")
                            message()
                        elif"Postal" in p.name():
                            os.kill(pid, signal.SIGTERM)
                            print("Killed app")
                            message()
                    if "GeForceNOW" in p.name():
                        os.kill(pid, signal.SIGTERM)
                        print("Killed app")
                        message()
            except:
                #print("Something went wrong, retrying")
                count = 0
        else:
            RemTime -= 5
            print("Time left: " + str(RemTime))
            # update the time left in the UI
            
def timer():
    global isOn
    Hours = (int(e1.get()))
    Minutes = (int(e2.get()))
    Seconds = (int(e3.get()))
    Time = Hours * 3600 + Minutes * 60 + Seconds
    print("Turning on timer for " + str(Time) + " Seconds")
    isOn = False
    time.sleep(Time)
    if isOn == False:
        print("Turning off timer")
        isOn = True

def on2():
    start_new_thread(timer, ())


def setOn():
    global  isOn
    if isOn == True:
        isOn = False
        isOn2 = False
        print ("Turning off")
    else:
        isOn = True
        print("Turning on")

start_new_thread(on, ())



# root = tk.Tk()
# frame = tk.Frame(root)
# frame.pack()
# button = tk.Button(frame,
#                    text="QUIT",
#                    fg="red",
#                    command=quit)
# button.pack(side=tk.LEFT)
# slogan = tk.Button(frame,
#                    text="On/Off",
#                    command=setOn)
# slogan.pack(side=tk.LEFT)

master = Tk()
Label(master, text="Hours").grid(row=0)
Label(master, text="Minutes").grid(row=1)
Label(master, text="Seconds").grid(row=2)
Label(master, text='Time Left:').grid(row=3)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
Button(master, text='Set Timer', command=on2).grid(row=4, column=1, sticky=W, pady=4)
Button(master, text='On/Off', command=setOn).grid(row=4, column=2, sticky=W, pady=4)
Button(master, text='Quit', command=quit).grid(row=4, column=0, sticky=W, pady=4)



# hours = int(e1)*3600
# minutes = int(e2)*60
# seconds = int(e3)
# time = hours + minutes + seconds
# if isOn == True:
#     time.sleep

master.mainloop()

#REEEEEEEEEEEEEEE