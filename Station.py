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

    def add_slot(self, slot):
        self.slots_list.append(slot)
    
    def remove_slot(self, slot):
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