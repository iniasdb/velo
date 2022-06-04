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
                    stationName= station.name,
                    street=station.street,
                    number=station.number,
                    postalCode=station.postal_code,
                    district=station.district,
                    capacity=station.capacity,
                    bikeList=slots,
                    color=in_use
                )
            )

