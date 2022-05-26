import csv
from fnmatch import fnmatchcase
from random import randint


class RandomUserGenerator():
    def __init__(self):
        self.first_names = []
        self.last_names = []
        self.fname = self.lname = ""

    def loadNames(self):
        with open('files/names.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == "first":
                    self.first_names.append(row[0])
                elif row[1] == "last":
                    self.last_names.append(row[0])

    def genName(self):
        randF = randint(0, len(self.first_names)-1)
        randL = randint(0, len(self.last_names)-1)
        self.fname = self.first_names[randF]
        self.lname = self.last_names[randL]

    def __str__(self):
        return f"First name: {self.fname}; Last name: {self.lname}"
        

gen = RandomUserGenerator()

gen.loadNames()
gen.genName()
print(str(gen))