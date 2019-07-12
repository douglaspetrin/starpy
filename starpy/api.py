import requests


class StarPyMae(object):

    """ Classe Mãe

    Descrição: \n Faz a chamada da api e coleta dados para manipulação. \n
    Ex: s = StarPyMae()

    """

    # Endpoints

    VEHICLES = 'vehicles'
    PEOPLE = 'people'
    STAR_SHIPS = 'starships'

    # Low-levels of resource

    MAX_ATMOSPHERING_SPEED = 'max_atmosphering_speed'

    def __init__(self):
        self.base_url = 'https://swapi.co/api'

    def sget(self, endpoint, resource=None):
        if resource is None:
            end, r = '%s/%s/', (self.base_url, endpoint)
        else:
            end, r = '%s/%s/%s/', (self.base_url, endpoint, resource)
        return requests.get(end % r).json()

    def get_next_page(self, endpoint, i):
        return self.sget(endpoint + '?page=' + str(i))


class People(StarPyMae):

    def get_people(self, res=None):
        return self.sget(self.PEOPLE, res)

    def get_people_by_id(self, rid):
        return self.get_people(rid)


class Vehicles(StarPyMae):

    def get_vehicles(self, res=None):
        return self.sget(self.VEHICLES, res)

    def get_vehicles_by_id(self, rid):
        return self.get_vehicles(rid)


class Starships(StarPyMae):

    def get_starships(self, res=None):
        return self.sget(self.STAR_SHIPS, res)

    def get_starships_by_id(self, rid):
        return self.get_starships(rid)