from Station import Station
from Slot import Slot
from random import randint


if __name__ == "__main__":
    station = Station(1, "test", "straat", "st jansplein", None, None, "Antwerpen", 2000, True, 20)
    for i in range(0, 20):
        rand = randint(0, 1)
        slot = Slot(1, rand)
        station.add_slot(slot)

    print(str(station.bikes_available()) + " bikes available")