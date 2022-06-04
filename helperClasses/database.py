import sqlite3
import os
ROOT_DIR = os.path.dirname(os.path.abspath("App.py"))

class Database():
    def __init__(self):
        self.conn = sqlite3.connect(ROOT_DIR + "/files/velo.db")
        self.curs = self.conn.cursor()

    def init_database(self):
        self.curs.execute("""CREATE TABLE IF NOT EXISTS users(
            uid INT PRIMARY KEY NOT NULL,
            transporter INT NOT NULL,
            fname TEXT NOT NULL,
            lname TEXT NOT NULL,
            email TEXT NOT NULL,
            subscribed INT NOT NULL,   
            bikeId INT
        );""")

        self.curs.execute("""CREATE TABLE IF NOT EXISTS stations(
            uid INT PRIMARY KEY NOT NULL,
            position TEXT,
            street TEXT NOT NULL,
            number INT,
            addition TEXT,
            district INT NOT NULL,
            postalCode INT NOT NULL,
            inUse INT NOT NULL,
            capacity INT NOT NULL
        );""")

        self.curs.execute("""CREATE TABLE IF NOT EXISTS slots(
            slotIndex INT NOT NULL,
            stationId INT NOT NULL,
            bikeId INT
        );""")

        self.curs.execute("""CREATE TABLE IF NOT EXISTS bikes(
            uid INT PRIMARY KEY NOT NULL,
            inUse INT NOT NULL
        );""")

        self.curs.execute("""CREATE TABLE IF NOT EXISTS userBikeLink(
            userId INT NOT NULL,
            bikeId INT NOT NULL
        );""")

    def insert_user(self, user):
        bike = user.bike
        if user.transporter:
            if user.count_bikes() > 0:
                self.insert_user_bike_link(user)
                user_data = (user.uid, user.transporter, user.fname, user.lname, user.email, user.subscribed, 1)
            else:
                user_data = (user.uid, user.transporter, user.fname, user.lname, user.email, user.subscribed, None)
            self.curs.execute("INSERT INTO users (uid, transporter, fname, lname, email, subscribed, bikeId) VALUES (?, ?, ?, ?, ?, ?, ?)", user_data)
        else:
            if bike == None:
                uid = None
            else:
                uid = bike.uid
            user_data = (user.uid, user.transporter, user.fname, user.lname, user.email, user.subscribed, uid)
            self.curs.execute("INSERT INTO users (uid, transporter, fname, lname, email, subscribed, bikeId) VALUES (?, ?, ?, ?, ?, ?, ?)", user_data)
        self.conn.commit()

    def insert_user_bike_link(self, user):
        for bike in user.get_bike_list():
            link_data = (user.uid, bike.uid)
            self.curs.execute("INSERT INTO userBikeLink(userId, bikeId) VALUES(?, ?)", link_data)
            self.conn.commit()

    def load_users(self):
        users = self.curs.execute("SELECT * FROM users;")
        return users.fetchall()

    def insert_station(self, station):
        station_data = (station.uid, station.position, station.street, station.number, station.addition, station.district, station.postal_code, station.in_use, station.capacity)
        self.curs.execute("INSERT INTO stations (uid, position, street, number, addition, district, postalCode, inUse, capacity) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);", station_data)
        self.conn.commit()

    def load_stations(self):
        stations = self.curs.execute("SELECT * FROM stations;")
        return stations.fetchall()  
    
    def insert_slot(self, slot, station_id):
        bike = slot.get_bike()
        if bike == None:
            uid = None
        else:
            uid = bike.uid
        slot_data = (slot.index, station_id, uid)
        self.curs.execute("INSERT INTO slots (slotIndex, stationId, bikeId) VALUES(?, ?, ?);", slot_data)
        self.conn.commit()

    def load_slots(self, stationId):
        slots = self.curs.execute("SELECT * FROM slots WHERE stationId = ?;", (stationId,))
        return slots.fetchall()  

    def insert_bike(self, bike):
        bike_data = (bike.uid, bike.in_use)
        self.curs.execute("INSERT INTO bikes (uid, inUse) VALUES(?, ?);", bike_data)
        self.conn.commit()

    def load_bike(self, uid):
        bike = self.curs.execute("SELECT * FROM bikes WHERE uid = ?", (uid,))
        return bike.fetchall()

    def load_bikes(self, userId):
        bikes = self.curs.execute("SELECT * FROM userBikeLink WHERE userId = ?", (userId,))
        return bikes.fetchall()

    def disconnect(self):
        self.curs.close()
        self.conn.close()
        
