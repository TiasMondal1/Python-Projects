import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

music_player = tkr.Tk()
music_player.title("My Music Player")
music_player.geometry("450x350")
directory = askdirectory()
song_list = os.listdir()
play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg='yellow', selectmode=tkr.SINGLE)
pos = 0
for item in song_list:
    play_list.insert(pos, item)
    pos += 1
pygame.init()
pygame.mixer.init()
song_name = tkr.StringVar()
sound = None # create a global variable to store the current sound object
def play():
    global sound # use the global variable
    # get the full path of the selected song
    song_path = os.path.join(directory, play_list.get(tkr.ACTIVE))
    # load the sound object from the song path
    sound = pygame.mixer.Sound(song_path)
    # play the sound object
    sound.play()
    song_name.set(play_list.get(tkr.ACTIVE))
def stop():
    global sound # use the global variable
    # stop the sound object
    sound.stop()
def pause():
    global sound # use the global variable
    # pause the sound object
    sound.pause()
def unpause():
    global sound # use the global variable
    # unpause the sound object
    sound.unpause()
def skip():
    global sound # use the global variable
    # get the current position of the sound object in seconds
    current_pos = sound.get_pos() / 1000.0
    # add 5 seconds
    new_pos = current_pos + 5
    # set the new position of the sound object
    sound.set_pos(new_pos)
def rewind():
    global sound # use the global variable
    # get the current position of the sound object in seconds
    current_pos = sound.get_pos() / 1000.0
    # subtract 5 seconds
    new_pos = current_pos - 5
    # set the new position of the sound object
    sound.set_pos(new_pos)
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
