from RandomUserGenerator import RandomUserGenerator
from Slot import Slot
from Station import Station
from Transporter import Transporter
from User import User
from helperClasses.SiteGenerator import SiteGenerator
from helperClasses.databaseConnector import DatabaseConnector
import json

import shortuuid
from Bike import Bike

if __name__ == "__man__":
    station = Station(1, "test", "straat", "st jansplein", 4, None, "Antwerpen", 2000, True, 20)

    gen = SiteGenerator()
    gen.create_stationpage(station)

if __name__ == "__man__":

    # Create station, print slots, get available bikes
    print("station")
    station = Station(1, "test", "straat", "st jansplein", 4, None, "Antwerpen", 2000, True, 20)
    print(station.print_slots)
    print(str(station.bikes_available()) + " bikes available")

    # Create random user
    print("gen user")
    gen = RandomUserGenerator()
    user = gen.get_user()
    print(user)

    # Create transporter
    print("transporter loan")
    tr = Transporter(1, "bob", "joskes", "bob.joskes@hotmail.com", 1, 1, 50)
    print(tr)
    station.loan_bike(tr)
    print(tr.count_bikes())
    station.loan_bike(tr)
    tr.print_bikes()
    
    print("user loan")
    # User loan and return bike
    station.loan_bike(user)
    print("bike: " + str(user.get_bike()))
    station.return_bike(user)
    print("bike: " + str(user.get_bike()))

user_list = []
transporter_list = []
station_list = []

def start_over(db, am_users, am_transporters):
    # generate users and store in database
    gen = RandomUserGenerator()
    for i in range(0, am_users):
        user = gen.get_user()
        user_list.append(user)
        db.insert_user(user)

    for i in range(0, am_transporters):
        transporter = gen.get_transporter()
        transporter_list.append(transporter)
        db.insert_user(transporter)
    
    # read stations from json file and store in database
    with open("files/velo.geojson", "r") as f:
        data = json.load(f)
        data_features = data["features"]

    for feature in data_features:
        properties = feature["properties"]

        in_use = False
        if properties["Gebruik"] == "IN_GEBRUIK":
            in_use = True

        station = Station(properties["OBJECTID"], properties["Ligging"], properties["Straatnaam"], properties["Huisnummer"], properties["Aanvulling"], properties["District"], properties["Postcode"], in_use, properties["Aantal_plaatsen"])
        station.generate_slots()
        station_list.append(station)
        db.insert_station(station)

        for slot in station.slots_list:
            db.insert_slot(slot, station.uid)
            if slot.get_occupied():
                db.insert_bike(slot.get_bike())
                pass

def load_data(db):
    users = db.load_users()
    for user in users:
        if user[1] == 0:
            new_user = User(user[0], user[2], user[3], user[4], user[5], user[1])
            bikeId = user[6]
            if not bikeId == None:
                bike = db.load_bike(bikeId)
                new_bike = Bike(bike[0], bike[1])
                new_user.set_bike(new_bike)
            user_list.append(new_user)
        else:
            new_user = Transporter(user[0], user[2], user[3], user[4], user[1])
            bikeId = user[6]
            if bikeId == 1:
                bikes = db.load_bikes(user[0])
                for bike in bikes:
                    new_bike = Bike(bike[0], bike[1])
                    new_user.set_bike(new_bike)
            transporter_list.append(new_user)

    stations = db.load_stations()
    for station in stations:
        new_station = Station(station[0], station[1], station[2], station[3], station[4], station[5], station[6], station[7], station[8])
        slots = db.load_slots(station[0])
        for slot in slots:
            if not slot[2] == None:
                bike = db.load_bike(slot[2])[0]
                new_bike = Bike(bike[0], bike[1])
                new_slot = Slot(slot[0], True, new_bike)
            else:
                new_slot = Slot(slot[0], False)
            
            new_station.add_slot(new_slot)

        station_list.append(new_station)

def start_menu():
    print("Velo Antwerpen")
    print("STARTMENU")

    answered = False
    while not answered:
        start_method = input("\n1) Vorige data laden uit database \n2) Nieuwe data genereren en naar database schrijven (wist huidige informatie)\n*** optie 2 kan enkele minuten duren***\n")
        if start_method == "1":
            load_data(db)
            answered = True
        elif start_method == "2":
            confirmed = False
            while not confirmed:
                con = input("Weet u zeker dat u opnieuw wilt beginnen? Dit zal alle huidige gegevens wissen (J/N)")
                if con == "j" or con == "J":
                    am_users = input("Aantal users die u wilt toevoegen: ")
                    am_transporters = input("Aantal transporteurs die u wilt toevoegen: ")
                    start_over(db, am_users, am_transporters)
                    confirmed = True
                    answered = True
                elif con == "n" or con == "N":
                    print("nee")
                    confirmed = True


if __name__ == "__main__":
    db = DatabaseConnector()
    db.init_database()
    
    start_menu()

    db.disconnect()
