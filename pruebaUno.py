from DataConnection.userConnection import *

dataBaseConnected = user()

comprueba = dataBaseConnected.getAllUserMailPass()
x="ulises@gmail.com"
y= "sger78427"

print(comprueba)
    
dataBaseConnected.close()