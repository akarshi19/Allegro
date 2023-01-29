from tkinter import *
from pygame import *
root=Tk()
root.title("Allegro")
root.state('zoomed')
root.configure(bg='Black')


def play_allegro():
    allegro_track=Playlist.get(ACTIVE)
    print(allegro_track[0:-4])

def apprehend_allegro():
    road = filedialog.askdirectory()
    if road:
        os.chdir(road)
        gaane=os.listdire(road)

        for gaana in gaane:
            if gaana.endwith(".mp3"):
                Playlist.insert(END,gaana)

mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()


root.mainloop()
