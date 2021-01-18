import tkinter as tk
from tkinter import filedialog
import pygame


pygame.mixer.init()

class Mp3Player():
    """ Ui and logic of a simple mp3 player"""
    def __init__(self, root):
        """ Intitiating all ui, global variables"""

        global paused
        paused = False

        # Create playlist box
        self.__song_box = tk.Listbox(root, bg="black", fg="green", width="60", selectbackground="green", selectforeground="black")

        # Buttons icons
        self.__pause_btn_img = tk.PhotoImage(file="images\pause50.png")
        self.__play_btn_img = tk.PhotoImage(file="images\play50.png")
        self.__forward_btn_img = tk.PhotoImage(file="images\\forward50.png")
        self.__back_btn_img = tk.PhotoImage(file="images\\back50.png")
        
        # Create frame for control buttons
        self.__btn_frame = tk.Frame(root)

        # Controll buttons
        self.__back_btn = tk.Button(self.__btn_frame, image=self.__back_btn_img, borderwidth=0, command=self.previous_song)
        self.__play_btn = tk.Button(self.__btn_frame, image=self.__play_btn_img, borderwidth=0, command=self.play)
        self.__pause_btn = tk.Button(self.__btn_frame, image=self.__pause_btn_img, borderwidth=0, command=self.pause)
        self.__forward_btn = tk.Button(self.__btn_frame, image=self.__forward_btn_img, borderwidth=0, command=self.next_song)

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
        self.__remove_song_menu.add_command(label="Delete all songs from playlist", command=self.delete_all_song)

        # Display all vidgets
        self.__song_box.pack(pady=20)
        
        self.__btn_frame.pack()

        self.__back_btn.grid(row=0, column=0, padx=10)
        self.__pause_btn.grid(row=0, column=1, padx=10)
        self.__play_btn.grid(row=0, column=2, padx=10)
        self.__forward_btn.grid(row=0, column=3, padx=10)

    def add_song(self):
        """ Adds a song to the end of listbox deleting song's path and extension"""
        song = filedialog.askopenfilename(title="Choose song", filetypes=(("mp3 Files", "*.mp3"), ))
        # initialdir="D:\\utorrent ustanovka\\torrents\\music\System Of A Down\\Albums\\1998 - System of a Down", 

        # Strip out directory info and extension
        song = song.split("/")
        song = song[-1].replace(".mp3", "")

        # Add song to the end of listbox
        self.__song_box.insert(tk.END, song)

    def add_many_songs(self):
        """ Adds many songs to the end of listbox deleting songs's path and extension"""
        songs = filedialog.askopenfilenames(title="Choose songs", filetypes=(("mp3 Files", "*.mp3"), ))

        # erasing path and extension of an every song
        for song in songs:
            song = song.split("/")
            song = song[-1].replace(".mp3", "")

            # Add song to the end of listbox
            self.__song_box.insert(tk.END, song)

    def play(self):
        global paused
        """ Plays selected song from listbox"""
        
        song = self.__song_box.get(tk.ACTIVE)

        song_path = f'D:\\utorrent ustanovka\\torrents\\music\\System Of A Down\\Albums\\2001 - Toxicity\\{song}.mp3'
        try:
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play(loops=0)
            paused = False
        except:
            pass

    def pause(self):
        """ Pause and unpause current song"""
        global paused

        # Unpause
        if(paused):
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
    
    def delete_all_song(self):
        """Delet all songs from playlist"""
        self.__song_box.delete(0, tk.END)
        pygame.mixer.music.stop()

        
        

root = tk.Tk()
root.title("WAVE")
root.geometry("500x300")
# Making root not resizable
root.maxsize(500, 300)
root.minsize(500, 300)

app = Mp3Player(root)

root.mainloop()