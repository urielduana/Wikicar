from DataConnection.userConnection import *

dataBaseConnected = user()

comprueba = dataBaseConnected.getAllUserMailPass()
x="ulises@gmail.com"
y= "sger78427"

for prueba in comprueba:
    print(prueba)
    if prueba[0] == x:
        print("coincide")
        if prueba[1] == y:
            print("login correcto")
        else:
            print("NO LOGIN")
    else:
        print("no coincide")
    
dataBaseConnected.close()