import csv
from pickle import TRUE
import shortuuid
from random import randint
from Transporter import Transporter
from User import User

class RandomUserGenerator:
    def __init__(self):
        shortuuid.set_alphabet("123456789")
        self.first_names_list = []
        self.last_names_list = []
        self.mails_list = []
        self.fname = self.lname = self.mail = ""
        self.__load_data()

    def __load_data(self):
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

    def __gen_name(self):
        randF = randint(0, len(self.first_names_list)-1)
        randL = randint(0, len(self.last_names_list)-1)
        self.fname = str(self.first_names_list[randF]).lower()
        self.lname = str(self.last_names_list[randL]).lower()

    def __gen_mail(self): 
        rand = randint(0, len(self.mails_list)-1)
        provider = self.mails_list[rand]
        self.mail = f"{self.fname}.{self.lname}@{provider}"

    def _generate(self):
        self.__gen_name()
        self.__gen_mail()

    def get_user(self):
        shortuuid.uuid()
        self._generate()
        sub = randint(0, 1)
        uid = shortuuid.uuid()[:10]
        return User(uid, self.fname, self.lname, self.mail, sub, False)

    def get_transporter(self):
        shortuuid.uuid()
        self._generate()
        uid = shortuuid.uuid()[:10]
        return Transporter(uid, self.fname, self.lname, self.mail, True)

    def __str__(self):
        return f"First name: {self.fname}; Last name: {self.lname}; Email: {self.mail}"

