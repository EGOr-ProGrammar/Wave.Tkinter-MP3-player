import tkinter as tk
from tkinter import filedialog
import pygame
import time
from mutagen.mp3 import MP3

pygame.mixer.init()


class Mp3Player():
    """ Ui and logic of a simple mp3 player"""

    def __init__(self, root):
        """ Intitiating all ui, global variables"""

        global paused
        paused = False
        # Temporary solution to play songs from any device
        global path

        # Create playlist box
        self.__song_box = tk.Listbox(root, bg="#002B4D", fg="white", width="60", selectbackground="white",
                                     selectforeground="#002B4D")

        # Buttons icons
        self.__pause_btn_img = tk.PhotoImage(file="images\pause50.png")
        self.__play_btn_img = tk.PhotoImage(file="images\play50.png")
        self.__forward_btn_img = tk.PhotoImage(file="images\\forward50.png")
        self.__back_btn_img = tk.PhotoImage(file="images\\back50.png")

        # Create frame for control buttons
        self.__btn_frame = tk.Frame(root, bg="#E5F3FF")

        # Controll buttons
        self.__back_btn = tk.Button(self.__btn_frame, image=self.__back_btn_img, borderwidth=0,
                                    command=self.previous_song, bg="#E5F3FF")
        self.__play_btn = tk.Button(self.__btn_frame, image=self.__play_btn_img, borderwidth=0, command=self.play,
                                    bg="#E5F3FF")
        self.__pause_btn = tk.Button(self.__btn_frame, image=self.__pause_btn_img, borderwidth=0, command=self.pause,
                                     bg="#E5F3FF")
        self.__forward_btn = tk.Button(self.__btn_frame, image=self.__forward_btn_img, borderwidth=0,
                                       command=self.next_song, bg="#E5F3FF")

        # Create main menu
        self.__main_menu = tk.Menu(root)
        root.config(menu=self.__main_menu)

        # Create 'Add songs' menu
        self.__add_song_menu = tk.Menu(self.__main_menu)
        self.__main_menu.add_cascade(label="Add songs", menu=self.__add_song_menu)

        self.__add_song_menu.add_command(label="Add song to playlist", command=self.add_song)
        self.__add_song_menu.add_command(label="Add many songs to playlist", command=self.add_many_songs)

        # Create 'Remove songs' menu
        self.__remove_song_menu = tk.Menu(self.__main_menu)
        self.__main_menu.add_cascade(label="Remove songs", menu=self.__remove_song_menu)

        self.__remove_song_menu.add_command(label="Delete song from playlist", command=self.delete_song)
        self.__remove_song_menu.add_command(label="Delete all songs from playlist", command=self.delete_all_songs)

        # Create status bar that shows duration of the song
        self.__status_bar = tk.Label(root, text="", bd=1, relief=tk.GROOVE, anchor=tk.E, bg="#7FC7FF")

        # Display all vidgets
        self.__song_box.pack(pady=20)

        self.__btn_frame.pack()

        self.__back_btn.grid(row=0, column=0, padx=10)
        self.__pause_btn.grid(row=0, column=1, padx=10)
        self.__play_btn.grid(row=0, column=2, padx=10)
        self.__forward_btn.grid(row=0, column=3, padx=10)

        self.__status_bar.pack(fill=tk.X, side=tk.BOTTOM, ipady=2)

    def add_song(self):
        """ Adds a song to the end of listbox deleting song's path and extension"""
        global path

        song_path = filedialog.askopenfilename(title="Choose song", filetypes=(("mp3 Files", "*.mp3"),))

        song_path = song_path.split("/")
        path = "/".join(song_path[:-1])
        # Strip out directory info and extension
        song = song_path[-1].replace(".mp3", "")

        # Add song to the end of listbox
        self.__song_box.insert(tk.END, song)

    def add_many_songs(self):
        """ Adds many songs to the end of listbox deleting songs's path and extension"""
        global path

        songs_path = filedialog.askopenfilenames(title="Choose songs", filetypes=(("mp3 Files", "*.mp3"),))

        # Erasing path and extension of an every song
        for song in songs_path:
            song = song.split("/")
            song = song[-1].replace(".mp3", "")

            # Add song to the end of listbox
            self.__song_box.insert(tk.END, song)

        # Take path of the song from tuple of songs
        songs_path = list(songs_path)
        songs_path = songs_path[0].split("/")
        path = "/".join(songs_path[:-1])

    def play(self):
        global paused
        global path
        """ Plays selected song from listbox"""

        song = self.__song_box.get(tk.ACTIVE)

        song_path = f'{path}\\{song}.mp3'
        try:
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play(loops=0)
            paused = False
        except:
            pass
        # Display duration of the song
        self.song_length()

    def pause(self):
        """ Pause and unpause current song"""
        global paused

        # Unpause
        if (paused):
            pygame.mixer.music.unpause()
            paused = False
        # Pause
        else:
            pygame.mixer.music.pause()
            paused = True

    def next_song(self):
        """ Playing next song in the list box """
        # Get current song tuple from listbox
        next_s = self.__song_box.curselection()

        # If we go forward of the last song, first song in the listbox
        # starting to play.    

        if next_s[0] == (self.__song_box.size() - 1):
            # Index of the first song, because current song is last
            # in the listbox
            next_s = 0
        else:
            # Index of the previous song
            next_s = next_s[0] + 1

        # Clear current song and make active next one 
        self.__song_box.selection_clear(0, tk.END)

        self.__song_box.selection_set(next_s)
        self.__song_box.activate(next_s)
        # Play next song
        self.play()

    def previous_song(self):
        """ Playing previous song in the list box """
        # Get current song tuple from listbox
        previous_s = self.__song_box.curselection()

        # If we go backward of the first song, last song in the listbox
        # starting to play.    
        if previous_s[0] == 0:
            # Index of the last song
            previous_s = self.__song_box.size() - 1
        else:
            # Index of the previous song
            previous_s = previous_s[0] - 1

        # Clear current song and make active previous one 
        self.__song_box.selection_clear(0, tk.END)

        self.__song_box.selection_set(previous_s)
        self.__song_box.activate(previous_s)
        # Play previous song
        self.play()

    def delete_song(self):
        """Delet curretn song"""
        self.__song_box.delete(tk.ANCHOR)
        pygame.mixer.music.stop()

        # Clear status bar
        self.__status_bar.config(text="")

    def delete_all_songs(self):
        """Delet all songs from playlist"""
        self.__song_box.delete(0, tk.END)
        pygame.mixer.music.stop()
        # Clear status bar
        self.__status_bar.config(text="")

    def song_length(self):
        """Get duration of the song"""
        # Current time
        current_time = pygame.mixer.music.get_pos() / 1000

        # Using module 'time' to convert time to format
        converted_current_time = time.strftime("%M:%S", time.gmtime(current_time))

        # Get song path to find song's length with mutagen
        song = self.__song_box.curselection()
        song = self.__song_box.get(song)
        song = f'D:\\utorrent ustanovka\\torrents\\music\\System Of A Down\\Albums\\2001 - Toxicity\\{song}.mp3'

        song_length = MP3(song)
        song_length = song_length.info.length
        # Convert song length
        converted_song_length = time.strftime("%M:%S", time.gmtime(song_length))

        # Display and update time in status bar
        self.__status_bar.config(text=f"{converted_current_time}   out of   {converted_song_length}")
        self.__status_bar.after(1000, self.song_length)


root = tk.Tk()
root.title("WAVE")
root.geometry("500x300")
root.iconphoto(False, tk.PhotoImage(file="images\\notes_ico_Wave.png"))
root.resizable(False, False)
root.configure(bg="#E5F3FF")
# 7FC7FF
# E5F3FF

app = Mp3Player(root)

root.mainloop()
