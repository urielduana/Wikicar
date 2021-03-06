from DataConnection.mainConnection import *


class user(dataBase):
    def __init__(self):
        dataBase.__init__(self)

    def getAllUserId(self):
        sql = 'SELECT Id_user, User_name, User_lastname FROM user'

        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()
            idSeleccion = []

            for user in users:
                #print("Nombre:", user[1], "| |", user[0])
                idSeleccion.append(user[0])
            return idSeleccion

        except Exception as e:
            raise
        
    def emailValidation(self, email):
        sql = "SELECT Id_user FROM user WHERE Email LIKE '{}'".format(email)
        try:
            self.cursor.execute(sql)
            emailValidated = self.cursor.fetchone()
            
            if emailValidated is None:
                emailBoolean = True
            else:
                emailBoolean = False
            
            return emailBoolean
        
        except Exception as e:
            raise
        
    def getAllUserMailPass(self):
        sql = 'SELECT Email, Password FROM user'
        
        try:
            self.cursor.execute(sql)
            emailPassword = self.cursor.fetchall()
            return emailPassword
        except Exception as e:
            raise
        
    

    def getLastUserId(self):
        sql = 'SELECT MAX(Id_user) as id FROM user'

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()

            print("Last ID", user[0])
            return user[0]

        except Exception as e:
            raise

    def addUser(self, nombre, apellido, Password, Email, Gender):

        sql = "INSERT INTO user(User_name, User_lastname,Password, Email, Gender) VALUES(%s,%s, %s, %s, %s)"
        val = (nombre, apellido,Password, Email, Gender)

        try:
            self.cursor.execute(sql, val)
            self.connection.commit()
        except Exception as e:
            raise

    def deleteUser(self, id):
        sql = "DELETE FROM user WHERE Id_user = {}".format(id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Deleted")
        except Exception as e:
            raise

    def selectUserName(self, id):
        sql = 'SELECT User_name, User_lastname FROM user WHERE Id_user = {}'.format(id)
        
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            
            nombreCompleto = user[0] + " " + user[1]
            return nombreCompleto
        
        except Exception as e:
            raise
                    
    def selectUser(self, id):
        sql = 'SELECT Id_user, User_name, User_lastname,Password, Email, Gender FROM user WHERE Id_user = {}'.format(
            id)

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()

            print("Id del user:", user[0])
            print("Nombre:", user[1])
            print("Apellido:", user[2])
            print("Contrase??a del user:", user[3])
            print("Email del user:", user[4])
            print("Gender del user:", user[5])

        except Exception as e:
            raise

    def selectAllUsers(self):
        sql = 'SELECT Id_user, User_name,User_lastname, Password, Email, Gender FROM user'
        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()
            for user in users:
                print("Id del user:", user[0])
                print("Nombre del user:", user[1])
                print("Apellido:", user[2])
                print("Contrase??a del user:", user[3])
                print("Email del user:", user[4])
                print("Gender del user:", user[5])
                print("___________________\n")

        except Exception as e:
            raise

    def updateUserName(self, id,  username):
        sql = "UPDATE user SET User_name='{}' WHERE Id_user = {}".format(username, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
        
    def updateUserLastName(self, id,  lastname):
        sql = "UPDATE user SET User_lastname='{}' WHERE Id_user = {}".format(lastname, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise

    def updateUserPassword(self, id, password):
        sql = "UPDATE user SET Password='{}' WHERE Id_user = {}".format(password, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise

    def updateUserMail(self, id, mail):
        sql = "UPDATE user SET Email='{}' WHERE Id_user = {}".format(mail, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise

    def updateUserGender(self, id, gender):
        sql = "UPDATE user SET Gender='{}' WHERE Id_user = {}".format(gender, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise


