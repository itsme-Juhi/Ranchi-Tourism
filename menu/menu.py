''' 
In this program i had made all the related menu functions to 
return the menu command for further operations 
'''
import tkinter as tk
from tkinter import *
import webbrowser
from PIL import Image, ImageTk
import imageio
'''
All the functions at one place 
'''
def pahari():
    pahari = tk.Tk()
    pahari.title("Pahari mandir")
    pahari.geometry("400x400")
    pahari.configure(background = "black")
    lable1 = tk.Label(pahari, text= "Pahari mandir :-",bg = "black",fg = "yellow" , font = "comicsans 20 bold")
    lable1.pack(side = "top")
    label2 = tk.Label(pahari, text = '''Pahari Mandir is a temple located in hilltop in Ranchi the capital of Jharkhand.\n The temple is dedicated to Shiva. This temple is located at 2140 feet above sea level and 350 feet above the ground. To reach the temple one has to climb 468 steps.\n The entire Ranchi city can be seen from the temple. Lord Shiva is worshiped in linga form in the hill temple. There is a large crowd of Shiva devotees here during the month of Shivaratri and Sawan.\n
    The story of the hill temple of Ranchi\n the capital of Jharkhand, is very interesting. This temple of Lord Shiva situated on the mountain was in the possession of the British before the independence of the country and they used to hang the Freedom Fighters here.\n Since Independence, the national flag is also hoisted with Independence Day and Republic Day along with religious flags on this temple.\n This is the first temple in the country where the tricolor is hoisted.\n

    This temple of Lord Shiva, located 7 km from Ranchi railway station is known as Pahari Temple. \nThe old name of the Pahari Baba temple was Tiriburu which later changed to 'Hanging Garry' in British times because Freedom Fighters were hanged here under the British rule.\n

    After independence the first tricolor flag was hoisted here in Ranchi,\n which was hoisted by a freedom fighter Krishna Chandra Das of Ranchi.\n He hoisted the tricolor in memory and honor of the martyred Freedom Fighters here.\n Since that time the tricolor is hoisted here on Independence Day and Republic Day every year.\n There is a stone in the hill temple, on which the message of freedom of the country is written on the midnight of August 14 and 15, 1947.''',bg = "black",fg = "red", font = "times 12")
    label2.pack(side = "left", fill = "x")
    pahari.mainloop()

def jagnath():
    jagnath = tk.Tk()
    jagnath.title("Jagnath mandir")
    jagnath.geometry("400x400")
    jagnath.configure(background = "black")
    lable1 = tk.Label(jagnath, text= "Jagnath mandir :-",bg = "black",fg = "yellow" , font = "comicsans 20 bold")
    lable1.pack(side = "top")
    jagnath.mainloop()

def sun():
    sun = tk.Tk()
    sun.title("Sun temple")
    sun.geometry("400x400")
    sun.configure(background = "black")
    lable1 = tk.Label(sun, text= "Sun Temple :-",bg = "black",fg = "yellow" , font = "comicsans 20 bold")
    lable1.pack(side = "top")
    sun.mainloop()

def hanuman():
    hanuman = tk.Tk()
    hanuman.title("Shree hanuman mandir")
    hanuman.geometry("400x400")
    hanuman.configure(background = "black")
    lable1 = tk.Label(hanuman, text= "Shree Hanuman mandir :-",bg = "black",fg = "yellow" , font = "comicsans 20 bold")
    lable1.pack(side = "top")
    hanuman.mainloop()

def dewri():
    dewri = tk.Tk()
    dewri.title("Dewri mandir")
    dewri.geometry("400x400")
    dewri.configure(background = "black")
    lable1 = tk.Label(dewri, text= "Dewri mandir :-",bg = "black",fg = "yellow" , font = "comicsans 20 bold")
    lable1.pack(side = "top")
    dewri.mainloop()