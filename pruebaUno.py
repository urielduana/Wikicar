from DataConnection.brandConnection import *

dataBaseConnected = brand()
x="Renault"
print(dataBaseConnected.nameValidation(x))
    
dataBaseConnected.close()