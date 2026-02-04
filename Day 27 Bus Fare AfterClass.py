class Vehicle:
    def __init__(self,fare):
        self.fare = fare

class Bus(Vehicle):
    def __init__(self):
        super().__init__(5000)   
        print(self.fare)

bus = Bus()
print(bus.fare)
