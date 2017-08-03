import os
import random
import sys
import tkinter as tk
from tkinter import messagebox

def addToClipBoard(text):
    if sys.platform != "linux":
        command = "echo " + text + " | clip"
        os.system(command)


def randomMAC():
    avlist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D", "E", "F"]
    a1 = random.choice(avlist)
    a2 = random.choice(avlist)
    a3 = random.choice(avlist)
    a4 = random.choice(avlist)
    a5 = random.choice(avlist)
    a6 = random.choice(avlist)
    a7 = random.choice(avlist)
    a8 = random.choice(avlist)
    a9 = random.choice(avlist)
    a10 = random.choice(avlist)
    a11 = random.choice(avlist)
    a12 = random.choice(avlist)

    mac = a1 + a2 + ":" + a3 + a4 + ":" + a5 + a6 + ":" + a7 + a8 + ":" + a9 + a10 + ":" + a11 + a12

    return mac


def getMAC(event=None):
    labeltext = randomMAC()
    label1.configure(text=labeltext)
    label2.configure(text="Random MAC:")


def info():
    infoMessage()


def copy():
    if sys.platform == "linux":
        root.destroy()
    else:
        asd = label1.cget("text")
        addToClipBoard(asd)
        root.destroy()


def infoMessage():
    messagebox.showinfo(title="Info", message="Written by Mehmet Fatih Okuyan")


root = tk.Tk()
root.title("Random MAC")
root.geometry("640x480")
root.configure(bg="black")
if sys.platform != "linux":
    root.iconbitmap("randommac.ico")

frame1 = tk.Frame(root, bg="black", bd="2", width=640, height=480)
frame1.pack()

label1 = tk.Label(frame1, fg="white", bg="black", font="Roboto 40", text="")
label1.place(x=20, y=160, width=600, height=130)
label1.focus()
label1.bind('<Return>', getMAC)
label2 = tk.Label(frame1, fg="white", bg="black", font="Roboto 13", text="Press \"New MAC\" button or Enter")
label2.place(x=165, y=60, width=310, height=50)

newMACButton = tk.Button(frame1, fg="white", bg="red", font="Roboto 14", text="New MAC", command=getMAC)
newMACButton.place(x=135, y=360, width=120, height=40)
copyButton = tk.Button(frame1, fg="white", bg="red", font="Roboto 14", text="Copy & Quit", command=copy)
copyButton.place(x=385, y=360, width=120, height=40)
infoButton = tk.Button(frame1, fg="white", bg="black", font="Roboto 5", text="i", command=info)
infoButton.place(x=610, y=450, width=20, height=20)

root.resizable(width=False, height=False)
root.mainloop()
