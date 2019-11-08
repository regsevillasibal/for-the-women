# Exercise7.py

# Challenge - Classes Exercise

# Add a method to the Car class called age
# that returns how old the car is (2019 - year)

# *Be sure to return the age, not print it

class Car:

    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model
#© 2019 GitHub, Inc.

#age = 2019 - year


	def age(self):
        today = 2019
        age = today - self.year
        return age
