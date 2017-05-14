
from Prac08.taxi import Taxi, UnreliableCar, SilverServiceTaxi


prius_taxi = Taxi("Prius", 100)
prius_taxi.drive(40)
print(prius_taxi)
prius_taxi.start_fare()
prius_taxi.drive(100)
print(prius_taxi)


unreliable_car = UnreliableCar("Bad Car", 200, 12)
unreliable_car.drive(50)
print(unreliable_car)


silver_surfer = SilverServiceTaxi("Surfer Taxi", 200, 2)
silver_surfer.drive(10)
print(silver_surfer)
print("Total fare ${}".format(silver_surfer.get_fare()))