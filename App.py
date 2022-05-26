from random import randint

from Station import Station
from Slot import Slot

if __name__ == "__main__":
    station = Station(1, "test", "straat", "st jansplein", None, None, "Antwerpen", 2000, True, 20)
    i = 1
    for i in range(0, 20):
        rand = randint(0, 1)
        slot = Slot(i, rand)
        station.add_slot(slot)
        i+=1

    print(str(station.bikes_available()) + " bikes available")