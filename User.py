class User:
    def __init__(self, uid, fname, lname, email, subscribed, active):
        self.uid = uid
        self.fname = fname
        self.lname = lname
        self.email = email
        self.subscribed = subscribed
        self.active = active
        self.bike = None

    def get_bike(self):
        return self.bike

    def set_bike(self, bike):
        self.bike = bike

    def __str__(self):
        return f"First name: {self.fname}; Last name: {self.lname}; Email: {self.email}; sub: {self.subscribed}; active: {self.active}"
