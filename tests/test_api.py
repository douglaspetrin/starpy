import unittest
from starpy.api import GetStars


class TestApi(unittest.TestCase):
    """ Tests with unittest """

    def setUp(self):
        self.s = GetStars()
        self.ha = 'ha'

    def test__sget(self):
        self.assertRaises(Exception, self.s._sget, self.ha)
        self.assertIs(type(self.s._sget(self.s._VEHICLES)), dict)

    def test_get_next_page(self):
        self.assertRaises(Exception, self.s._sget, self.ha)

    def test_get_people_by_id(self):
        self.assertRaises(Exception, self.s.get_person_by_id, self.ha)
        self.assertIs(type(self.s.get_person_by_id(10)), dict)

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
        self.assertRaises(Exception, self.s._find_pilots_to_list, self.ha)
        self.assertIs(type(self.s._find_pilots_to_list(self.s._STAR_SHIPS)), list)

    def test_find_pilots_from_v(self):
        self.assertRaises(Exception, self.s.find_pilots_from_v, self.ha)
        self.assertIs(type(self.s.find_pilots_from_v()), list)

    def test_find_pilots_from_s(self):
        self.assertRaises(Exception, self.s.find_pilots_from_s, self.ha)
        self.assertIs(type(self.s.find_pilots_from_s()), list)

    def test__find_fastest_transport_name_and_its_speed(self):
        self.assertRaises(Exception, self.s._find_fastest_transport_name_and_its_speed, self.ha)
        self.assertIs(type(self.s._find_fastest_transport_name_and_its_speed(self.s._VEHICLES)), tuple)

    def test__find_fastest_speed(self):
        self.assertRaises(Exception, self.s._find_fastest_speed, self.ha)
        self.assertIs(type(self.s._find_fastest_speed(self.s._VEHICLES)), dict)

    def test__find_fastest_trans_name(self):
        self.assertRaises(Exception, self.s._find_fastest_trans_name, self.ha)
        self.assertIs(type(self.s._find_fastest_trans_name(self.s._VEHICLES)), list)

    def test_find_fastest_v(self):
        self.assertRaises(Exception, self.s.find_fastest_v, self.ha)
        self.assertIs(type(self.s.find_fastest_v()), dict)

    def test__df_of_transport(self):
        import pandas as pd
        self.assertRaises(Exception, self.s._df_of_transport, self.ha)
        self.assertIs(type(self.s._df_of_transport(self.s._VEHICLES)), pd.DataFrame)

    def test__url_of_fastest_pilot(self):
        self.assertRaises(Exception, self.s._url_of_fastest_pilot, self.ha)
        self.assertIs(type(self.s._url_of_fastest_pilot(self.s._VEHICLES)), list)

    def test__get_transport(self):
        self.assertRaises(Exception, self.s._get_transport, self.ha)
        self.assertIs(type(self.s._get_transport(self.s._VEHICLES)), dict)

    def test__url_fastest_pilots_v(self):
        self.assertRaises(Exception, self.s._url_fastest_pilots_v, self.ha)
        self.assertIs(type(self.s._url_fastest_pilots_v()), list)

    def test__url_fastest_pilot_v(self):
        self.assertRaises(Exception, self.s._url_fastest_pilot_v, self.ha)
        self.assertIs(type(self.s._url_fastest_pilot_v()), str)

    def test__url_fastest_pilots_s(self):
        self.assertRaises(Exception, self.s._url_fastest_pilots_s, self.ha)
        self.assertIs(type(self.s._url_fastest_pilots_s()), list)

    def test__id_fastest_pilots(self):
        self.assertRaises(Exception, self.s._id_fastest_pilots, self.ha)
        self.assertIs(type(self.s._id_fastest_pilots(self.s._VEHICLES)), list)

    def test_id_fastest_pilots_v(self):
        return self.is_raises(self.s.id_fastest_pilots_v,
                              self.s.id_fastest_pilots_v(), list)

    def test_id_fastest_pilot_v(self):
        return self.is_raises(self.s.id_fastest_pilot_v,
                              self.s.id_fastest_pilot_v(), str)

    def test_id_fastest_pilots_s(self):
        return self.is_raises(self.s.id_fastest_pilots_s,
                              self.s.id_fastest_pilots_s(), list)

    def test_id_fastest_pilot_s(self):
        return self.is_raises(self.s.id_fastest_pilot_s,
                              self.s.id_fastest_pilot_s(), str)

    def test__pilot_names(self):
        return self.is_raises(self.s._pilot_names,
                              self.s._pilot_names(self.s._STAR_SHIPS), list)

    def test_pilot_names_v(self):
        return self.is_raises(self.s.pilot_names_v,
                              self.s.pilot_names_v(), list)

    def test_pilot_names_s(self):
        return self.is_raises(self.s.pilot_names_s,
                              self.s.pilot_names_s(), list)

    def test_name_and_max_speed(self):
        return self.is_raises(self.s._name_and_max_speed,
                              self.s._name_and_max_speed(self.s._STAR_SHIPS), list)

    def test_name_and_max_speed_v(self):
        return self.is_raises(self.s.name_and_max_speed_v,
                              self.s.name_and_max_speed_v(), list)

    def test_name_and_max_speed_s(self):
        return self.is_raises(self.s.name_and_max_speed_s,
                              self.s.name_and_max_speed_s(), list)

    def test__find_slowest_speed(self):
        return self.is_raises(self.s._find_slowest_speed,
                              self.s._find_slowest_speed(self.s._VEHICLES), dict)

    def test_find_slowest_s(self):
        return self.is_raises(self.s.find_slowest_s,
                              self.s.find_slowest_s(), dict)

    def test_find_slowest_v(self):
        return self.is_raises(self.s.find_slowest_v,
                              self.s.find_slowest_v(), dict)

    def test__get_transport(self):
        self.assertRaises(Exception, self.s._get_transport, self.ha)
        self.assertIs(type(self.s._get_transport(self.s._VEHICLES)), dict)

    def is_raises(self, argA, argB, argC):
        """ Method auxiliary for assertRaises and assertIs """
        self.assertRaises(Exception, argA, self.ha)
        self.assertIs(type(argB), argC)


if __name__ == '__main__':
    unittest.main()