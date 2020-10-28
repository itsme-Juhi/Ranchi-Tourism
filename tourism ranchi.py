import tkinter as tk, threading
from tkinter import *
import imageio
from PIL import Image, ImageTk
from menu import menu
config = {"title":"Ranchi tourism", "version":"[Version: 0.1]"}
class Marquee(tk.Canvas):
    def __init__(self, parent, text, margin=2, borderwidth=1, relief='flat', fps=30):
        tk.Canvas.__init__(self, parent, borderwidth=borderwidth, relief=relief)
        self.fps = fps

        # start by drawing the text off screen, then asking the canvas
        # how much space we need. Use that to compute the initial size
        # of the canvas. 
        text = self.create_text(0, -1000, text=text, anchor="w", tags=("text",))
        (x0, y0, x1, y1) = self.bbox("text")
        width = (x1 - x0) + (2*margin) + (2*borderwidth)
        height = (y1 - y0) + (2*margin) + (2*borderwidth)
        self.configure(width=width, height=height)

        # start the animation
        self.animate()

    def animate(self):
        (x0, y0, x1, y1) = self.bbox("text")
        if x1 < 0 or y0 < 0:
            # everything is off the screen; reset the X
            # to be just past the right margin
            x0 = self.winfo_width()
            y0 = int(self.winfo_height()/2)
            self.coords("text", x0, y0)
        else:
            self.move("text", -1, 0)

        # do again in a few milliseconds
        self.after_id = self.after(int(1000/self.fps), self.animate)

video_name = "intro1.mp4" #This is your video file path
video = imageio.get_reader(video_name)

def stream(label):

    for image in video.iter_data():
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        label.config(image=frame_image,height = 400, width = 1200 )
        label.image = frame_image
def pah():
    p = Tk()
    p.configure(bg = "black")
    lb = Label(p, text = "Pahari Mandir", font = "times 20 bold",bg = "black", fg= "red")
    lb.pack()
    photo = PhotoImage(file = "icon2.png")
    lable = Label(p, Image = photo)
    lable.pack()
    p.mainloop()
if __name__ == "__main__":

    root = tk.Tk()
    root.geometry("500x700")
    root.configure(bg="black")
    root.title(config["title"] + " " +config["version"])
    root.state('zoomed')
    i1 = tk.PhotoImage(file = "icon1.png")
    root.iconphoto(False, i1)
    Heading = tk.Label(text = "WELLCOME TO RANCHI TOURISM",font = "times 32 bold", bg = "black",fg ="yellow")
    Heading.pack()
    marquee = Marquee(root, text="This Application is developed by Awanish Kumar for those who really intrested to explore the new Horizons of Ranchi the heart of Jharkhand", borderwidth=1, relief="sunken")
    marquee.pack(side="top", fill="x", pady=20)
    my_label = tk.Label(root)
    my_label.pack()
    thread = threading.Thread(target=stream, args=(my_label,))
    thread.daemon = 1
    thread.start()
    sub_heading = tk.Label(text = "Please do check the Menu section to know the the visitable site of the Ranchi !", font = "comicsans 20 bold", bg = "black" ,fg = "red")
    sub_heading.pack(fill = "x", side = "left")
    menubar = tk.Menu(root, background='lightblue', foreground='black',
               activebackground='#004c99', activeforeground='white')  
    pilgrimmenu = tk.Menu(menubar, tearoff=0, background='lightblue', foreground='black')
    pilgrimmenu.add_separator()
    pilgrimmenu.add_command(label = "Pahari Mandir",command = menu.pahari)
    pilgrimmenu.add_command(label = "Jaganath Mandir")
    pilgrimmenu.add_command(label = "sun temple")
    pilgrimmenu.add_command(label = "shri Hanuman Mandir")
    pilgrimmenu.add_command(label = "Dewari Mandir")
    pilgrimmenu.add_separator()
    menubar.add_cascade(label="Relegious", menu=pilgrimmenu)

    parkmenu = tk.Menu(menubar, tearoff = 0, background = 'lightblue', foreground = 'red')
    parkmenu.add_separator()
    parkmenu.add_command(label = "oxygen park")
    menubar.add_cascade(label = "Parks", menu = parkmenu)

    fallmenu = tk.Menu(menubar, tearoff = 0, background = 'lightblue', foreground = 'red')
    fallmenu.add_separator()
    fallmenu.add_command(label = "oxygen park")
    menubar.add_cascade(label = "Falls", menu = fallmenu)

    hangmenu = tk.Menu(menubar, tearoff = 0, background = 'lightblue', foreground = 'red')
    hangmenu.add_separator()
    hangmenu.add_command(label = "oxygen park")
    menubar.add_cascade(label = "Hangout", menu = hangmenu)

    dammenu = tk.Menu(menubar, tearoff = 0, background = 'lightblue', foreground = 'red')
    dammenu.add_separator()
    dammenu.add_command(label = "oxygen park")
    menubar.add_cascade(label = "Dam's", menu = dammenu)

    musmenu = tk.Menu(menubar, tearoff = 0, background = 'lightblue', foreground = 'red')
    musmenu.add_separator()
    musmenu.add_command(label = "oxygen park")
    menubar.add_cascade(label = "Museam", menu = musmenu)
    root.config(menu=menubar)
    root.mainloop()

