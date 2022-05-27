import csv
from random import randint
from User import User

class RandomUserGenerator:
    def __init__(self):
        self.first_names_list = []
        self.last_names_list = []
        self.mails_list = []
        self.fname = self.lname = self.mail = ""
        self.load_data()

    def load_data(self):
        with open('files/names.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == "first":
                    self.first_names_list.append(row[0])
                elif row[1] == "last":
                    self.last_names_list.append(row[0])
        with open('files/mails.txt', 'r') as file:
            for mail in file:
                self.mails_list.append(mail)

    def gen_name(self):
        randF = randint(0, len(self.first_names_list)-1)
        randL = randint(0, len(self.last_names_list)-1)
        self.fname = str(self.first_names_list[randF]).lower()
        self.lname = str(self.last_names_list[randL]).lower()

    def gen_mail(self): 
        rand = randint(0, len(self.mails_list)-1)
        provider = self.mails_list[rand]
        self.mail = f"{self.fname}.{self.lname}@{provider}"

    def __str__(self):
        return f"First name: {self.fname}; Last name: {self.lname}; Email: {self.mail}"
        
if __name__ == "__main__":
    gen = RandomUserGenerator()

    gen.gen_name()
    gen.gen_mail()

    sub = randint(0, 1)
    if sub == 0:
        act = randint(0, 1)
        user = User(1, gen.fname, gen.lname, gen.mail, sub, act)
    else:
        user = User(1, gen.fname, gen.lname, gen.mail, sub, sub)

    print(str(user))

