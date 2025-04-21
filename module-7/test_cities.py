# test_cities.py
#tysonblatter4/20 7.2
import unittest
from city_functions import city_country


class TestCityCountry(unittest.TestCase):

    def test_city_country(self):
        #
        result = city_country("Orlando", "USA")
        self.assertEqual(result, "Orlando, USA")

        result = city_country("Paris", "France")
        self.assertEqual(result, "Paris, France")

        result = city_country("Tokyo", "Japan")
        self.assertEqual(result, "Tokyo, Japan")


if __name__ == '__main__':
    unittest.main()
