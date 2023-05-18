import tkinter as tk
import os
import numpy as np
from pygame import mixer

mixer.init()

window = tk.Tk()
window.geometry("600x400")
window.title("Music Player")
window.config(bg='lightblue')

path = "/home/koushik/Music"
dir_list = os.listdir(path)
check_list = os.listdir(path)

def checkend():
  global paused
  if not mixer.music.get_busy() and not paused:
     window.after(100,checkend)
     playnext()
  else:
    window.after(100,checkend)

currmusic=np.random.choice(dir_list)
check_list.remove(currmusic)
mixer.music.load(path+"/"+currmusic)
mixer.music.play()
global paused 
paused = False
window.after(100,checkend)



def playnext():
 global paused
 paused = False
 if len(check_list) == 0:
  quit()
 else:
  while True:
   currmusic=np.random.choice(dir_list)
   if currmusic in check_list:
       check_list.remove(currmusic)
       break
  label.config(text=currmusic)
  mixer.music.load(path+"/"+currmusic)
  mixer.music.play()

  

label = tk.Label(window,text=currmusic,bg = 'lightblue',fg = 'violet' ,font =("Iskoola Pota", "40", "bold italic"))
label.pack(pady = 20)

frame = tk.Frame(window,bg = 'lightblue')
frame.pack(anchor  = 'center')

def pause():
 global paused
 paused = True
 mixer.music.pause()

def resume():
 global paused
 mixer.music.unpause()
 paused = False

def exit():
 quit()

pausebutton = tk.Button(window,text="Pause",command=pause)
pausebutton.pack(pady = 40, in_ = frame, side = 'left')

playbutton = tk.Button(window,text="Resume",command=resume)
playbutton.pack(pady = 40, in_ = frame, side = 'left',)

nextbutton = tk.Button(window,text="Next",command=playnext)
nextbutton.pack(pady = 10, in_ = frame, side = 'left')

exitbutton = tk.Button(window,text="Exit",command=exit)
exitbutton.pack(pady = 10)

window.mainloop()