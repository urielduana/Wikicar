from DataConnection.mainConnection import * 

class post(dataBase):
    def __init__(self):
        dataBase.__init__(self)
        
    def getAllPostId(self):
        sql = 'SELECT Id_post FROM post'
        
        try:
            self.cursor.execute(sql)
            posts = self.cursor.fetchall()
            idSeleccion = []
            
            for post in posts:
                idSeleccion.append(post[0])
                return idSeleccion
        except Exception as e:
            raise
    
    def getLastPostId(self):
        sql = 'SELECT MAX(Id_post) as id FROM post'
        
        try:
            self.cursor.execute(sql)
            post = self.cursor.fetchone()
            
            print("Last ID", post[0])
            return post[0]
        
        except Exception as e:
            raise
        
    def addPost(self, postScore, postText, sectionId):
        sql = "INSERT INTO post(Post_date, Post_score, Post_text, Section_id) VALUES(NOW(), %s, %s, %s)"
        val = (postScore, postText, sectionId)
        
        try:
            self.cursor.execute(sql, val)
            self.connection.commit()
            
        except Exception as e:
            raise
        
    def deletePost(self, id):
        sql = "DELETE FROM post WHERE Id_post = {}".format(id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Deleted")
            
        except Exception as e:
            raise
        
    def selectAllPosts(self):
        sql = 'SELECT * FROM post'
        
        try:
            self.cursor.execute(sql)
            posts = self.cursor.fetchall()
            
            for post in posts:
                print("Fecha:", post[1])
                print("Puntuacion:", post[2])
                print(post[3])
                print("___________________\n")
        except Exception as e:
            raise
            
    def updatePostScore(self, id, score):
        sql = "UPDATE post SET Post_score = '{}' WHERE Id_post = {}".format(score, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
        
    def updatePostText(self, id, text):
        sql = "UPDATE post SET Post_text = '{}' WHERE Id_post = {}".format(text, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise 
            