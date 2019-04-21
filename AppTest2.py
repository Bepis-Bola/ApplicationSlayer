import psutil
import os
import signal
import time
import tkinter as tk
from tkinter import *
from _thread import start_new_thread
import datetime
from firebase import firebase
firebase = firebase.FirebaseApplication('https://unity3d-46471.firebaseio.com/', None)

MachID = "0000000"
result = str(firebase.get('/aaaclarkproj/' + MachID + '/RemTime', None)).replace('"','')
print(result)
RemTime = int(result)
# print(psutil.pids())
isOn = True
isOn2 = False
count = 0

status = ("off")

def message():
    top = Toplevel()
    top.title("Stop")
    msg = Message(top, text='stop')
    msg.pack()
    button = Button(top, text="ok", command=top.destroy)
    button.pack()

def TimesUp():
    top = Toplevel()
    top.title("Time's up")
    msg = Message(top, text="Time's up")
    msg.pack()
    button = Button(top, text="ok", command=top.destroy)
    button.pack()

def on(text1):
    global isOn
    global RemTime
    global status
    while True:
        time.sleep(5)
        result = str(firebase.get('/aaaclarkproj/' + MachID + '/RemTime', None)).replace('"','')
        print(result)
        RemTime = int(result)
        # print("isOn:" + str(isOn))
        if isOn:
            status = ("on")
            # print("Start")
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
                            print("Killed app")
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
                        elif "Postal" in p.name():
                            os.kill(pid, signal.SIGTERM)
                            print("Killed app")
                            message()
                    if "GeForceNOW" in p.name():
                        os.kill(pid, signal.SIGTERM)
                        print("Killed app")
                        message()
            except:
                # print("Something went wrong, retrying")
                count = 0
        else:
            if RemTime <= 0:
                isOn = True
                print("Time's up")
                TimesUp()
            else:
                RemTime -= 5
                print("Time left:  " + str(RemTime))
                # update the time left in the UI
                text1.set('Time Left: ' + str(datetime.timedelta(seconds=RemTime)))
                print('Time Left: ' + str(datetime.timedelta(seconds=RemTime)))
                firebase.put('/aaaclarkproj', name = MachID + '/RemTime', data = RemTime)



# def timer():
#     global isOn
#     Hours = (int(e1.get()))
#     Minutes = (int(e2.get()))
#     Seconds = (int(e3.get()))
#     Time = Hours * 3600 + Minutes * 60 + Seconds
#     print("Turning on timer for " + str(Time) + " Seconds")
#     isOn = False
#     time.sleep(Time)
#     if isOn == False:
#         print("Turning off timer")
#         isOn = True


def on2():
    start_new_thread(timer, ())


def setOn():
    global isOn
    global status
    if isOn == True:
        isOn = False
        text2.set("Application Slayer is off")
        isOn2 = False
        print("Turning off")
    else:
        isOn = True
        text2.set("Application Slayer is on")
        print("Turning on")






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
# Label(master, text="Hours").grid(row=0)
# Label(master, text="Minutes").grid(row=1)
# Label(master, text="Seconds").grid(row=2)
text2 = StringVar()
if isOn == True:
    text2.set('Application Slayer is currently on')
else:
    text2.set('Application Slayer is currently off')
appstatus = Label(master, textvariable = text2)
appstatus.grid(row = 0)
# Label(master, text = "Application Slayer is currently ").grid (row = 0)

text1 = StringVar()
# text1.set('Time Left:' + str(RemTime))
text1.set('Time Left:' + str(datetime.timedelta(seconds=RemTime)))
lbl = Label(master, textvariable = text1)
lbl.grid(row=3)

# e1 = Entry(master)
# e2 = Entry(master)
# e3 = Entry(master)
#e4 = Entry(master)

# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# e3.grid(row=2, column=1)
#e4.grid(row=3, column=1)
# Button(master, text='Set Timer', command=on2).grid(row=4, column=1, sticky=W, pady=4)
Button(master, text='On/Off', command=setOn).grid(row=4, column=1, sticky=W, pady=4)
Button(master, text='Quit', command=master.destroy).grid(row=4, column=0, sticky=W, pady=4)




# hours = int(e1)*3600
# minutes = int(e2)*60
# seconds = int(e3)
# time = hours + minutes + seconds
# if isOn == True:
#     time.sleep

start_new_thread(on, (text1,))

master.mainloop()

#フォートナイトが大好き

#I CANT PULL ON MY DESKTOP REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE

# REEEEEEEEEEEEEEE