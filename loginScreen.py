from tkinter import *
from tkinter.font import BOLD
from DataConnection.userConnection import *
from signUpsScreen import screenSignUp     #User database connection class

class screenLogin(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Login - WikiCar")    
        self.config(bg="#1B2631")
        self.master.config(bg="#17202A")    #Main Panel configuration and size
        self.master.geometry("900x600")
        self.pack()                     #Interface created widht pack to try to make it responsive
        self.create_widgets()           #Create widgets Initialized at the beggining of the 
                                        #class to create widgets at the same moment that we open the interface
        
        
    def loginValidation(self):          #Method to create the connection and validation of the login interface with the MySQL database and open the next window
        
        email = self.emailEntry.get()           #Variables that connect and save the strings of the email and password entries
        password = self.passwordEntry.get()
        
        tag = False                        #Boolean variable to validate if the validation is incorrect and we need to throw a message to inform it
        dataBaseConnected = user()
        
        check = dataBaseConnected.getAllUserMailPass()  
        
        for checked in check:                   #For loop to validate with the email and pass list and open a new window or throw an advise
            if checked[0] == email:
                if checked[1] == password:
                    tag = True
                    break
                else:
                    break  
                              
        if tag==False:
            errorLabel = Label(self.spaceFrameError, text="User not available", fg="#ECF0F1", font=("Helveltic",12, BOLD), bg="#1B2631")
            errorLabel.pack()       #Label to advise a login problem
    
    def openSignUp(self):
        self.master.destroy()     
        root = Tk()
        v = screenSignUp(root)
        v.mainloop()
    
    def create_widgets(self):
        
        #Main welcome labels
        welcomeLabel = Label(self, text="Welcome to WikiCar", fg="#ECF0F1", font=("Helveltic",20, BOLD))
        welcomeLabel.config(bg="#1B2631", height=4)
        welcomeLabel.pack()  
                
        bottomLoginLabel = Label(self, text="Login", fg="#ECF0F1", font=("Helvetic", 22, BOLD))
        bottomLoginLabel.config(bg="#1B2631")
        bottomLoginLabel.pack()
        
        
        #Space to add an image in a label
        imageFrame = Frame(self, width=400, height=150, bg="#1B2631")
        imageFrame.pack()
        
        
        #Frame created to contain a label and email entry
        emailFrame = Frame(self)
        emailFrame.config(bg="#1B2631")
        emailFrame.pack()
        
        emailLabel = Label(emailFrame, text="Email:", fg="#ECF0F1", font=("Helveltic",16, BOLD))
        emailLabel.config(bg="#1B2631")
        emailLabel.pack(side="left")
        self.emailEntry = Entry(emailFrame, bg="#1B2631", fg="#ECF0F1", font=("Arial",14), width=16, insertbackground="#ECF0F1")
        self.emailEntry.pack(side="right")  #"self." used to connect widgets wirh other moethods
        
        
        #Frame to create a line break
        spaceFrame = Frame(self, width=400, height=15, bg="#1B2631")
        spaceFrame.pack()
        
        
        #Frame created to contain a label and password entry
        passwordFrame = Label(self)
        passwordFrame.config(bg="#1B2631")
        passwordFrame.pack()
        
        passwordLabel = Label(passwordFrame, text="Password:", fg="#ECF0F1", font=("Helveltic",16, BOLD))
        passwordLabel.config(bg="#1B2631")
        passwordLabel.pack(side="left")
        self.passwordEntry = Entry(passwordFrame, bg="#1B2631", fg="#ECF0F1", show="*", font=("Arial",14), width=12,  insertbackground="#ECF0F1")
        self.passwordEntry.pack(side="right")
        
        
        #Frame to create a line break
        spaceFrame2 = Frame(self, width=400, height=8, bg="#1B2631")
        spaceFrame2.pack()
        
        
        
        #Frame created to contain a label and register button
        #Was created 3 frames to make it stetic and mantain the button and the label at the center
        registerFrame = Frame(self)
        registerFrame.config(bg="#1B2631")
        registerFrame.pack()
        #Frame created to contain a label inside the main registerFrame
        registerTextFrame = Frame(registerFrame)
        registerTextFrame.pack(side="left")
        #Frame created to contain a button inside the main registerFrame
        registerButtonFrame = Frame(registerFrame)
        registerButtonFrame.pack(side="right")
        
        registerLabel = Label(registerTextFrame, text="Not a member yet?", fg="#ECF0F1", font=("Helveltic",12, BOLD))
        registerLabel.config(bg="#1B2631")
        registerLabel.pack(side="left")
        self.registerButton = Button(registerButtonFrame, text="Sign Up", fg="#ECF0F1", font=("Helveltic",11, BOLD))
        self.registerButton.config(bg="#17202A", activebackground="#1B2631", activeforeground="#F8F9F9", bd=1, command=self.openSignUp)
        
        self.registerButton.pack(side="right")
        
        
        #Frame assigned to create a label to advice a login problem
        self.spaceFrameError = Frame(self, width=400, height=15, bg="#1B2631")
        self.spaceFrameError.pack()
        
        
        #Last container to the login button
        loginFrame = Frame(self)
        loginFrame.config(bg="#1B2631")
        loginFrame.pack()
        
        #Button to execute the validationLogin method
        self.loginButton = Button(loginFrame, text="Login" ,fg="#17202A", font=("Helveltic",17, BOLD), command= self.loginValidation)
        self.loginButton.config(bg="#ECF0F1", activebackground="#F8F9F9", activeforeground="#1B2631")
        self.loginButton.pack()
        
        
        #Frame used to colorized the login form 
        centerFrame = Frame(self)
        centerFrame.config(width=400, height=600, bg="#1B2631")
        centerFrame.pack()
        
                
        
