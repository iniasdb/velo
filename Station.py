from random import randint
import shortuuid
from Bike import Bike
from Slot import Slot
from Relocation import Relocation
from helperClasses.logger import Logger

logger = Logger()

class Station:
    def __init__(self, uid, position, street, number, addition, district, postal_code, in_use, capacity):
        self.uid = uid
        self.position = position
        self.street = street
        self.number = number
        self.addition = addition
        self.district = district
        self.postal_code = postal_code
        self.in_use = in_use
        self.capacity = capacity
        self.slots_list = []

    def generate_slots(self):
        i = 1
        for i in range(0, self.capacity):
            rand = randint(0, 1)
            if rand:
                uid = shortuuid.uuid()[:10]
                bike = Bike(uid, True)
                slot = Slot(i, rand, bike)
            else:
                slot = Slot(i, rand)

            self.add_slot(slot)
            i+=1

    def add_slot(self, slot):
        self.slots_list.append(slot)

    def bikes_available(self):
        '''checks all slots if they are occupied
           if true: increment amount of available bikes
        '''
        bikes = 0
        
        for slot in self.slots_list:
            if slot.get_occupied():
                bikes+=1

        return bikes

    def get_empty_slot(self):
        for slot in self.slots_list:
            if not slot.get_occupied():
                return slot
        logger.warn("No empty slots")

    def get_occupied_slot(self):
        for slot in self.slots_list:
            if slot.get_occupied():
                return slot
        logger.warn("No occupied slots")

    def loan_bike(self, user):
        slot = self.get_occupied_slot()
        bike = slot.get_bike()
        slot.release_bike(user)
        return Relocation(user, bike, self)

    def loan_bike(self, user, return_slot_nr = False):
        slot = self.get_occupied_slot()
        bike = slot.get_bike()
        slot.release_bike(user)
        if return_slot_nr:
            return (Relocation(user, bike, self), slot)
        else:
            return Relocation(user, bike, self)

    def return_bike(self, user, relocation):
        slot = self.get_empty_slot()
        slot.place_bike(user)
        relocation.set_new_station(self)
        return slot

    def get_capacity(self):
        return self.capacity

    def __str__(self):
        return f"straat: {self.street}; nummer: {self.number}; postcode: {self.postal_code}; gebruik: {self.in_use}; cap: {self.capacity}"

