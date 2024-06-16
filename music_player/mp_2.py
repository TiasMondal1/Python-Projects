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
pos = 0
for item in song_list:
    play_list.insert(pos, item)
    pos += 1


pygame.init()
pygame.mixer.init()
song_name = tkr.StringVar()
def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    song_name.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()
def skip():
    current_pos = pygame.mixer.music.get_pos()
    new_pos = current_pos + 5000
    new_pos = new_pos / 1000.0
    pygame.mixer.music.set_pos(new_pos)
    
def rewind():
    current_pos = pygame.mixer.music.get_pos()
    new_pos = current_pos - 5000
    new_pos = new_pos / 1000.0
    pygame.mixer.music.set_pos(new_pos)
    
def update_song(event):
    song_name.set(play_list.get(tkr.ACTIVE))
Button1 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PLAY", command=play, bg="blue", fg="white")
Button2 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=stop, bg="red", fg="white")
Button3 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PAUSE", command=pause, bg="purple", fg="white")
Button4 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE", command=unpause, bg="orange", fg="white")
Button5 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="SKIP", command=skip, bg="green", fg="white")
Button6 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="REWIND", command=rewind, bg="pink", fg="white")
song_title = tkr.Label(music_player, font="Helvetica 12 bold", textvariable=song_name)
song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
Button5.pack(fill="x")
Button6.pack(fill="x")
play_list.pack(fill="both", expand="yes")
play_list.bind("<<ListboxSelect>>", update_song)
music_player.mainloop()
