class Vihicle:

    """This is hello """
    def __init__(self,name:str,speed:int,year:int):
        self.name = name
        self.speed = speed
        self.year = year

    def speed_up(self,miliage:int):
        self.speed += miliage

    def __str__(self):
        return f"this is {self.name} car and it's build in {self.year}"
mihails_first_car = Vihicle('Pejo',180,1994)

print(mihails_first_car.name)

mihails_first_car.speed_up(30)
print(mihails_first_car.speed)
print(mihails_first_car)