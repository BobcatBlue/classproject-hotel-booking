import pandas as pd

df = pd.read_csv("hotels.csv", sep=",")

class Hotel:
    def __init__(self, id):
        pass

    def book(self):
        pass

    def available(self):
        pass


class Reservation:
    def __init__(self, customer_name, hotel_object):
        pass

    def generate(self):
        pass


print(df)
id = input("Enter the hotel ID: ")
hotel = Hotel(id)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation = Reservation(name, hotel)
    print(reservation.generate())
else:
    print("Hotel is not available")
