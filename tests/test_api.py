import unittest
from starpy.api import GetStars


class TestApi(unittest.TestCase):

    def setUp(self):
        self.s = GetStars()

    def test_get_people_by_id(self):
        self.assertRaises(Exception, self.s.get_people_by_id, 'hehe] ')
        self.assertIs(type(self.s.get_people_by_id(10)), dict)

    def test_get_starships_by_id(self):
        self.assertIs(type(self.s.get_starships_by_id(10)), dict)

    def test_get_vehicles_by_id(self):
        self.assertRaises(Exception, self.s.get_vehicles_by_id, 10)
        self.assertIs(type(self.s.get_vehicles_by_id(35)), dict)

    def test_get_transport(self):
        self.assertIs(type(self.s._get_transport(self.s._VEHICLES)), dict)
        self.assertRaises(Exception, self.s._get_transport(''))

    def test_sget(self):
        self.assertIs(type(self.s._sget(self.s._VEHICLES)), dict)

    def test_if_transport(self):
        # IsNot
        self.assertIsNot(type(self.s._if_transport(132)), dict)
        self.assertIsNot(type(self.s._if_transport('veiculo')), dict)
        self.assertIsNot(type(self.s._if_transport(self.s._PEOPLE)), dict)
        # Is
        self.assertIs(type(self.s._if_transport(self.s._VEHICLES)), dict)

    def test_api_endpoint(self):
        pass


if __name__ == '__main__':
    unittest.main()