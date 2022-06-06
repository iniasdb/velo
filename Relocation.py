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

    def get_data(self):
        name = str(self.user.fname.capitalize()) + " " + str(self.user.lname.capitalize())

        if self.new_station == None:
             new_street = "None"
        else:
            new_street = self.new_station.street

        
        return (self.bike.uid, name, self.prev_station.street, new_street)     

    def __str__(self):
        if self.new_station == None:
            if self.user.transporter:
                return f"Bike {self.bike.uid} moved from {self.prev_station.street} by transporter {self.user.fname.capitalize()} {self.user.lname.capitalize()}"
            else:
                return f"Bike {self.bike.uid} moved from {self.prev_station.street} by {self.user.fname.capitalize()} {self.user.lname.capitalize()}"
        else:
            if self.user.transporter:
                return f"Bike {self.bike.uid} moved from {self.prev_station.street} to {self.new_station.street} by transporter {self.user.fname.capitalize()} {self.user.lname.capitalize()}"
            else:
                return f"Bike {self.bike.uid} moved from {self.prev_station.street} to {self.new_station.street} by {self.user.fname.capitalize()} {self.user.lname.capitalize()}"
