class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, increment):
        self.speed += increment
        return f'The {self.make} {self.model} is now going at a speed of {self.speed}mph'
    
    def brake(self, decrement):
        if self.speed - decrement < 0:
            self.speed = 0
        else:
            self.speed -= decrement
        return f'The {self.make} {self.model} has slowed to {self.speed}mph'
    
    def honk(self):
        return "Beep Beep"
    
my_car = car('Toyota', "Corolla", 2022)

print(my_car.accelerate(30))
print(my_car.brake(10))
print(my_car.honk())