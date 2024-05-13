class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

    def info_vehicle(self):
        print("LES INFO DU BUS SONT",'\n',self.name, self.max_speed, self.mileage)