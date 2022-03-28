from sectionConnection import *

class news(section):
    def __init__(self):
        section.__init__(self)
        
    def getAllNewsId(self):
        sql = 'SELECT Id_news FROM news'
        
        try:
            self.cursor.execute(sql)
            news = self.cursor.fetchall()
            idSeleccion = []
            
            for new in news:
                idSeleccion.append(news[0])
                return idSeleccion
        except Exception as e:
            raise
    
    def getLastNewsId(self):
        sql = 'SELECT MAX(Id_news) as id FROM news'
        
        try:
            self.cursor.execute(sql)
            news = self.cursor.fetchone()
            
            print("Last ID", news[0])
            return news[0]
        
        except Exception as e:
            raise
        
    def addNews(self, newsScore, newsText, newsId):
        sql = "INSERT INTO news(News_date, News_score, News_text, Section_id) VALUES(NOW(), %s, %s, %s)"
        val = (newsScore, newsText, newsId)
        
        try:
            self.cursor.execute(sql, val)
            self.connection.commit()
            
        except Exception as e:
            raise
        
    def deleteNews(self, id):
        sql = "DELETE FROM news WHERE Id_news = {}".format(id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Deleted")
            
        except Exception as e:
            raise
        
    def selectAllNews(self):
        sql = 'SELECT * FROM news'
        
        try:
            self.cursor.execute(sql)
            news = self.cursor.fetchall()
            sectionDataBase = section()
            
            for new in news:
                name = sectionDataBase.selectSectionName(new[4])
                print("Modelo:", name[1])
                print("Sección:", name[0])
                print("Fecha:", new[1])
                print("Puntuacion:", new[2])
                print(new[3])
                print("___________________\n")
        except Exception as e:
            raise
            
    def updateNewsScore(self, id, score):
        sql = "UPDATE news SET News_score = '{}' WHERE Id_news = {}".format(score, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
        
    def updateNewsText(self, id, text):
        sql = "UPDATE news SET News_text = '{}' WHERE Id_news = {}".format(text, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise 
            