import pymysql

class dataBase():
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',  #'ip' en caso de ser remota
            user = 'root',
            passwd = '',
            db = 'Wikicar'
        )
        self.cursor = self.connection.cursor()
    
    def close(self):
        self.connection.close()