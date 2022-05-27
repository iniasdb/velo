from random import randint

from Station import Station

if __name__ == "__main__":
    station = Station(1, "test", "straat", "st jansplein", None, None, "Antwerpen", 2000, True, 20)

    print(station.print_slots)
    print(str(station.bikes_available()) + " bikes available")