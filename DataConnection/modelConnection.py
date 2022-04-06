from DataConnection.mainConnection import *

class model(dataBase):
    def __init__(self):
        dataBase.__init__(self)
        
    def getAllModelId(self):
        sql = 'SELECT Id_model, Model_name FROM model'
        
        try:
            self.cursor.execute(sql)
            models = self.cursor.fetchall()
            idSeleccion = []
            
            for model in models:
                idSeleccion.append(model[0])
                return idSeleccion
        
        except Exception as e:
            raise
    
    def getLastModelId(self):
        sql = 'SELECT MAX(Id_model) as id FROM model'
        
        try:
            self.cursor.execute(sql)
            model = self.cursor.fetchone()
            
            print("Last ID", model[0])
            return model[0]
        
        except Exception as e:
            raise
    
    def addModel(self, modelName, modelType, doors, seats, tankCapacity, gasType, modelYear, startingPrice, actualPrice, configuration, brandId):
        sql = "INSERT INTO model(Model_name, Model_type, Doors, Seats, GasTank_capacity, Gas_type, Model_year, Starting_price, Actual_price, Configuration, Brand_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (modelName, modelType, doors, seats, tankCapacity, gasType, modelYear, startingPrice, actualPrice, configuration, brandId)
        
        try:
            self.cursor.execute(sql, val)
            self.connection.commit()
        
        except Exception as e:
            raise
    
    def deleteModel(self, id):
        sql = "DELETE FROM model WHERE Id_model = {}".format(id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Deleted")
            
        except Exception as e:
            raise
    
    def selectModelName(self, id):
        sql = 'SELECT Model_name FROM model WHERE Id_model = {}'.format(id)
        
        try:
            self.cursor.execute(sql)
            model = self.cursor.fetchone()
            return model[0]
    
        except Exception as e:
            raise
       
    def selectModel(self, id):
        sql = 'SELECT * FROM model WHERE Id_model = {}'.format
        
        
        try:
            self.cursor.execute(sql)
            model = self.cursor.fetchone()
            
            print("Modelo:", model[1])
            print("Tipo de modelo:", model[2])
            print("No. de puertas:", model[3])
            print("No. de asientos:", model[4])
            print("Capacidad del tanque:", model[5])
            print("Tipo de gasolina:", model[6])
            print("Año:", model[7])
            print("Precio inicial:", model[8])
            print("Precio actual:", model[9])
            print("Configuracion:", model[10])
            
        except Exception as e:
            raise
        
    def selectAllModels(self):
        sql = 'SELECT * FROM model'
        
        try:
            
            self.cursor.execute(sql)
            models = self.cursor.fetchall()
            
            for model in models:
                
                print("Modelo:", model[1])
                print("Tipo de modelo:", model[2])
                print("No. de puertas:", model[3])
                print("No. de asientos:", model[4])
                print("Capacidad del tanque:", model[5])
                print("Tipo de gasolina:", model[6])
                print("Año:", model[7])
                print("Precio inicial:", model[8])
                print("Precio actual:", model[9])
                print("Configuracion:", model[10])
        
        except Exception as e:
            raise
        
    def updateModelName(self, id, name):
        sql = "UPDATE model SET Model_name = '{}' WHERE Id_model = {}".format(name, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
    
    def updateModelType(self, id, type):
        sql = "UPDATE model SET Model_type = '{}' WHERE Id_model = {}".format(type, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise               
    
    def updateModelDoors(self, id, doors):
        sql = "UPDATE model SET Doors = '{}' WHERE Id_model = {}".format(doors, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
        
    def updateModelSeats(self, id, seats):
        sql = "UPDATE model SET Seats = '{}' WHERE Id_model = {}".format(seats, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
    
    def updateModelTankCapacity(self, id, tankCapacity):
        sql = "UPDATE model SET GasTank_capacity = '{}' WHERE Id_model = {}".format(tankCapacity, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
    
    def updateModelGasType(self, id, gasType):
        sql = "UPDATE model SET Gas_type = '{}' WHERE Id_model = {}".format(gasType, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
    
    def updateModelYear(self, id, modelYear):
        sql = "UPDATE model SET Model_year = '{}' WHERE Id_model = {}".format(modelYear, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
        
    def updateModelStartingPrice(self, id, startingPrice):
        sql = "UPDATE model SET Starting_price = '{}' WHERE Id_model = {}".format(startingPrice, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
    
    def updateActualPrice(self, id, actualPrice):
        sql = "UPDATE model SET Actual_price = '{}' WHERE Id_model = {}".format(actualPrice, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
    
    def updateModelConfiguration(self, id, configuration):
        sql = "UPDATE model SET Configuration = '{}' WHERE Id_model = {}".format(configuration, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
    
    def updateModelBrand(self, id, brandId):
        sql = "UPDATE model SET Brand_id = '{}' WHERE Id_model = {}".format(brandId, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
    