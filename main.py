import tkinter as tk
from tkinter import filedialog
import pygame


pygame.mixer.init()

class Mp3Player():
    # Ui and logic of a simple mp3 player
    def __init__(self, root):
        # Intitiating all ui

        # Create playlist box
        #bg="black", fg="green"
        self.__song_box = tk.Listbox(root, bg="black", fg="green", width="60", selectbackground="green", selectforeground="black")

        # Buttons icons
        self.__stop_btn_img = tk.PhotoImage(file="images\stop50.png")
        self.__play_btn_img = tk.PhotoImage(file="images\play50.png")
        self.__forward_btn_img = tk.PhotoImage(file="images\\forward50.png")
        self.__back_btn_img = tk.PhotoImage(file="images\\back50.png")
        
        # Create frame for control buttons
        self.__btn_frame = tk.Frame(root)

        # Controll buttons
        self.__back_btn = tk.Button(self.__btn_frame, image=self.__back_btn_img, borderwidth=0)
        self.__play_btn = tk.Button(self.__btn_frame, image=self.__play_btn_img, borderwidth=0)
        self.__stop_btn = tk.Button(self.__btn_frame, image=self.__stop_btn_img, borderwidth=0)
        self.__forward_btn = tk.Button(self.__btn_frame, image=self.__forward_btn_img, borderwidth=0)

        # Create menu
        self.__main_menu = tk.Menu(root)
        root.config(menu=self.__main_menu)

        # Create 'Add song' menu
        self.__add_song_menu = tk.Menu(self.__main_menu)
        self.__main_menu.add_cascade(label="Add songs", menu=self.__add_song_menu)
        self.__add_song_menu.add_command(label="Add 1 song to playlist", command=self.add_song)

        # Display all vidgets
        self.__song_box.pack(pady=20)
        
        self.__btn_frame.pack()

        self.__back_btn.grid(row=0, column=0, padx=10)
        self.__stop_btn.grid(row=0, column=1, padx=10)
        self.__play_btn.grid(row=0, column=2, padx=10)
        self.__forward_btn.grid(row=0, column=3, padx=10)

    def add_song(self):
        # You can change an 'initialdir' on your folder with music
        song = filedialog.askopenfilename(initialdir='audio/', title="Choose song", filetypes=(("mp3 Files", "*.mp3"), ))

        # Strip out directory info and extension
        song = song.split("/")
        song = song[-1].replace(".mp3", "")

        # Add song to the end of listbox
        self.__song_box.insert(tk.END, song)

        
    

root = tk.Tk()
root.title("WAVE")
root.geometry("500x300")
# Making root not resizable
root.maxsize(500, 300)
root.minsize(500, 300)

app = Mp3Player(root)

root.mainloop()