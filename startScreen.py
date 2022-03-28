from tkinter import *

class screenLogin:
    def __init__(self, master):
        # Establecemos el tamaño de la raíz
        master.geometry("900x600")
        master.config(bg='#1B2631')
        master.title("Wikicar - Login")
        # Añadimos el botón y lo empaquetamos
        self.createWidgets()
    
    def createWidgets(self):
        centerFrame = Frame(self)
        


