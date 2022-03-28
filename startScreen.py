from tkinter import *

class screenLogin(Frame):
    def __init__(self, master):
        super().__init__(master)    #Inicializa el frame
        self.master.title("WikiCar - Login")    #Titulo de la ventana
        self.master.resizable(width=False, height=False)    #Permite o no que la ventana cambie de tamano
        self.master.geometry("900x600") #Configura el tamano de la ventana
        self.master.config(bg='#17202A')  #Color de fondo
        self.config(width=400, height=600, bg="#1B2631")
        self.pack()
        self.createWidget()
        
    def createWidget(self):
        self.welcomeLabel= Label(self, text="Welcome to WikiCar", fg="#ECF0F1", font='Arial 20 bold')
        self.welcomeLabel.place(y=40)
        self.welcomeLabel.config(bg="#1B2631")