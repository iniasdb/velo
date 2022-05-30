from RandomUserGenerator import RandomUserGenerator
from Station import Station

if __name__ == "__main__":

    # Create station, print slots, get available bikes
    station = Station(1, "test", "straat", "st jansplein", None, None, "Antwerpen", 2000, True, 20)
    print(station.print_slots)
    print(str(station.bikes_available()) + " bikes available")

    # Create random user
    gen = RandomUserGenerator()
    user = gen.get_user()
    print(user)

    # User loan and return bike
    station.loan_bike(user)
    print("bike: " + str(user.get_bike()))
    station.return_bike(user)
    print("bike: " + str(user.get_bike()))