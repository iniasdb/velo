from random import random, randint
import sys
from time import sleep
import json

from RandomUserGenerator import RandomUserGenerator
from Slot import Slot
from Station import Station
from Transporter import Transporter
from User import User
from Bike import Bike
from helperClasses.SiteGenerator import SiteGenerator
from helperClasses.database import Database
from helperClasses.logger import Logger


if __name__ == "__man__":
    station = Station(1, "straat", "st jansplein", 4, None, "Antwerpen", 2000, True, 20)

    gen = SiteGenerator()
    gen.create_stationpage(station)

user_list = []
active_user_list = {}
transporter_list = []
active_transporter_list = {}
station_list = []
low_station_list = []
overflow_station_list = []
relocation_list = []

logger = Logger(5, True, True)

def start_over(db, am_users, am_transporters):
    db.clear()

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

    db.commit()
    
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
    db.commit()

def load_data(db):
    users = db.load_users()
    for user in users:
        if user[1] == 0:
            new_user = User(user[0], user[2], user[3], user[4], user[5], user[1])
            bikeId = user[6]
            if not bikeId == None:
                bike = db.load_bike(bikeId)[0]
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

def start_menu(load):
    print("Velo Antwerpen")
    print("STARTMENU")

    if load:
        answered = False
        while not answered:
            start_method = input("\n1) Vorige data laden uit database \n2) Nieuwe data genereren en naar database schrijven (wist huidige informatie)\n")
            if start_method == "1":
                load_data(db)
                answered = True
            elif start_method == "2":
                confirmed = False
                while not confirmed:
                    con = input("Weet u zeker dat u opnieuw wilt beginnen? Dit zal alle huidige gegevens wissen (J/N)")
                    if con == "j" or con == "J":
                        am_users = int(input("Aantal users die u wilt toevoegen: "))
                        am_transporters = int(input("Aantal transporteurs die u wilt toevoegen: "))
                        start_over(db, am_users, am_transporters)
                        confirmed = True
                        answered = True
                    elif con == "n" or con == "N":
                        confirmed = True
    else:
        answered = False
        while not answered:
            start_method = input("\nEr staat op deze moment nog niets in de database\n1) Nieuwe data genereren en naar database schrijven\n")
            if start_method == "1":
                am_users = int(input("Aantal users die u wilt toevoegen: "))
                am_transporters = int(input("Aantal transporteurs die u wilt toevoegen: "))
                start_over(db, am_users, am_transporters)
                answered = True

def simulate():
    running = True
    bike_loan_chance = 0.30
    bike_return_chance = 0.45
    transporter_pickup_chance = 0.20
    transporter_return_chance = 0.6

    # percentage when station needs to be filled
    station_low_point = 0.30
    station_overflow_point = 0.6

    try:
        while running:
            if random() < bike_loan_chance:
                print("loaning bike")
                index = randint(0, len(user_list)-1)
                user = user_list[index]
                station = station_list[randint(0, len(station_list)-1)]

                rel = station.loan_bike(user)
                print(rel)
                relocation_list.append(rel)

                active_user_list[user] = rel
                user_list.remove(user)

            if random() < transporter_pickup_chance:
                # Search for stations that are overflowing
                overflow_station_list.clear()
                for station in station_list:
                    cap = station.get_capacity()
                    av = station.bikes_available()
                    
                    if av/cap >= station_overflow_point:
                        overflow_station_list.append(station)

                # Choose transporter
                transporter = transporter_list[randint(0, len(transporter_list)-1)]
                temp_rel_list = []

                # Transporter goes to overflowing stations and loads his truck untill it's full
                while transporter.count_bikes() < transporter.get_capacity() and len(overflow_station_list) > 0:
                    station = overflow_station_list[randint(0, len(overflow_station_list)-1)]
                    overflow_station_list.remove(station)

                    while station.bikes_available() > station.get_capacity()/2:
                        rel = station.loan_bike(transporter)
                        temp_rel_list.append(rel)
                        relocation_list.append(rel)
                        print(rel)

                if transporter.count_bikes() > 0:
                    active_transporter_list[transporter] = temp_rel_list
                    transporter_list.remove(transporter)

            if random() < transporter_return_chance:
                # Search for stations that need to be filled and stations that are overflowing
                low_station_list.clear()
                for station in station_list:
                    cap = station.get_capacity()
                    av = station.bikes_available()
                    
                    if av/cap <= station_low_point:
                        low_station_list.append(station)
                if len(active_transporter_list) > 0 and len(low_station_list) > 0:
                    print("transporter returning bikes")
                                    
                    key_list = list(active_transporter_list.keys())
                    val_list = list(active_transporter_list.values())
                
                    randomIndex = randint(0, len(active_transporter_list)-1)
                    transporter = key_list[randomIndex]
                    rel_list = val_list[randomIndex]
                    
                    # Transporter goes to low stations and loads them until they're full or his truck is empty
                    while transporter.count_bikes() > 0 and len(low_station_list) > 0:
                        station = low_station_list[randint(0, len(low_station_list)-1)]
                        low_station_list.remove(station)

                        cap = station.get_capacity()

                        while station.bikes_available()/cap < station_overflow_point and len(rel_list) > 0:
                            rel = rel_list.pop()
                            station.return_bike(transporter, rel)
                            print(rel)
                        
                    active_transporter_list.pop(transporter)


            if random() < bike_return_chance:
                if not len(active_user_list) == 0:
                    print("Returning bike")
                    randomIndex = randint(0, len(active_user_list)-1)

                    key_list = list(active_user_list.keys())
                    val_list = list(active_user_list.values())

                    user = key_list[randomIndex]
                    rel = val_list[randomIndex]

                    station = station_list[randint(0, len(station_list)-1)]
                    
                    station.return_bike(user, rel)
                    active_user_list.pop(user)
                    print(rel)


            sleep(1)
    except KeyboardInterrupt:
        print("Simulation stopped")

def save_data_to_db(db):
    print("saving data to database")
    db.clear()

    for user in user_list:
        db.insert_user(user)

    for user in active_user_list:
        db.insert_user(user)
        bike = user.get_bike()
        if not bike == None:
            db.insert_bike(bike)

    for transporter in transporter_list:
        db.insert_user(transporter)

    for transporter in active_transporter_list:
        db.insert_user(transporter)
        bike_list = user.get_bike()
        if not bike_list == None:
            for bike in bike_list:
                db.insert_bike(bike)
    
    db.commit()

    for station in station_list:
        db.insert_station(station)
        for slot in station.slots_list:
            db.insert_slot(slot, station.uid)
            if slot.get_occupied():
                db.insert_bike(slot.get_bike())

    db.commit()
    
    for relocation in relocation_list:
        db.insert_relocation(relocation)
    db.commit()

if __name__ == "__main__":
    db = Database()
    db.init_database()

    load = False
    if db.check_empty(): load = True

    start_menu(load)

    if len(sys.argv) > 1:
        if sys.argv[1] == "-s":
            print("Simulatie modus")
            print("ctrl+c om te stoppen")
            input("Enter drukken om te starten")
            simulate()

    save_data_to_db(db)

    db.disconnect()
