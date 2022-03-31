from mainConnection import *

class brand(dataBase):
    def __init__(self):
        dataBase.__init__(self)
        
    def getAllBrandId(self):
        sql = 'SELECT Id_brand, Brand_name FROM brand'
        
        try:
            self.cursor.execute(sql)
            brands = self.cursor.fetchall()
            idSeleccion = []
            
            for brand in brands:
                idSeleccion.append(brand[0])
            return idSeleccion
        
        except Exception as e:
            raise
    
    def getLastBrandId(self):
        sql = 'SELECT MAX(Id_brand) as id FROM brand'

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            
            print("Last ID", user[0])
            return user[0]
            
        except Exception as e:
            raise
    
    def addBrand(self,nombre, Founders, fechaFundacion, paisOrigen, historiabrand):
        sql = "INSERT INTO brand(Brand_name, Founders, Foundation_date, Country, Brand_history) VALUES(%s,%s, %s, %s, %s)"
        val = (nombre, Founders, fechaFundacion, paisOrigen, historiabrand)  
        
        try:
            self.cursor.execute(sql, val)
            self.connection.commit()
        except Exception as e:
            raise
        
    def deleteBrand(self, id):
        sql = "DELETE FROM brand WHERE Id_brand = {}".format(id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Deleted")
            
        except Exception as e:
            raise
    
    def selectBrandName(self, id):
        sql = 'SELECT Brand_name FROM brand WHERE Id_brand = {}'.format(id)
        
        try:
            self.cursor.execute(sql)
            brand = self.cursor.fetchone()
            return brand[0]
        
        except Exception as e:
            raise
        
    def selectBrand(self, id):
        sql = 'SELECT Id_brand, Brand_name, Founders, Foundation_date, Country, Brand_history FROM brand WHERE Id_brand = {}'.format(id)
        
        try:
            self.cursor.execute(sql)
            brand = self.cursor.fetchone()
            
            print("Id de la brand:", brand[0])
            print("Nombre de la brand:", brand[1])
            print("Founders de la brand:", brand[2])
            print("Fecha de la fundacion:", brand[3])
            print("Pais de origen:", brand[4])
            print("Historia:", brand[5])
            
            
        except Exception as e:
            raise
    
    def selectAllUsers(self):
        sql = 'SELECT Id_brand, Brand_name, Founders, Foundation_date, Country, Brand_history FROM brand'
        
        try:
            self.cursor.execute(sql)
            brands = self.cursor.fetchall()
            for brand in brands:
                print("Id de la brand:", brand[0])
                print("Nombre de la brand:", brand[1])
                print("Founders de la brand:", brand[2])
                print("Fecha de la fundacion:", brand[3])
                print("Pais de origen:", brand[4])
                print("Historia:", brand[5])
                print("___________________\n")
                
        except Exception as e:
            raise
    
    def updateBrandName(self, id, nombre):
        sql = "UPDATE brand SET Brand_name = '{}' WHERE Id_brand = '{}'".format(nombre, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
    
    def updateBrandFounder(self, id, Founders):
        sql = "UPDATE brand SET Brand_name = '{}' WHERE Founders = '{}'".format(Founders, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
        
    def updateBrandDate(self, id, date):
        sql = "UPDATE brand SET Foundation_date = '{}' WHERE Id_brand = '{}'".format(date, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
    
    def updateBrandCountry(self, id, country):
        sql = "UPDATE brand SET Country '{}' WHERE Id_brand = '{}'".format(country, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
    
    def updateBrandHistory(self, id, history):
        sql = "UPDATE brand SET Brand_history = '{}' WHERE Id_brand = '{}'".format(history, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise