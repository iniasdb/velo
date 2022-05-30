class Slot:
    def __init__(self, index, occupied, bike = None):
        self.index = index
        self.occupied = occupied
        self.bike = bike

    def place_bike(self, user):
        bike = user.get_bike()
        user.set_bike(None)
        self.bike = bike
        self.occupied = True
    
    def release_bike(self, user):
        if self.occupied == False:
            #TODO logging
            print("no bike")
            return None
        user.set_bike(self.bike)
        self.bike = None
        self.occupied = False

    def get_index(self):
        return self.index

    def get_occupied(self):
        return self.occupied

    def set_occupied(self, occupied):
        self.occupied = occupied

    def get_bike(self):
        return self.bike