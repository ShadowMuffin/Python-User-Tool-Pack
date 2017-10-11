import random
import webbrowser
import time
from Tkinter import *





def show_songs():
    txt = open("AlarmSongs.txt", "r")
    songs1 = txt.readlines()
    songs = ''
    for x in songs1:
        songs += x.replace('\n', '\n')
    entry.delete('1.0', END)
    entry.insert(INSERT, songs)
    txt.close()

def update_songs():
    txt = open("AlarmSongs.txt", "w+")
    txt.truncate()
    adds = entry.get('1.0', END)
    for x in adds.split("\n"):
        txt.write(x + "\n")
    txt.close()


def choose_song():
    songs = entry.get('1.0', END)
    song_list = songs.split("\n")
    rand_song = (random.choice(song_list))
    webbrowser.open(rand_song)

def count_time():
    while True:
        localtime = time.strftime("%H:%M", time.localtime()) ## HH:MM 24HR cl
        selected_time = hourEntry.get('1.0', '1.2') + ':' + minuteEntry.get('1.0', '1.2')
        if localtime == selected_time:
            choose_song()
            break
            
            
            
####----------------------------------------------------------------------------------------####



root = Tk()
root.title("Alarm Clock")
root.geometry("800x600")


title = Label(root, text = "Alarm Clock", font = ("Ariel 20 bold"))
title.place(relx = 0.4, rely = 0.05)

entryLabel = Label(root, text = "Enter the URL list for YouTube songs below", font = ("Ariel", 14))
entryLabel.place(relx = 0.25, rely = 0.15)
entry = Text(root, width = 50, height = 20)
entry.place(relx = 0.3, rely = 0.20)

timeLabel = Label(root, text = "Enter the alarm time", font = ('Ariel', 14))
timeLabel.place(relx = 0.14, rely = 0.755)
hourEntry = Text(root, width = 2, height = 1)
hourEntry.place(relx = 0.405, rely = 0.76)
comma = Label(root, text=":", font = ("Ariel", 16))
comma.place(relx = 0.43, rely = 0.75)
minuteEntry = Text(root, width = 2, height = 1)
minuteEntry.place(relx = 0.445, rely = 0.76)
startButton = Button(root, text = "Start", command = count_time)
startButton.place(relx = 0.48, rely = 0.755)

refresh = Button(root, text = "Refresh", font = "Ariel", command = update_songs)
refresh.place(relx = 0.1, rely = 0.4)

credits = Label(root, text = "Created by Lior Dahan", font = ("Ariel", 10))
credits.place(relx = 0.78, rely = 0.9)


show_songs()
root.mainloop()