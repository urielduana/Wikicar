from tkinter import *
from tkinter.font import BOLD

class screenLogin(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.config(bg="#17202A")
        self.master.geometry("900x600")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        mainFrame= Frame(self)
        mainFrame.config(bg="#1B2631")
        mainFrame.pack()
        
        welcomeLabel = Label(mainFrame, text="Welcome to WikiCar", fg="#ECF0F1", font=("Helveltic",20, BOLD))
        welcomeLabel.config(bg="#1B2631", height=4)
        welcomeLabel.pack()     
        
        loginLabel = Label(mainFrame, text="Login", fg="#ECF0F1", font=("Helvetic", 22, BOLD))
        loginLabel.config(bg="#1B2631", height=2)
        loginLabel.pack()
        
        centerFrame = Frame(self)
        centerFrame.config(width=400, height=600, bg="#1B2631")
        centerFrame.pack()
                
        
