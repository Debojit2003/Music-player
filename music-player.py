from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer
import os


mixer.init()


def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    song_name.set(songs_list.get(ACTIVE))

    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.play()

    status.set("Song: PLAYING")


def stop_song(status: StringVar):
    mixer.music.stop()
    status.set("Song: STOPPED")


def load(listbox):
    os.chdir(filedialog.askdirectory(title='Open a songs directory'))

    tracks = os.listdir()

    for track in tracks:
        listbox.insert(END, track)


def pause_song(status: StringVar):
    mixer.music.pause()
    status.set("Song: PAUSED")


def resume_song(status: StringVar):
    mixer.music.unpause()
    status.set("Song: RESUMED")



root = Tk()
root.geometry('700x220')     
root.title('Music Player')
root.resizable(0, 0)


song_frame = LabelFrame(root, text='Current Song', bg='green', width=400, height=80)
song_frame.place(x=0, y=0)

button_frame = LabelFrame(root, text='Buttons', bg='Gray', width=400, height=120)
button_frame.place(y=80)

listbox_frame = LabelFrame(root, text='Songs-Playlist', bg='Maroon')
listbox_frame.place(x=400, y=0, height=200, width=300)


current_song = StringVar(root, value='<Not selected>')

song_status = StringVar(root, value='<Select song to play>')


playlist = Listbox(listbox_frame, font=("Times", "10", "italic"), selectbackground='Silver')

scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=BOTH)

playlist.config(yscrollcommand=scroll_bar.set)

scroll_bar.config(command=playlist.yview)

playlist.pack(fill=BOTH, padx=5, pady=5)


Label(song_frame, text='CURRENTLY PLAYING:', bg='LightBlue', font=('Verdana', 10, 'italic')).place(x=9, y=22)

song_lbl = Label(song_frame, textvariable=current_song, bg='Goldenrod', font=("Times", 12), width=25)
song_lbl.place(x=150, y=20)


pause_btn = Button(button_frame, text='Pause', bg='Pink', font=("Georgia", 13 ,"italic"), width=7,
                    command=lambda: pause_song(song_status))
pause_btn.place(x=15, y=10)

stop_btn = Button(button_frame, text='Stop', bg='Pink', font=("Georgia", 13 ,"italic"), width=7,
                  command=lambda: stop_song(song_status))
stop_btn.place(x=105, y=10)

play_btn = Button(button_frame, text='Play', bg='Pink', font=("Georgia", 13 ,"italic"), width=7,
                  command=lambda: play_song(current_song, playlist, song_status))
play_btn.place(x=195, y=10)

resume_btn = Button(button_frame, text='Resume', bg='Pink', font=("Georgia", 13 ,"italic"), width=7,
                    command=lambda: resume_song(song_status))
resume_btn.place(x=285, y=10)

load_btn = Button(button_frame, text='Load Directory', bg='Pink', font=("Georgia", 13 ,"italic"), width=35,
                  command=lambda: load(playlist))
load_btn.place(x=10, y=55)


Label(root, textvariable=song_status, bg='Teal', font=('Times', 9), justify=LEFT).pack(side=BOTTOM, fill=X)


root.update()
root.mainloop()
