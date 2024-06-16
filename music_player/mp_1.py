import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

music_player = tkr.Tk()
music_player.title("My Music Player")
music_player.geometry("450x350")
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()
play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg='yellow', selectmode=tkr.SINGLE)
pos = 0 # move the pos variable outside the loop
for item in song_list:
    play_list.insert(pos, item) # indent this line under the loop
    pos += 1 # indent this line under the loop
pygame.init()
pygame.mixer.init()
vars = tkr.StringVar() # define the vars variable before using it
def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    vars.set(play_list.get(tkr.ACTIVE)) # update the vars variable with the selected song
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()
def update_song(event): # define a callback function to update the vars variable when the selection changes
    vars.set(play_list.get(tkr.ACTIVE))
Button1 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PLAY", command=play,
bg="blue", fg="white")
Button2 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=stop,
bg="red", fg="white")
Button3 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PAUSE",
command=pause, bg="purple", fg="white")
Button4 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE",
command=unpause, bg="orange", fg="white")
song_title = tkr.Label(music_player, font="Helvetica 12 bold", textvariable=vars)
song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
play_list.pack(fill="both", expand="yes")
play_list.bind("<<ListboxSelect>>", update_song) # bind the callback function to the play_list widget
music_player.mainloop()