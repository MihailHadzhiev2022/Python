

from unittest import TestCase,main

from Classes_Objects.enheretance import Animal, Cat


class TestEnheretance(TestCase):

    def setUp(self):
        self.animal = Animal('some kind', 'someAge', 'some name')
        self.cat = Cat("Asher")

    def test_correct_initializing(self):
        self.assertEqual("some kind", self.animal.kind)
        self.assertEqual("someAge", self.animal.age)
        self.assertEqual("some name", self.animal.name)
        self.assertEqual('Asher', self.cat.name)


    def test_if_run_return_message(self):
        self.assertEqual('some name is running!', self.animal.run())

 

if __name__ == "__main__":
    main()