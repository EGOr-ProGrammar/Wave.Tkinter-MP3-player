import tkinter as tk

class Mp3Player():
    # Ui and logic of a simple mp3 player
    def __init__(self, root):
        self.root = root
        self.init_ui()

    def init_ui(self):

        # Intitiating all ui

        # Create playlist box
        self.song_box = tk.Listbox(self.root, bg="black", fg="green", width="60")

        # Buttons icons
        self.stop_btn_img = tk.PhotoImage(file="images\stop50.png")
        self.play_btn_img = tk.PhotoImage(file="images\play50.png")
        self.forward_btn_img = tk.PhotoImage(file="images\\forward50.png")
        self.back_btn_img = tk.PhotoImage(file="images\\back50.png")
        
        # Create frame for control buttons
        self.btn_frame = tk.Frame()

        # Controll buttons
        self.back_btn = tk.Button(self.btn_frame, image=self.back_btn_img, borderwidth=0)
        self.play_btn = tk.Button(self.btn_frame, image=self.play_btn_img, borderwidth=0)
        self.stop_btn = tk.Button(self.btn_frame, image=self.stop_btn_img, borderwidth=0)
        self.forward_btn = tk.Button(self.btn_frame, image=self.forward_btn_img, borderwidth=0)


        # Display all vidgets
        self.song_box.pack(pady=20)
        
        self.btn_frame.pack()

        self.back_btn.grid(row=0, column=0, padx=10)
        self.stop_btn.grid(row=0, column=1, padx=10)
        self.play_btn.grid(row=0, column=2, padx=10)
        self.forward_btn.grid(row=0, column=3, padx=10)

        
    

root = tk.Tk()
root.title("WAVE")
root.geometry("500x300")
# Making root not resizable
root.maxsize(500, 300)
root.minsize(500, 300)

app = Mp3Player(root)


root.mainloop()