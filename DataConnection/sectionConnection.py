from DataConnection.mainConnection import *

class section(dataBase):
    def __init__(self):
        dataBase.__init__(self)
        
    def getAllSectionId(self):
        sql = 'SELECT Id_section, Section_type FROM section '
        
        try:
            self.cursor.execute(sql)
            sections = self.cursor.fetchall()
            idSeleccion = []
            
            for section in sections:
                idSeleccion.append(section[0])
                return idSeleccion
        except Exception as e:
            raise
            
    def getLastSectionId(self):
        sql = 'SELECT MAX(Id_section) as id FROM section'
        
        try:
            self.cursor.execute(sql)
            section = self.cursor.fetchone()
            
            print("Last ID", section[0])
            return section[0]
        
        except Exception as e:
            raise
    
    def addSection(self, sectionName, modelId):
        sql = "INSERT INTO section(Creation_date, Section_type, Model_id) VALUES(NOW(), %s, %s)"
        val = (sectionName, modelId)
        
        try:
            self.cursor.execute(sql, val)
            self.connection.commit()
        except Exception as e:
            raise
    
    def deleteSection(self, id):
        sql = "DELETE FROM selection WHERE Id_section = {}".format(id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Deleted")
        
        except Exception as e:
            raise    
    
    def selectSectionName(self, id):
        sql = 'SELECT Section_type, Model_id FROM section WHERE Id_section = {}'.format(id)
        try:
            self.cursor.execute(sql)
            section = self.cursor.fetchone()
            sectionNameModel = section[0]
            return sectionNameModel
        except Exception as e:
            raise
        
    def selectAllSections(self):
        sql = 'SELECT * FROM section'
        
        try:
            self.cursor.execute(sql)
            sections = self.cursor.fetchall()
            
            for section in sections:
                print("Nombre de la secci??n:", section[2])
                print("Fecha de creaci??n:", section[1])
                print("___________________\n")
        except Exception as e:
            raise
        
    def updateSectionName(self, id, sectionName):
        sql = "UPDATE section SET Section_type = '{}' WHERE Id_section = {}".format(sectionName, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise        