import unittest
from database import add_vehicle, db, delete_vehicle, get_database, empty_database, view_vehicle, update_vehicle


class MyTestCase(unittest.TestCase):
    def test_add_vehicle(self):
        empty_database()
        self.assertEqual(get_database(), [])
        add_vehicle("BMW", "320", 1996, "blue", 300_000)
        self.assertEqual(get_database(), [("BMW", "320", 1996, "blue", 300_000)])

    def test_delete_vehicle(self):
        empty_database()
        add_vehicle("BMW", "320", 1996, "blue", 300_000)
        delete_vehicle(0)
        self.assertEqual(get_database(), [])

    def test_view_vehicle(self):
        empty_database()
        add_vehicle("BMW", "320", 1996, "blue", 300_000)
        vehicle_data = view_vehicle(0)
        self.assertEqual(vehicle_data[0], "BMW")
        self.assertEqual(vehicle_data[1], "320")
        self.assertEqual(vehicle_data[2], 1996)
        self.assertEqual(vehicle_data[3], "blue")
        self.assertEqual(vehicle_data[4], 300_000)

    def test_update_vehicle(self):
        empty_database()
        add_vehicle("BMW", "320", 1996, "blue", 300_000)
        update_vehicle(0, "BMW1", "3201", 19961, "blue1", 300_0001)
        vehicle_data = view_vehicle(0)
        self.assertEqual(vehicle_data[0], "BMW1")
        self.assertEqual(vehicle_data[1], "3201")
        self.assertEqual(vehicle_data[2], 19961)
        self.assertEqual(vehicle_data[3], "blue1")
        self.assertEqual(vehicle_data[4], 300_0001)


if __name__ == '__main__':
    unittest.main()
