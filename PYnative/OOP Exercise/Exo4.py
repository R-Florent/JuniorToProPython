from Exo1 import Vehicle

class Bus(Vehicle):
    def __init__(self, namebus, max_speed, mileage, capacity ,color):
        super().__init__(namebus, max_speed, mileage,color)
        self.capacity = capacity

    def Bus_info(self):
        print('inside the bus :',self.capacity)


    def return_capacity(self,capacity):
        return super().seating_capacity(capacity)


my_bus = Bus("School Volvo",100,2000,50)
my_bus.info_vehicle()

my_bus.return_capacity(my_bus.capacity)

print(my_bus.seating_capacity(my_bus.capacity))
print(my_bus.color)