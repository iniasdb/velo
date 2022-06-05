import shortuuid

class Relocation:
    def __init__(self, user, bike, prev_station):
        shortuuid.set_alphabet("123456789")
        self.uid = shortuuid.uuid()[:10]
        self.user = user
        self.bike = bike
        self.prev_station = prev_station
        self.new_station = None

    def set_new_station(self, station):
        self.new_station = station

    def __str__(self):
        if self.new_station == None:
            street = None
        else:
            street = self.new_station.street
        
        if self.user.transporter:
            return f"Bike {self.bike.uid} moved from {self.prev_station.street} to {street} by transporter {self.user.fname}"
        else:
            return f"Bike {self.bike.uid} moved from {self.prev_station.street} to {street} by {self.user.fname}"
