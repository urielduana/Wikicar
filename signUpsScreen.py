from tkinter import *
from tkinter.font import BOLD
from DataConnection.userConnection import *     #User database connection class

class screenSignUp(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Sign Up - WikiCar")    #Titulo de la ventana
        self.config(bg="#1B2631")
        self.master.config(bg="#17202A")    #Main Panel configuration and size
        self.master.geometry("900x600")
        self.pack()                     #Interface created widht pack to try to make it responsive
        self.create_widgets()           #Create widgets Initialized at the beggining of the 
                                        #class to create widgets at the same moment that we open the interface
        
        
    def passwordValidation(self):
        if len(self.passwordEntry.get()) >= 8:        
            if self.passwordEntry.get() == self.repeatedpassEntry.get():
                print("Coincide")
                self.emailValidation()
            else:
                errorLabel = Label(self.spaceFrameError, text="The password doesn't match", fg="#ECF0F1", font=("Helveltic",12, BOLD), bg="#1B2631")
                errorLabel.pack()       #Label to advise a login problem
        else:
            errorLabel = Label(self.spaceFrameError, text="Empty Field", fg="#ECF0F1", font=("Helveltic",12, BOLD), bg="#1B2631")
            errorLabel.pack()
    
    def emailValidation(self):
        if len(self.emailEntry.get()) > 0:
            email = self.emailEntry.get()           #Variables that connect and save the strings of the email and password entries
                    
            tag = False                        #Boolean variable to validate if the validation is incorrect and we need to throw a message to inform it
            dataBaseConnected = user()
            
            check = dataBaseConnected.getAllUserMailPass()  
            for checked in check:                   #For loop to validate with the email and pass list and open a new window or throw an advise
                if checked[0] == email:
                    tag = False
                    break
                else:
                    tag=True
            if tag==False:
                errorLabel = Label(self.spaceFrameError, text="Email not available", fg="#ECF0F1", font=("Helveltic",12, BOLD), bg="#1B2631")
                errorLabel.pack()
            if tag == True:
                self.userRegister()

        else:
            errorLabel = Label(self.spaceFrameError, text="Empty Field - use + 8 characters", fg="#ECF0F1", font=("Helveltic",12, BOLD), bg="#1B2631")
            errorLabel.pack()
            
            
    def userRegister(self):
        if (len(self.nameEntry.get())>0) or (len(self.lastnameEntry.get())>0) or (len(self.genderEntry.get())>0):
            
            dataBaseConnected = user()
            dataBaseConnected.addUser(self.nameEntry.get(),self.lastnameEntry.get(), self.passwordEntry.get(), self.emailEntry.get(), self.genderEntry.get())
            print("completo")
        else:
            errorLabel = Label(self.spaceFrameError, text="Empty Field - use + 8 characters", fg="#ECF0F1", font=("Helveltic",12, BOLD), bg="#1B2631")
            errorLabel.pack()
                                 
                
    def create_widgets(self):
        
        #Main welcome labels
        welcomeLabel = Label(self, text="Welcome to WikiCar", fg="#ECF0F1", font=("Helveltic",20, BOLD), bg="#1B2631", height=4)
        welcomeLabel.pack()  
                
        bottomLoginLabel = Label(self, text="Sign Up", fg="#ECF0F1", font=("Helvetic", 22, BOLD), bg="#1B2631")
        bottomLoginLabel.pack()
        
        
        spaceFrame = Frame(self, width=400, height=50, bg="#1B2631")
        spaceFrame.pack()        
        
        
        nameFrame = Frame(self, bg="#1B2631")
        nameFrame.pack()
        
        nameLabel = Label(nameFrame, text="Name:", fg="#ECF0F1", font=("Helveltic",16, BOLD), bg="#1B2631")
        nameLabel.pack(side="left")
        self.nameEntry = Entry(nameFrame, bg="#1B2631", fg="#ECF0F1", font=("Arial",14), width=19, insertbackground="#ECF0F1")
        self.nameEntry.pack(side="right")
        
        
        spaceFrame = Frame(self, width=400, height=15, bg="#1B2631")
        spaceFrame.pack()
        
        
        lastnameFrame = Frame(self, bg="#1B2631")
        lastnameFrame.pack()
        
        lastnameLabel = Label(lastnameFrame, text="Last Name:", fg="#ECF0F1", font=("Helveltic",16, BOLD), bg="#1B2631")
        lastnameLabel.pack(side="left")
        self.lastnameEntry = Entry(lastnameFrame, bg="#1B2631", fg="#ECF0F1", font=("Arial",14), width=15, insertbackground="#ECF0F1")
        self.lastnameEntry.pack(side="right")
        
        
        spaceFrame = Frame(self, width=400, height=15, bg="#1B2631")
        spaceFrame.pack()
        
        
        #Frame created to contain a label and email entry
        emailFrame = Frame(self, bg="#1B2631")
        emailFrame.pack()
        
        emailLabel = Label(emailFrame, text="Email:", fg="#ECF0F1", font=("Helveltic",16, BOLD), bg="#1B2631")
        emailLabel.pack(side="left")
        self.emailEntry = Entry(emailFrame, bg="#1B2631", fg="#ECF0F1", font=("Arial",14), width=20, insertbackground="#ECF0F1")
        self.emailEntry.pack(side="right")  #"self." used to connect widgets wirh other moethods
        
        
        #Frame to create a line break
        spaceFrame = Frame(self, width=400, height=15, bg="#1B2631")
        spaceFrame.pack()
        
        
        #Frame created to contain a label and password entry
        passwordFrame = Label(self, bg="#1B2631")
        passwordFrame.pack()
        
        passwordLabel = Label(passwordFrame, text="Password:", fg="#ECF0F1", font=("Helveltic",16, BOLD), bg="#1B2631")
        passwordLabel.pack(side="left")
        self.passwordEntry = Entry(passwordFrame, bg="#1B2631", fg="#ECF0F1", show="*", font=("Arial",14), width=16,  insertbackground="#ECF0F1")
        self.passwordEntry.pack(side="right")
        
        
        #Frame to create a line break
        spaceFrame2 = Frame(self, width=400, height=8, bg="#1B2631")
        spaceFrame2.pack()
        
        
        repeatedpassFrame = Label(self, bg="#1B2631")
        repeatedpassFrame.pack()
        
        repeatedpassLabel = Label(repeatedpassFrame, text="Repeat\nPassword:", fg="#ECF0F1", font=("Helveltic",12, BOLD), bg="#1B2631")
        repeatedpassLabel.pack(side="left")
        self.repeatedpassEntry = Entry(repeatedpassFrame, bg="#1B2631", fg="#ECF0F1", show="*", font=("Arial",14), width=18,  insertbackground="#ECF0F1")
        self.repeatedpassEntry.pack(side="right")
        
        
        spaceFrame2 = Frame(self, width=400, height=8, bg="#1B2631")
        spaceFrame2.pack()
        
        
        genderFrame = Label(self, bg="#1B2631")
        genderFrame.pack()
        
        genderLabel = Label(genderFrame, text="Gender:", fg="#ECF0F1", font=("Helveltic",12, BOLD), bg="#1B2631")
        genderLabel.pack(side="left")
        self.genderEntry = Entry(genderFrame, bg="#1B2631", fg="#ECF0F1", font=("Arial",14), width=20,  insertbackground="#ECF0F1")
        self.genderEntry.pack(side="right")
        
        
        #Frame assigned to create a label to advice a login problem
        self.spaceFrameError = Frame(self, width=400, height=15, bg="#1B2631")
        self.spaceFrameError.pack()
        
        
        #Last container to the login button
        loginFrame = Frame(self, bg="#1B2631")
        loginFrame.pack()
        
        #Button to execute the validationLogin method
        self.signUpButton = Button(loginFrame, text="Sign Up" ,fg="#17202A", font=("Helveltic",17, BOLD), command= self.passwordValidation)
        self.signUpButton.config(bg="#ECF0F1", activebackground="#F8F9F9", activeforeground="#1B2631")
        self.signUpButton.pack()
        
        
        #Frame used to colorized the login form 
        centerFrame = Frame(self, width=400, height=600, bg="#1B2631")
        centerFrame.pack()
        
                
        
