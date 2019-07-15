import unittest
from starpy.api import GetStars


class TestApi(unittest.TestCase):

    def test_get_people__by_id(self):
        self.assertIs(type(s.get_people_by_id(10)), dict)
        alphabet = []
        for letter in range(65, 91):
            alphabet.append(chr(letter))

        for i in range(len(alphabet)):
            self.assertEqual((s.get_people_by_id(alphabet[i])['detail']), 'Not found')

    def test_api_is_lists(self):
        self.assertIs(type(s._get_starships(10)), dict)
        self.assertIs(type(s._get_vehicles(10)), dict)

        self.assertIs(type(s.get_people_by_id(10)), dict)
        self.assertIs(type(s.get_starships_by_id(10)), dict)
        self.assertIs(type(s.get_vehicles_by_id(10)), dict)

    def test_var_types(self):
        self.assertIs(type(s._PEOPLE), str)
        self.assertIs(type(s._STAR_SHIPS), str)
        self.assertIs(type(s._VEHICLES), str)

    def test_get_transport(self):
        self.assertIs(type(s._get_transport(s._VEHICLES)), dict)
        self.assertIs(type(s._get_transport('')), Exception)

    def test_sget(self):
        self.assertIs(type(s._sget(s._VEHICLES)), dict)

    def test_if_transport(self):
        # IsNot
        self.assertIsNot(type(s._if_transport(132)), dict)
        self.assertIsNot(type(s._if_transport('veiculo')), dict)
        self.assertIsNot(type(s._if_transport(s._PEOPLE)), dict)
        # Is
        self.assertIs(type(s._if_transport(s._VEHICLES)), dict)

    def test_api_endpoint(self):
        pass


s = GetStars()

if __name__ == '__main__':
    unittest.main()