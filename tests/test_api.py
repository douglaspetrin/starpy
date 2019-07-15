import unittest
from starpy.api import GetStars


class TestApi(unittest.TestCase, GetStars):
    s = GetStars()

    def test_api_is_lists(self):
        self.assertIs(type(self.s._get_people(10)), type({}))
        self.assertIs(type(self.s._get_starships(10)), type({}))
        self.assertIs(type(self.s._get_vehicles(10)), type({}))

        self.assertIs(type(self.s.get_people_by_id(10)), type({}))
        self.assertIs(type(self.s.get_starships_by_id(10)), type({}))
        self.assertIs(type(self.s.get_vehicles_by_id(10)), type({}))

    def test_api_endpoint(self):
        pass



if __name__ == '__main__':
    unittest.main()