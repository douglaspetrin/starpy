import unittest
from starpy.api import GetStars


class TestApi(unittest.TestCase):

    def setUp(self):
        self.s = GetStars()
        self.ha = 'ha'

    def test__sget(self):
        self.assertRaises(Exception, self.s._sget, self.ha)
        self.assertIs(type(self.s._sget(self.s._VEHICLES)), dict)

    def test_get_next_page(self):
        self.assertRaises(Exception, self.s._sget, self.ha)

    def test_get_people_by_id(self):
        self.assertRaises(Exception, self.s.get_people_by_id, self.ha)
        self.assertIs(type(self.s.get_people_by_id(10)), dict)

    def test__get_starships_by_id(self):
        self.assertRaises(Exception, self.s._get_starships, self.ha)
        self.assertIs(type(self.s.get_starships_by_id(10)), dict)

    def test_get_vehicles_by_id(self):
        self.assertRaises(Exception, self.s.get_vehicles_by_id, 10)
        self.assertIs(type(self.s.get_vehicles_by_id(35)), dict)

    def test__if_transport(self):
        self.assertRaises(Exception, self.s._if_transport, self.ha)
        self.assertRaises(Exception, self.s._if_transport, 123)
        self.assertRaises(Exception, self.s._if_transport, 'vehicle')
        self.assertIs(type(self.s._if_transport(self.s._VEHICLES)), dict)

    def test__find_pilots_from_df(self):
        self.assertRaises(Exception, self.s._find_pilots_from_df, self.ha)
        self.assertRaises(Exception, self.s._find_pilots_from_df, self.ha)

    def test__get_transport(self):
        self.assertRaises(Exception, self.s._get_transport, self.ha)
        self.assertIs(type(self.s._get_transport(self.s._VEHICLES)), dict)


if __name__ == '__main__':
    unittest.main()