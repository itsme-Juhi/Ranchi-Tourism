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
    i1 = tk.PhotoImage(file = "icon2.png")
    pahari.iconphoto(False, i1)
    pahari.title("Pahari mandir")
    pahari.geometry("400x400")
    pahari.configure(background = "grey")
    lable1 = Label(pahari, text= "this is the second window")
    lable1.pack()
    pahari.mainloop()