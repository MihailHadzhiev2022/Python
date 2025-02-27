from unittest import TestCase, main

from Classes_Objects.enheretance import Animal


class test3(TestCase):

    def setUp(self):
        self.animal = Animal('kind', 'age', 'name')

    def test_correct_messsage_4(self):
        self.assertEqual(self.animal.kind, 'kind')
        self.assertEqual(self.animal.age, 'age')
        self.assertEqual(self.animal.name, 'name')



if __name__ == '__main__':
    main()