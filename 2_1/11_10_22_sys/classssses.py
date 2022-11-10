class Vehicle():
    """docstring"""

    def __init__(self, names, doors, tires):
        """Constructor"""
        self.name = names
        self.doors = doors
        self.tires = tires

    def __str__(self):
        return self.name

    def brake(self):
        """
        Stop the car
        """
        return "Braking"*self.tires

    def drive(self):
        """
        Drive the car
        """
        return "I'm driving!"

kia=Vehicle("kia",4,4)
names=["bmv","mers"]
doors=["4","2"]
mas_with_cars=[]
for i in range(len(names)):
    mas_with_cars.append(Vehicle(names[i],doors[i],4))
#while run:
for car in mas_with_cars:
    print(car.brake())

names=0

bmv=Vehicle("red",4,4)
#mers
