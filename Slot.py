class Slot:
    def __init__(self, index, occupied):
        self.index = index
        self.occupied = occupied

    def place_bike(self, bike):
        self.bike = bike
        self.occupied = True
    
    def release_bike(self, user, bike):
        # TODO bike aan user toekennen
        self.occupied = False

    def get_index(self):
        return self.index

    def get_occupied(self):
        return self.occupied

    def set_occupied(self, occupied):
        self.occupied = occupied