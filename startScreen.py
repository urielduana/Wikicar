from cgitb import text
import email
from tkinter import *
from tkinter.font import BOLD
from DataConnection.userConnection import *

class screenLogin(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="#1B2631")
        self.master.config(bg="#17202A")
        self.master.geometry("900x600")
        self.pack()
        self.create_widgets()
        
        
    def loginValidation(self):
        email = self.emailEntry.get()
        password = self.passwordEntry.get()
        etiqueta = False
        dataBaseConnected = user()
        comprueba = dataBaseConnected.getAllUserMailPass()
        for prueba in comprueba:
            if prueba[0] == email:
                if prueba[1] == password:
                    etiqueta = True
                    break
                else:
                    break                
        if etiqueta==False:
            errorLabel = Label(self.spaceFrameError, text="User not available", fg="#ECF0F1", font=("Helveltic",12, BOLD), bg="#1B2631")
            errorLabel.pack()
        
    def create_widgets(self):
        
        welcomeLabel = Label(self, text="Welcome to WikiCar", fg="#ECF0F1", font=("Helveltic",20, BOLD))
        welcomeLabel.config(bg="#1B2631", height=4)
        welcomeLabel.pack()  
                
        bottomLoginLabel = Label(self, text="Login", fg="#ECF0F1", font=("Helvetic", 22, BOLD))
        bottomLoginLabel.config(bg="#1B2631")
        bottomLoginLabel.pack()
        
        imageFrame = Frame(self, width=400, height=150, bg="#1B2631")
        imageFrame.pack()
        
        emailFrame = Frame(self)
        emailFrame.config(bg="#1B2631")
        emailFrame.pack()
        
        emailLabel = Label(emailFrame, text="Email:", fg="#ECF0F1", font=("Helveltic",16, BOLD))
        emailLabel.config(bg="#1B2631")
        emailLabel.pack(side="left")
        self.emailEntry = Entry(emailFrame, bg="#1B2631", fg="#ECF0F1", font=("Arial",14), width=16, insertbackground="#ECF0F1")
        self.emailEntry.pack(side="right")
        
        spaceFrame = Frame(self, width=400, height=15, bg="#1B2631")
        spaceFrame.pack()
        
        passwordFrame = Label(self)
        passwordFrame.config(bg="#1B2631")
        passwordFrame.pack()
        
        passwordLabel = Label(passwordFrame, text="Password:", fg="#ECF0F1", font=("Helveltic",16, BOLD))
        passwordLabel.config(bg="#1B2631")
        passwordLabel.pack(side="left")
        self.passwordEntry = Entry(passwordFrame, bg="#1B2631", fg="#ECF0F1", show="*", font=("Arial",14), width=12,  insertbackground="#ECF0F1")
        self.passwordEntry.pack(side="right")
        
        spaceFrame2 = Frame(self, width=400, height=8, bg="#1B2631")
        spaceFrame2.pack()
        
        registerFrame = Frame(self)
        registerFrame.config(bg="#1B2631")
        registerFrame.pack()
        registerTextFrame = Frame(registerFrame)
        registerTextFrame.pack(side="left")
        registerButtonFrame = Frame(registerFrame)
        registerButtonFrame.pack(side="right")
        
        registerLabel = Label(registerTextFrame, text="Not a member yet?", fg="#ECF0F1", font=("Helveltic",12, BOLD))
        registerLabel.config(bg="#1B2631")
        registerLabel.pack(side="left")
        self.registerButton = Button(registerButtonFrame, text="Sign Up", fg="#ECF0F1", font=("Helveltic",11, BOLD))
        self.registerButton.config(bg="#17202A", activebackground="#1B2631", activeforeground="#F8F9F9", bd=1)
        self.registerButton.pack(side="right")
        
        self.spaceFrameError = Frame(self, width=400, height=15, bg="#1B2631")
        self.spaceFrameError.pack()
        
        loginFrame = Frame(self)
        loginFrame.config(bg="#1B2631")
        loginFrame.pack()
        
        self.loginButton = Button(loginFrame, text="Login" ,fg="#17202A", font=("Helveltic",17, BOLD), command= self.loginValidation)
        self.loginButton.config(bg="#ECF0F1", activebackground="#F8F9F9", activeforeground="#1B2631")
        self.loginButton.pack()
        
        
                
        centerFrame = Frame(self)
        centerFrame.config(width=400, height=600, bg="#1B2631")
        centerFrame.pack()
        
                
        
