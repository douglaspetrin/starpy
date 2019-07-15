import unittest
from starpy.api import GetStars


class TestApi(unittest.TestCase):

    def test_api_is_lists(self):
        self.assertIs(type(s._get_people(10)), type({}))
        self.assertIs(type(s._get_starships(10)), type({}))
        self.assertIs(type(s._get_vehicles(10)), type({}))

        self.assertIs(type(s.get_people_by_id(10)), type({}))
        self.assertIs(type(s.get_starships_by_id(10)), type({}))
        self.assertIs(type(s.get_vehicles_by_id(10)), type({}))

    def test_api_is_str(self):
        self.assertIs(type(s._get_transport(s._PEOPLE)), type(''))
        self.assertIs(type(s._get_transport(s._STAR_SHIPS)), type(''))
        self.assertIs(type(s._get_transport(s._VEHICLES)), type(''))

    def test_api_endpoint(self):
        pass


s = GetStars()

if __name__ == '__main__':
    unittest.main()