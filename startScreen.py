from cgitb import text
from tkinter import *
from tkinter.font import BOLD
from tkinter.ttk import Labelframe
from turtle import left, right

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
                
        bottomLoginLabel = Label(self, text="Login", fg="#ECF0F1", font=("Helvetic", 22, BOLD))
        bottomLoginLabel.config(bg="#1B2631")
        bottomLoginLabel.pack()
        
        
        emailFrame = Frame(self)
        emailFrame.config(width=400, height=50, bg="#1B2631")
        emailFrame.pack()
        
        emailLabel = Label(emailFrame, text="Email:", fg="#ECF0F1", font=("Helveltic",16, BOLD))
        emailLabel.config(bg="#1B2631")
        emailLabel.pack(side="left")
        emailEntry = Entry(emailFrame, bg="#ECF0F1",  font=("Arial",14), width=16)
        emailEntry.pack(side="right")
        
        
        passwordFrame = Label(self)
        passwordFrame.config(width=400, height=50, bg="#1B2631")
        passwordFrame.pack()
        
        passwordLabel = Label(passwordFrame, text="Password:", fg="#ECF0F1", font=("Helveltic",16, BOLD))
        passwordLabel.config(bg="#1B2631")
        passwordLabel.pack(side="left")
        passwordEntry = Entry(passwordFrame, bg="#ECF0F1", show="*", font=("Arial",14), width=12)
        passwordEntry.pack(side="right")
        
        registerFrame = Frame(self)
        registerFrame.config(width=400, height=50, bg="#1B2631")
        registerFrame.pack()
        registerTextFrame = Frame(registerFrame)
        registerTextFrame.pack(side="left")
        registerButtonFrame = Frame(registerFrame)
        registerButtonFrame.pack(side="right")
        
        registerLabel = Label(registerTextFrame, text="Not a member yet?", fg="#ECF0F1", font=("Helveltic",12, BOLD))
        registerLabel.config(bg="#1B2631")
        registerLabel.pack(side="left")
        registerButton = Button(registerButtonFrame, text="Sign Up", fg="#ECF0F1", font=("Helveltic",11, BOLD))
        registerButton.config(bg="#17202A", activebackground="#1B2631", activeforeground="#F8F9F9", bd=1)
        registerButton.pack(side="right")
        
        loginFrame = Frame(self)
        loginFrame.config(width=400, height=50, bg="#1B2631")
        loginFrame.pack()
        
        loginButton = Button(loginFrame, text="Login" ,fg="#17202A", font=("Helveltic",17, BOLD))
        loginButton.config(bg="#ECF0F1", activebackground="#F8F9F9", activeforeground="#1B2631")
        loginButton.pack()
        
        
                
        centerFrame = Frame(self)
        centerFrame.config(width=400, height=600, bg="#1B2631")
        centerFrame.pack()
        
                
        
