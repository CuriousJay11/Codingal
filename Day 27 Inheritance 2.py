class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def display(self):
        print("Vehicle Name:", self.name)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage,No_Seats,No_Doors,Staff):
        Vehicle.__init__(self, name, max_speed, mileage)
        self.No_Seats = No_Seats
        self.No_Doors = No_Doors
        self.Staff = Staff


class Car(Vehicle):
    def __init__(self, name, max_speed, mileage,No_Seats,No_Doors):
        Vehicle.__init__(self, name, max_speed, mileage)
        self.No_Seats = No_Seats
        self.No_Doors = No_Doors


school_bus = Bus("School Bus", 180, 12,45,3,2)
mercedes_car = Car("Mercedes", 240, 15,5,4)

school_bus.display()
print()
mercedes_car.display()