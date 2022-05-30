from random import randint
from Bike import Bike
from Slot import Slot

class Station:
    def __init__(self, uid, name, position, street, number, addition, district, postal_code, in_use, capacity):
        self.uid = uid
        self.name = name
        self.position = position
        self.street = street
        self.number = number
        self.addition = addition
        self.district = district
        self.postal_code = postal_code
        self.in_use = in_use
        self.capacity = capacity
        self.slots_list = []

        self.__generate_slots()

    def __generate_slots(self):
        i = 1
        for i in range(0, self.capacity):
            rand = randint(0, 1)
            if rand:
                bike = Bike(1, True)
                slot = Slot(i, rand, bike)
            else:
                slot = Slot(i, rand)

            self.__add_slot(slot)
            i+=1

    def __add_slot(self, slot):
        self.slots_list.append(slot)
    
    def __remove_slot(self, slot):
        self.slots_list.remove(slot)

    def print_slots(self):
        #TODO: print details
        for slot in self.slots_list:
            print(slot)

    def bikes_available(self):
        '''checks all slots if they are occupied
           if not: increment amount of available bikes
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
        return "No empty slots"

    def get_occupied_slot(self):
        for slot in self.slots_list:
            if slot.get_occupied():
                return slot
        return "No occupied slots"

    def loan_bike(self, user):
        slot = self.get_occupied_slot()
        slot.release_bike(user)

    def return_bike(self, user):
        slot = self.get_empty_slot()
        slot.place_bike(user)

