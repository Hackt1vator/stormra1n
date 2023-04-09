# import system functions
import os
import time
import re
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from subprocess import run
import subprocess
# load images in Tkinter python
from PIL import ImageTk, Image
# web
import webbrowser
# sounds
# from pygame import mixer

# Designed and developed by @hackt1vator

# frame settings
root = tk.Tk()
frame = tk.Frame(root, width="500", height="250")
frame.pack(fill=BOTH,expand=True)
#tk.Entry(root).pack(fill='x')

# uses current directory to load the image file for the icon
root.iconphoto(False, tk.PhotoImage(file='./settings.gif'))

LAST_CONNECTED_UDID = ""
LAST_CONNECTED_IOS_VER = ""


def startcheckra1n():
    global LAST_CONNECTED_UDID, LAST_CONNECTED_IOS_VER

    root.iconphoto(False, tk.PhotoImage(file='checkra1nicon.png'))
    messagebox.showinfo("Enter DFU Mode","Get ready...\n\nFirst, press Ok button.\n\nThen, put the device into DFU mode. The jailbreak will automatically complete afterwards.")
    
    print("Loading jb script...")
    os.system("./checkra1n/checkra1n -c -V -E")
    print("Ran jb script.\n")
    #show message to jb
    messagebox.showinfo("Jailbreak Ran","Jailbreak done!\n\nNow Make it Sn0w!")
    root.iconphoto(False, tk.PhotoImage(file='settings.gif'))
    
    
def ios15bypass():

    global LAST_CONNECTED_UDID, LAST_CONNECTED_IOS_VER
    
    #iOSVER = str(LAST_CONNECTED_IOS_VER)
    iOSVer = askstring('Device iOS?', 'On what ios version are you?')
    
    #check if theres a valid string to continue to reversing jb
    if(len(iOSVer) < 2):
        showinfo('Bypass Failed', 'Give me a valid iOS version.')
    else:
        showinfo('Ready to Jailbreak...', 'Hi, iOS '+str(iOSVer)+'. \n\nWe will now bypass your device '+str(iOSVer)+' Semi-Tethered.')
        print("Starting bypass...")
        os.system(f"cd ./palera1n/ && ./palera1n.sh --tweaks {iOSVer} --semi-tethered")
        
        print("Device is bypassed!\n")
        showinfo('Bypass Success!', 'Device is now bypassed!')
    
    

def showDFUMessage():
    messagebox.showinfo("Step 1","Put your iDevice into DFU mode.\n\nClick Ok once its ready in DFU mode to proceed.")
    
def startbypass():
    os.system("bash FactoryActivation.sh")
def enterRecMode():
    print("Kicking device into recovery mode...")
    os.system("./extras/euphoria_scripts/enterrecovery.sh")
    
def exitRecMode():
    print("Kicking device out recovery mode...")
    os.system("./extras/euphoria_scripts/exitrecovery.sh")

def callback(url):
   webbrowser.open_new_tab(url)

def quitProgram():
    print("Exiting...")
    os.system("exit")
    
def opendonate():
    webbrowser.open('https://www.buymeacoffee.com/hacktivator', new=2)


root.title('Stormra1n - Made by @Hackt1vator')
frame.pack()

#set image and resize it
#img2 = Image.open("racoon.png")
#frame2 = PhotoImage(file=imagefilename, format="gif -index 2")
#NewIMGSize2 = img2.resize((120,120), Image.ANTIALIAS)
#new_image2 = ImageTk.PhotoImage(NewIMGSize2)
#label = Label(frame, image = new_image2)
#label.place(x=235, y=10)

#BIG title on program
mainText = Label(root, text="          Stormra1n",font=('Helveticabold', 24))
mainText.place(x=140, y=70)

#label
my_label2 = Label(frame,
                 text = "FactoryActivation bypass for ios 12-16")
my_label2.place(x=130, y=130)

#label
my_label3 = Label(frame,
                 text = "ver 1.0")
my_label3.place(x=10, y=220)


cButton1 = tk.Button(frame,
                   text="beat the storm",
                   command=startbypass,
                   state="normal")
cButton1.place(x=200, y=160)
cButton2 = tk.Button(frame,
                   text="start checkra1n",
                   command=startcheckra1n,
                   state="normal")
cButton2.place(x=70, y=160)
cButton3 = tk.Button(frame,
                   text="bypass ios 15-16",
                   command=ios15bypass,
                   state="normal")
cButton3.place(x=325, y=160)

#Create a Label to display the link
link = Label(root, text="Made this tool @hackt1vator",font=('Helveticabold', 12), cursor="hand2")
link.place(x=165, y=220)
link.bind("<Button-1>", lambda e:
callback("https://twitter.com/hackt1vator"))

cbeginExploit2 = tk.Button(frame,
                   text="Donate!",
                   command=opendonate,
                   state="normal")
cbeginExploit2.place(x=380, y=210)

root.geometry("500x250")

root.resizable(False, False)

root.eval('tk::PlaceWindow . center')

#make message box popup on load start
#messagebox.showinfo("Hello!","Device must be jailbroken before running Make it Sn0w!")
#song = AudioSegment.from_mp3("./extras/euphoria_scripts/success.mp3")
#messagebox.showinfo("Warning!","Make sure you have wiped the locked iDevice with iTunes using DFU mode before you begin...")

root.mainloop()

