class Animal:
    def __init__(self, kind, age,name):
        self.kind  = kind
        self.age = age
        self.name = name

    def run(self):
        return  f"{self.name} is running!"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(kind="Cat", age=None,name=name)

    def run(self):
        print(f"{self.name} the cat is running!")


Asher = Cat('Asher')
Asher.run()