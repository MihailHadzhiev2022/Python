from logging import exception
from unittest import  TestCase, main

from unit_testing.vehicle.poject.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vihicle = Vehicle(3.13,130.5)


    def test_correct_default_fuel_consumption(self):
        self.assertEqual(1.25, self.vihicle.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_init(self):
        self.assertEqual(3.13, self.vihicle.fuel)
        self.assertEqual(130.5,self.vihicle.horse_power)
        self.assertEqual(self.vihicle.fuel, self.vihicle.capacity)
        self.assertEqual(self.vihicle.DEFAULT_FUEL_CONSUMPTION, self.vihicle.fuel_consumption)

    def test_drive_without_enough_fuel_raise_exception(self):

        self.vihicle.fuel = 0

        with self.assertRaises(Exception) as ex:

            self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_car_with_enough_fuel_expect_fuel_decrease(self):

        self.vihicle.drive(2)
        self.assertEqual(0.6299999999999999, self.vihicle.fuel)

    def test_refuel_too_much_fuel(self):

        with self.assertRaises(Exception) as ex:
            self.vihicle.refuel(1)
        self.assertEqual('Too much fuel', str(ex.exception))

    def test_refuel_with_enough_fuel(self):

        self.vihicle.fuel = 0
        self.vihicle.refuel(1)
        self.assertEqual(1, self.vihicle.fuel)

    def test_correct_str(self):
        self.assertEqual("The vehicle has 130.5 " +
               "horse power with 3.13 fuel left and 1.25 fuel consumption", str(self.vihicle))

if __name__ == "__main__":
    main()