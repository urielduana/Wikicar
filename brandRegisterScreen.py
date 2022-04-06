from tkinter import *
from tkinter.font import BOLD
from DataConnection.brandConnection import *

class screenBrandRegister(Frame, brand):
    def __init__(self, master):       
        super().__init__(master)
        self.master.title("Brand Register - WikiCar")    
        self.master.config(bg="#17202A")    #Main Panel configuration and size
        self.master.geometry("1200x800")
        self.config(bg="#1B2631")
        self.pack(side="right")                     #Interface created widht pack to try to make it responsive
        self.create_widgets()           #Create widgets Initialized at the beggining of the 
                                        #class to create widgets at the same moment that we open the interface
        
    def brandValidation(self):
        if len(self.brandEntry.get()) > 0:
            brands = self.brandEntry.get()         #Variables that connect and save the strings of the brand and password entries
                    
            dataBaseConnected = brand()
            
            validatedBoolen = dataBaseConnected.nameValidation(brands)  
                    
                    
            if validatedBoolen==False:
                self.errorLabel.config(text="Brand already registered")
            else:
                self.brandRegister()

        else:
            self.errorLabel.config(text="Empty Field")
    
    
    def getTextHistory(self):
        text = self.historyEntry.get(1.0, END+"-1c")
        return text
    
    def brandRegister(self):
        historyText = self.getTextHistory()
        
        if (len(self.foundersEntry.get())>0) and (len(self.foundersDayEntry.get())>0) and (len(self.foundersMonthEntry.get())>0) and (len(self.foundersYearEntry.get())>0) and (len(self.countryEntry.get())>0) and (len(historyText)>0):
            dataBaseConnected = brand()
            date = self.foundersYearEntry.get() + "-" + self.foundersMonthEntry.get() + "-" + self.foundersDayEntry.get()
            
            
            dataBaseConnected.addBrand(self.brandEntry.get(), self.foundersEntry.get(), date, self.countryEntry.get(), historyText)
            print("Completo")
        else:
            self.errorLabel.config(text="Empty Field")
    
    
    def create_widgets(self):
        
        welcomeLabel = Label(self, text="New Brand Registration", fg="#ECF0F1", font=("Helveltic",26, BOLD))
        welcomeLabel.config(bg="#1B2631", height=4)
        welcomeLabel.pack()  
             
        bottomLoginLabel = Label(self, text="If the brand is already register, you cannot add it. \nPlease, don't be rude :D", fg="#ECF0F1", font=("Helvetic", 13, BOLD))
        bottomLoginLabel.config(bg="#1B2631")
        bottomLoginLabel.pack()
        
        spaceFrame = Frame(self, width=400, height=15, bg="#1B2631")
        spaceFrame.pack()


        brandFrame = Frame(self)
        brandFrame.config(bg="#1B2631")
        brandFrame.pack()
        
        brandLabel = Label(brandFrame, text="Brand Name:", fg="#ECF0F1", font=("Helveltic",16, BOLD))
        brandLabel.config(bg="#1B2631")
        brandLabel.pack(side="left")
        self.brandEntry = Entry(brandFrame, bg="#1B2631", fg="#ECF0F1", font=("Arial",14), width=16, insertbackground="#ECF0F1")
        self.brandEntry.pack(side="right")  #"self." used to connect widgets wirh other moethods
        
        
        
        #Frame to create a line break
        spaceFrame = Frame(self, width=400, height=15, bg="#1B2631")
        spaceFrame.pack()
        
        #Frame created to contain a label and password entry
        foundersFrame = Label(self)
        foundersFrame.config(bg="#1B2631")
        foundersFrame.pack()
        
        foundersLabel = Label(foundersFrame, text="Founders:", fg="#ECF0F1", font=("Helveltic",16, BOLD))
        foundersLabel.config(bg="#1B2631")
        foundersLabel.pack(side="left")
        self.foundersEntry = Entry(foundersFrame, bg="#1B2631", fg="#ECF0F1", font=("Arial",14), width=12,  insertbackground="#ECF0F1")
        self.foundersEntry.pack(side="right")



        #Frame to create a line break
        spaceFrame = Frame(self, width=400, height=15, bg="#1B2631")
        spaceFrame.pack()

        dateFoundationFrame = Label(self)
        dateFoundationFrame.config(bg="#1B2631")
        dateFoundationFrame.pack()
        
        foundersLabel = Label(dateFoundationFrame, text="Foundation Date:", fg="#ECF0F1", font=("Helveltic",16, BOLD), bg="#1B2631")
        foundersLabel.pack(side="left")
        foundersDayLabel = Label(dateFoundationFrame, text="Day", fg="#ECF0F1", font=("Helveltic",12, BOLD), bg="#1B2631")
        foundersDayLabel.pack(side="left")
        self.foundersDayEntry = Entry(dateFoundationFrame, bg="#1B2631", fg="#ECF0F1", font=("Arial",14), width=4,  insertbackground="#ECF0F1")
        self.foundersDayEntry.pack(side="left")
        foundersMonthLabel = Label(dateFoundationFrame, text="Month", fg="#ECF0F1", font=("Helveltic",12, BOLD), bg="#1B2631")
        foundersMonthLabel.pack(side="left")
        self.foundersMonthEntry = Entry(dateFoundationFrame, bg="#1B2631", fg="#ECF0F1", font=("Arial",14), width=4,  insertbackground="#ECF0F1")
        self.foundersMonthEntry.pack(side="left")
        foundersYearLabel = Label(dateFoundationFrame, text="Year", fg="#ECF0F1", font=("Helveltic",12, BOLD), bg="#1B2631")
        foundersYearLabel.pack(side="left")
        self.foundersYearEntry = Entry(dateFoundationFrame, bg="#1B2631", fg="#ECF0F1",font=("Arial",14), width=4,  insertbackground="#ECF0F1")
        self.foundersYearEntry.pack(side="left")
        
        
        
        #Frame to create a line break
        spaceFrame = Frame(self, width=400, height=15, bg="#1B2631")
        spaceFrame.pack()
        
        #Frame created to contain a label and password entry
        countryFrame = Label(self)
        countryFrame.config(bg="#1B2631")
        countryFrame.pack()
        
        countryLabel = Label(countryFrame, text="Country:", fg="#ECF0F1", font=("Helveltic",16, BOLD))
        countryLabel.config(bg="#1B2631")
        countryLabel.pack(side="left")
        self.countryEntry = Entry(countryFrame, bg="#1B2631", fg="#ECF0F1", font=("Arial",14), width=12,  insertbackground="#ECF0F1")
        self.countryEntry.pack(side="right")
        
        
        
        #Frame to create a line break
        spaceFrame = Frame(self, width=400, height=15, bg="#1B2631")
        spaceFrame.pack()
        
        #Frame created to contain a label and password entry
        historyFrame = Label(self, bg="#1B2631")
        historyFrame.pack()
        
        historyLabel = Label(historyFrame, text="Brand history:", fg="#ECF0F1", font=("Helveltic",16, BOLD), bg="#1B2631")
        historyLabel.pack(side="left")
        self.historyEntry = Text(historyFrame, bg="#1B2631", fg="#ECF0F1", font=("Arial",11), insertbackground="#ECF0F1", width=50, height=8)
        self.historyEntry.pack(side="right")
        #self.historyEntry = Entry(historyFrame, bg="#1B2631", fg="#ECF0F1", font=("Arial",14), width=12, insertbackground="#ECF0F1")
        #self.historyEntry.pack(side="right")
        
        
        #Frame to create a line break
        spaceFrame2 = Frame(self, width=400, height=8, bg="#1B2631")
        spaceFrame2.pack()
        
        #Frame assigned to create a label to advice a login problem
        self.spaceFrameError = Frame(self, width=400, height=15, bg="#1B2631")
        self.spaceFrameError.pack()
        self.errorLabel = Label(self.spaceFrameError, fg="#ECF0F1", font=("Helveltic",12, BOLD), bg="#1B2631")
        self.errorLabel.pack()
        
        
        #Last container to the login button
        registerFrame = Frame(self)
        registerFrame.config(bg="#1B2631")
        registerFrame.pack()
        
        #Button to execute the validationLogin method
        self.registerButton = Button(registerFrame, text="Register" ,fg="#17202A", font=("Helveltic",17, BOLD), command= self.brandValidation)
        self.registerButton.config(bg="#ECF0F1", activebackground="#F8F9F9", activeforeground="#1B2631")
        self.registerButton.pack()
        
        
        #Frame used to colorized the login form 
        centerFrame = Frame(self)
        centerFrame.config(width=850, height=750, bg="#1B2631")
        centerFrame.pack()
        
                
        
