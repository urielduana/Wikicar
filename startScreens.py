from tkinter import *
from DataConnection.brandConnection import brand
from brandRegisterScreen import screenBrandRegister
from loginScreen import *
from signUpsScreen import *

root = Tk()
v = screenSignUp(root)
#v = screenLogin(root)
#v = screenBrandRegister(root)
v.mainloop()
