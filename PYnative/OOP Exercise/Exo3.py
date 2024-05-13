from Exo1 import Vehicle

class Bus(Vehicle):
    pass

school_bus = Bus("Volvo",100,20000)
print("Vehicle Name:", school_bus.name, "Speed:", school_bus.max_speed, "Mileage:", school_bus.mileage)