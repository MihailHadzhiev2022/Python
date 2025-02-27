from unittest import TestCase, main

from unit_testing.vehicle.poject.vehicle import Vehicle


class TestVehicle3(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(3.5,150)

    def test_drive_fuel_needed(self):
        self.vehicle.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_enough_fuel(self):
        self.vehicle.drive(2)
        self.assertEqual(1.0,self.vehicle.fuel)

    def test_refuel_with_exception_error(self):

       with self.assertRaises(Exception) as ex:
        self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", self.vehicle.fuel)

    def test_refuel_correct(self):
        self.vehicle.fuel = 1
        self.vehicle.refuel(1)

        self.assertEqual(2,self.vehicle.fuel)

    def test_correct_str(self):
        self.assertEqual("The vehicle has 150 " +
               "horse power with 3.5 fuel left and 1.25 fuel consumption", str(self.vehicle))


if __name__ == "__main__":
    main()