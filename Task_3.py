
class Car:
    def __init__(self, make, model, year, odometr=0, fuel=70):
        self.make = make
        self.model = model
        self.year = year
        self.odometr = odometr
        self.fuel = fuel

    def drive(self, killometry):
        liters = killometry/10
        if liters <= self.fuel:
            self.__add_distance(self, killometry)
            print('Let’s drive!')
        elif self.fuel == 0:
            self.__subtract_fuel(self, liters)
            print('Need more fuel, please, fill more!')

    def __add_distance(self, killometry):
        self.odometr += killometry
        return self.odometr

    def __subtract_fuel(self, liters):
        self.fuel -= liters

    def __str__(self):
        print(f'Car {self.model} {self.year} {self.fuel} {self.odometr}')


car1 = Car('USA', 'Tesla Model S', 2010)
print(car1.model)
print(car1.year)
car1.drive(300)

car2 = Car('FRA', 'Pejo S6', 2009, 0, 0)
print(car2.model)
print(car2.year)
car2.drive(300)

print(car1.__str__())

