from userConnection import *
from brandConnection import *

class car(brand, user):
    def __init__(self):
        brand.__init__(self)
        user.__init__(self)
        
    def getAllCarId(self):
        sql = 'SELECT Id_car, Registration_plate FROM car'
        
        try:
            self.cursor.execute(sql)
            cars = self.cursor.fetchall()
            idSeleccion = []
            
            for car in cars:
                idSeleccion.append(car[0])
                return idSeleccion
            
        except Exception as e:
            raise
    
    def getLastCarId(self):
        sql = 'SELECT MAX(Id_car) as id FROM car'
        
        try:
            self.cursor.execute(sql)
            car = self.cursor.fetchone()
            
            print("Last ID", car[0])
            return car[0]
        
        except Exception as e:
            raise     
            
    def addCar(self, registrationPlate, color, deficiency, mileage, userId, brandId):
        sql = "INSERT INTO car(Registration_plate, Color, Deficiency, Mileage, User_id, Brand_id) VALUES(%s,%s, %s, %s, %s, %s)"
        val = (registrationPlate, color, deficiency, mileage, userId, brandId)
        
        try:
            self.cursor.execute(sql, val)
            self.connection.commit()
        except Exception as e:
            raise
        
    def deleteCar(self, id):
        sql = "DELETE FROM car WHERE Id_car = {}".format(id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Deleted")
        
        except Exception as e:
            raise
        
    def selectCar(self, id):
        sql = 'SELECT Id_car, Registration_plate, Color, Deficiency, Mileage, User_id, Brand_id FROM car WHERE Id_car = {}'.format(id)
        
        userDataBase = user()
        brandDataBase = brand()
        
        try:
            self.cursor.execute(sql)
            car = self.cursor.fetchone()
            
            print("Dueño:", userDataBase.selectUserName(car[5]))
            print("Placas:", car[1])
            print("Color:", car[2])
            print("Defectos:", car[3])
            print("Kilometraje:", car[4])
            print("Marca:", brandDataBase.selectBrandName(car[6]))
            
        except Exception as e:
            raise
    
    def selectAllCars(self):
        sql = 'SELECT Id_car, Registration_plate, Color, Deficiency, Mileage, User_id, Brand_id FROM car'
        try:
            self.cursor.execute(sql)
            cars = self.cursor.fetchall()
            userDataBase = user()
            brandDataBase = brand()
            
            for car in cars:
                
                print("Dueño:", userDataBase.selectUserName(car[5]))
                print("Placas:", car[1])
                print("Color:", car[2])
                print("Defectos:", car[3])
                print("Kilometraje:", car[4])
                print("Marca:", brandDataBase.selectBrandName(car[6]))
                print("___________________\n")
        except Exception as e:
            raise
            
    def updateCarPlate(self, id, plate):
        sql = "UPDATE car SET Registration_plate = '{}' WHERE Id_car = {}".format(plate, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
    
    def updateCarColor(self, id, color):
        sql = "UPDATE car SET Color = '{}' WHERE Id_car = {}".format(color, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
       
    def updateCarDeficiency(self, id, deficiency):
        sql = "UPDATE car SET Deficiency = '{}' WHERE Id_car = {}".format(deficiency, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
        
    def updateCarMileage(self, id, mileage):
        sql = "UPDATE car SET Mileage = '{}' WHERE Id_car = {}".format(mileage, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
        
    def updateCarOwnerId(self, id, ownerId):
        sql = "UPDATE car SET User_id = '{}' WHERE Id_car = {}".format(ownerId, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
        
    def updateCarBrandId(self, id, brandId):
        sql = "UPDATE car SET Brand_id = '{}' WHERE Id_car = {}".format(brandId, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
        