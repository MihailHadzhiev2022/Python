from unittest import TestCase, main

from unit_testing.mammal.project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal('some name', 'some type', 'some sound')


    def test_correct_inicialization(self):

        self.assertEqual('some name', self.mammal.name)
        self.assertEqual('some type', self.mammal.type)
        self.assertEqual('some sound', self.mammal.sound)

    def test_return_correct_message(self):
        self.assertEqual('some name makes some sound', self.mammal.make_sound())

    def test_correct_get_kingdom(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_correct_message_kingdom(self):
        self.assertEqual('some name is of type some type', self.mammal.info())



if __name__ == '__main__':
    main()
