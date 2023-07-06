import pandas as pd

df = pd.read_csv("hotels.csv", sep=",")


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        pass

    def book(self):
        pass

    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class Reservation:
    def __init__(self, customer_name, hotel_object):
        pass

    def generate(self):
        pass


print(df)
hotel_ID = input("Enter the hotel ID: ")
hotel = Hotel(hotel_ID)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation = Reservation(name, hotel)
    print(reservation.generate())
else:
    print("Hotel is not available")
