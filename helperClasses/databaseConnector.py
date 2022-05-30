import sqlite3
import os
ROOT_DIR = os.path.dirname(os.path.abspath("App.py"))

class DatabaseConnector():
    def __init__(self):
        self.conn = sqlite3.connect(ROOT_DIR + "/files/velo.db")
        self.curs = self.conn.cursor()

    def init_database(self):
        self.curs.execute("""CREATE TABLE IF NOT EXISTS velo.users(
   uid INT PRIMARY KEY NOT NULL,
   fname TEXT NOT NULL,
   lname TEXT NOT NULL,
   email TEXT NOT NULL,
   subscribed INT,   
   active INT,
   bikeId INT
   );""")

    def disconnect(self):
        self.curs.close()
        self.conn.close()