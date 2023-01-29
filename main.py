import tkinter as tk
import time
from tkinter import filedialog



root = tk.Tk()
root.geometry("200x200")

browsebutton = tk.Button(text = "Browse", command = browse_file)
browsebutton.pack()

playbutton = tk.Button(text = "Play", command = play_music)
playbutton.pack()

pausebutton = tk.Button(text = "Pause", command = pause_music)
pausebutton.pack()

stopbutton = tk.Button(text = "Stop", command = stop_music)
stopbutton.pack()

root.mainloop()
