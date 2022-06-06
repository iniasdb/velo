from jinja2 import Environment, FileSystemLoader

class SiteGenerator:
    def __init__(self):
        self.template_env = Environment(loader=(FileSystemLoader(searchpath="./files/webTemplates")))
        self.station_template = self.template_env.get_template("stationTemplate.html")
        self.bike_template = self.template_env.get_template("bikeTemplate.html")
        self.user_template = self.template_env.get_template("userTemplate.html")

    def create_stationpage(self, station):
        if station.in_use:
            in_use = "green"
        else:
            in_use = "red"

        number = ""
        if not station.number == None:
            number = station.number

        slots = ""
        for slot in station.slots_list:
            if slot.get_occupied():
                slot_data = "OCCUPIED"
            else:
                slot_data = "EMPTY" 
            slots += "<li>"+str(slot.get_index()+1) + ": " + str(slot_data)+"</li>"

        with open("_site/stations.html", "w") as of:

            of.write(
                self.station_template.render(
                    street=station.street,
                    number=station.number,
                    postalCode=station.postal_code,
                    district=station.district,
                    capacity=station.capacity,
                    bikeList=slots,
                    color=in_use
                )
            )

    def create_bikepage(self, bike):
        if bike.in_use:
            color = "green"
            in_use = "in use"
        else:
            color = "red"
            in_use = "not in use"

        with open("_site/bikes.html", "w") as of:

            of.write(
                self.bike_template.render(
                    uid = bike.uid,
                    inUse = in_use,
                    color = color
                )
            )

    def create_userpage(self, user):
        with open("_site/users.html", "w") as of:
            subscribed = ""
            if not user.subscribed:
                subscribed = "not "

            bike_list = "<ul>"
            transporter = ""
            if not user.transporter:
                transporter = "not "
            else:
                user_bike_list = user.get_bike_list()

                for bike in user_bike_list:
                    bike_list += "<li>"+ str(bike.uid) + "</li>"

                if len(user_bike_list) == 0:
                    bike_list += "<p>No bike equiped</p>"
                else:
                    bike_list += "</ul>"

            
            of.write(
                self.user_template.render(
                    fname = user.fname.capitalize(),
                    lname = user.lname.capitalize(),
                    uid = user.uid,
                    email = user.email,
                    subscribed = subscribed,
                    transporter = transporter,
                    bikeList = bike_list
                )
            )