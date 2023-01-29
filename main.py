from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import *
import os


root=Tk()
root.title("Allegro")
root.state('zoomed')
root.configure(bg='White')
mixer.init()


def apprehend_allegro():
    road = filedialog.askdirectory()
    if road:
        os.chdir(road)
        gaane = os.listdire(road)

        for gaana in gaane:
            if gaana.endwith(".mp3"):
                Playlist.insert(END,gaana)

def play_allegro():
    allegro_track=Playlist.get(ACTIVE)
    print(allegro_track[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

#ICONS

allegro_img = PhotoImage(file="logo.png")
Label(root,image=allegro_img).grid(row=0,column=11)
#Button(root,image=allegro_img)
icon_play=PhotoImage(file="play.png")
Button(root,image=icon_play,bg="DarkGoldenrod1",command=play_allegro).grid(row=4,column=5)

icon_stop=PhotoImage(file="stop.png")
Button(root,image=icon_stop,bg="DarkGoldenrod1",command=mixer.music.stop).grid(row=4,column=3)

icon_pause=PhotoImage(file="pause.png")
Button(root,image=icon_pause,bg="DarkGoldenrod1",command=mixer.music.pause).grid(row=4,column=7)



#allegro_menu = PhotoImage(file="3dots.png")
#Label(root, image=allegro_menu).pack(side=RIGHT)
frame_allegro = Frame(root, bd=2, relief=RIDGE)
frame_allegro.grid(row=4,column=7)

Button(root, text="Add Music", width=15, height=2, font=("times new roman",12,"bold"),fg="Black", bg="#21b3de",command= apprehend_allegro).grid(row=3,column=9)


root.mainloop()
