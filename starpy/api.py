import requests
import pandas as pd
import fire

class StarPyMae(object):

    """ Classe Mãe

    Descrição: \n Faz a chamada da api e coleta dados para manipulação. \n

    """

    # Endpoints

    VEHICLES = 'vehicles/'
    PEOPLE = 'people/'
    STAR_SHIPS = 'starships/'

    # Low-levels of resource

    MAX_ATMOSPHERING_SPEED = 'max_atmosphering_speed'

    def __init__(self):
        self.base_url = 'https://swapi.co/api'

    def _sget(self, endpoint, resource=None):
        if resource is None:
            end, r = '%s/%s' , (self.base_url, endpoint)
        else:
            end, r = '%s/%s%s/' , (self.base_url, endpoint, resource)
        return requests.get(end % r).json()

    def get_next_page(self, endpoint, i):
        return self._sget(endpoint='%s?page=%s' % (endpoint, i), resource=None)


class GetStars(StarPyMae):

    def get_people(self, res=None):
        """ Recebe people """
        return self._sget(self.PEOPLE, res)

    def get_people_by_id(self, rid):
        """ Recebe people por id
            :param rid :type int
        """
        return self.get_people(rid)

    def get_vehicles(self, res=None):
        """ Recebe vehicles """
        return self._sget(self.VEHICLES, res)

    def get_vehicles_by_id(self, rid):
        """ Recebe vehicles por id
            :param rid :type int
        """
        return self.get_vehicles(rid)

    def get_starships(self, res=None):
        """ Recebe starships """
        return self._sget(self.STAR_SHIPS, res)

    def get_starships_by_id(self, rid):
        """
        Recebe starships por id
        :param rid :type: int
        :return:
        """
        return self.get_starships(rid)

    def _find_pilots_from_li(self, transport):
        """ Versão do tipo lista """
        if transport == self.VEHICLES:
            vm = self.get_vehicles()
        else:
            vm = self.get_starships()

        v, page, l = vm, 1, []
        while v['next'] is not None:
            v = v['results']
            for i in range(len(v)):
                if v[i]['pilots']:
                    li = [
                        [
                            {'i': i},
                            {'pilots_url': v[i]['pilots']},
                            {'name': v[i]['name']},
                            {'max_speed': v[i]['max_atmosphering_speed']}
                        ]
                    ]
                    l.append(li) # python only
            page += 1
            v = self.get_next_page(transport, page)

        v = self.get_next_page(transport, page)['results']
        for j in range(len(v)):
            if v[j]['pilots'] and v[j]['max_atmosphering_speed']:
                li = [
                    [
                        {'j': j},
                        {'pilots_url': v[j]['pilots']},
                        {'name': v[j]['name']},
                        {'max_speed': v[j]['max_atmosphering_speed']}
                    ]
                ]
                l.append(li)
        return l

    def _find_pilots_from_df(self, transport):
        """ Versão do tipo Dataframe """
        if transport == self.VEHICLES:
            vm = self.get_vehicles()
        else:
            vm = self.get_starships()

        v, page, li2 = vm, 1, []
        while v['next'] is not None:
            v = v['results']
            for i in range(len(v)):
                if v[i]['pilots']:
                    lista = v[i]['pilots'], v[i]['name'], v[i]['max_atmosphering_speed'], 'i', i
                    li2.append(lista)
            page += 1
            v = self.get_next_page(transport, page)

        v = self.get_next_page(transport, page)['results']
        for j in range(len(v)):
            if v[j]['pilots'] and v[j]['max_atmosphering_speed']:
                lista = v[j]['pilots'], v[j]['name'], v[j]['max_atmosphering_speed'], 'j', j
                li2.append(lista)
        return li2

    def find_pilots_from_v(self):
        return self._find_pilots_from_df(self.VEHICLES)

    def find_pilots_from_s(self):
        return self._find_pilots_from_df(self.STAR_SHIPS)

    def _find_fastest_df(self, transport):
        """ Cria DataFrame para fácil manipulação """
        df = self._df_of_transport(transport)
        return df[2].nlargest(3).to_dict()

    def _find_fastest_li(self, transport):
        """ Obsoleto? """
        pass

    def find_fastest_v(self):
        """ Encontra veículos mais rápidos e que tenham pilotos """
        return self._find_fastest_df(self.VEHICLES)

    def find_fastest_s(self):
        """ Encontra naves mais rápidas e que tenham pilotos """
        return self._find_fastest_df(self.STAR_SHIPS)

    def _df_of_transport(self, transport):
        """ Cria DataFrame para fácil manipulação """

        l2 = self._find_pilots_from_df(transport)
        df = pd.DataFrame(l2)
        df[2].replace(regex=True, inplace=True, to_replace='\D', value=r'0')
        df[2] = pd.to_numeric(df[2])
        return df


s = GetStars()

""" StarPy CLI """
# if __name__ == '__main__':
#     fire.Fire(GetStars)