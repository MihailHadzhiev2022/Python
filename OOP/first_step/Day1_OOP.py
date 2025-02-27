class Person:
    def __init__(self,name,age,town):
        self.name = name
        self.age = age
        self.town = town


    def move_to_city(self, second_town):
        self.town = second_town



mihail = Person('Mihail', 38, 'Yambol')


print (mihail.name)
print (mihail.age)
print (mihail.town)
mihail.move_to_city('Sofia')
print(mihail.town)