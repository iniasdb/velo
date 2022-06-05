from User import User

class Transporter(User):
    def __init__(self,  uid, fname, lname, email, transporter):
        super().__init__(uid, fname, lname, email, 1, transporter)
        self.capacity = 50
        self.bike_list = []

    def get_bike(self):
        bike = self.bike_list.pop()
        return bike

    def set_bike(self, bike):
        self.bike_list.append(bike)

    def count_bikes(self):
        return len(self.bike_list)

    def get_bike_list(self):
        return self.bike_list

    def get_capacity(self):
        return self.capacity