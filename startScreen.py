from tkinter import *
from tkinter.font import BOLD

class screenLogin(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="#1B2631")
        self.master.config(bg="#17202A")
        self.master.geometry("900x600")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        
        welcomeLabel = Label(self, text="Welcome to WikiCar", fg="#ECF0F1", font=("Helveltic",20, BOLD))
        welcomeLabel.config(bg="#1B2631", height=4)
        welcomeLabel.pack()  
        
        img = PhotoImage(file='userImg.png')
        userImage = Label(self,image=img)
        userImage.pack()
                
        loginLabel = Label(self, text="Login", fg="#ECF0F1", font=("Helvetic", 22, BOLD))
        loginLabel.config(bg="#1B2631")
        loginLabel.pack()
        
        centerFrame = Frame(self)
        centerFrame.config(width=400, height=600, bg="#1B2631")
        centerFrame.pack()
        
                
        
