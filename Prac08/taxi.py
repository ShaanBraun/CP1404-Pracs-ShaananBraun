"""
CP1404/CP5632 Practical
Car class
"""

import random


class Car:
    """ represent a car object """

    def __init__(self, name="", fuel=0):
        """ initialise a Car instance """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        return "{}, fuel={}, odo={}".format(self.name, self.fuel, self.odometer)

    def add_fuel(self, amount):
        """ add amount to the car's fuel"""
        self.fuel += amount

    def drive(self, distance):
        """ drive the car a given distance if it has enough fuel or drive until fuel runs out
        return the distance actually driven """
        if distance > self.fuel:
            distance_driven = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
            distance_driven = distance
        self.odometer += distance_driven
        return distance_driven


class Taxi(Car):
    """ specialised version of a Car that includes fare costs """

    price_per_km = 1.2

    def __init__(self, name, fuel):
        """ initialise a Taxi instance, based on parent class Car """
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """ return a string representation like a car but with current fare distance"""
        return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(), self.current_fare_distance,
                                                             self.price_per_km)

    def get_fare(self):
        """ get the price for the taxi trip """
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """ begin a new fare """
        self.current_fare_distance = 0

    def drive(self, distance):
        """ drive like parent Car but calculate fare distance as well"""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability=100):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if random.randint(0, 100) < self.reliability:
            super().drive(distance)
        else:
            print("Car broke down.")


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=1.0):
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        return "{} plus flagfall of ${}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        return (self.price_per_km*self.current_fare_distance) + self.flagfall
