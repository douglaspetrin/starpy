import requests
import pandas as pd
import fire


class StarPyMae(object):

    """ Classe Mãe

    Descrição: \n Faz a chamada da api e coleta dados para manipulação. \n

    """

    # Endpoints

    VEHICLES = 'vehicles'
    PEOPLE = 'people'
    STAR_SHIPS = 'starships'

    # Low-levels of resource

    def __init__(self):
        self.base_url = 'https://swapi.co/api'

    def _sget(self, endpoint, resource=None):
        if resource is None:
            end, r = '%s/%s', (self.base_url, endpoint)
        else:
            end, r = '%s/%s/%s/', (self.base_url, endpoint, resource)
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

    def _get_transport(self, transport, res=None):
        return self._sget(transport, res)

    def get_vehicles(self, res=None):
        """ Recebe vehicles """
        return self._get_transport(self.VEHICLES, res)

    def get_vehicles_by_id(self, rid):
        """ Recebe vehicles por id
            :param rid :type int
        """
        return self.get_vehicles(rid)

    def get_starships(self, res=None):
        """ Recebe starships """
        return self._get_transport(self.STAR_SHIPS, res)

    def get_starships_by_id(self, rid):
        """
        Recebe starships por id
        :param rid :type: int
        :return:
        """
        return self.get_starships(rid)

    def _if_transport(self, transport):
        """ Verifica qual tipo de transporte está sendo requisitado """
        v = None
        if transport == self.VEHICLES:
            v = self.get_vehicles()
        elif transport == self.STAR_SHIPS:
            v = self.get_starships()
        return v

    def _find_pilots_from_df(self, transport):
        """ Versão do tipo Dataframe """
        v = self._if_transport(transport)
        page, li2 = 1, []
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

    def _find_fastest_transport_name_and_its_speed(self, transport):
        df = self._df_of_transport(transport)
        f, kl = df[2].nlargest(3), []
        for i in range(len(f)):
            n_index = f.index[i]
            n_transporte = df[1][n_index]
            kl.append(n_transporte)
        return kl, f.to_dict()

    def _find_fastest_speed(self, transport):
        """ Cria DataFrame dos transportes mais rápidos """
        return self._find_fastest_transport_name_and_its_speed(transport)[1]

    def _find_fastest_trans_name(self, transport):
        return self._find_fastest_transport_name_and_its_speed(transport)[0]

    def find_fastest_v(self):
        """ Encontra veículos mais rápidos e que tenham pilotos """
        return self._find_fastest_speed(self.VEHICLES)

    def find_fastest_s(self):
        """ Encontra naves mais rápidas e que tenham pilotos """
        return self._find_fastest_speed(self.STAR_SHIPS)

    def _df_of_transport(self, transport):
        """ Cria DataFrame para fácil manipulação """

        l2 = self._find_pilots_from_df(transport)
        df = pd.DataFrame(l2)
        df[2].replace(regex=True, inplace=True, to_replace='\D', value=r'0')
        df[2] = pd.to_numeric(df[2])
        return df

    def _url_of_fastest_pilot(self, transport):
        fastest = self._find_fastest_speed(transport)
        fastest, url_list = list(fastest.keys()), []
        for i in range(len(fastest)):
            df, n = self._df_of_transport(transport), fastest[i]
            url_list.append(df[0][n][0])
        return url_list

    def _url_fastest_pilot_v(self):
        return self._url_of_fastest_pilot(self.VEHICLES)

    def _url_fastest_pilot_s(self):
        return self._url_of_fastest_pilot(self.STAR_SHIPS)

    def _id_fastest_pilots(self, transport):
        pilot_id, il = self._url_of_fastest_pilot(transport), []
        for i in range(len(pilot_id)):
            pid = pilot_id[i].split('/')[-2]
            il.append(pid)
        return il

    def _id_fastest_pilots_v(self):
        return self._id_fastest_pilots(self.VEHICLES)

    def _id_fastest_pilots_s(self):
        return self._id_fastest_pilots(self.STAR_SHIPS)

    def _names_pilots(self, transport):
        l_ids, l_names = self._id_fastest_pilots(transport), []
        for i in range(len(l_ids)):
            name = self.get_people_by_id(int(l_ids[i]))['name']
            l_names.append(name)
        return l_names

    def names_pilots_v(self):
        return self._names_pilots(self.VEHICLES)

    def names_pilots_s(self):
        return self._names_pilots(self.STAR_SHIPS)

    def _name_and_max_speed(self, transport):
        n, sp, lis = self._names_pilots(transport), list(self._find_fastest_speed(transport).values()), []
        trans = self._find_fastest_trans_name(transport)
        transport_name = transport.capitalize()[:-1] + ' name'
        for i in range(len(n)):
            li = [{'Name': n[i], 'Max. Speed': sp[i], transport_name: trans[i]}]
            lis.append(li)
        return lis

    def name_and_max_speed_v(self):
        return self._name_and_max_speed(self.VEHICLES)

    def name_and_max_speed_s(self):
        return self._name_and_max_speed(self.STAR_SHIPS)

    def _by_idpeople_return_transport_speed(self, transport, idname):
        lss, transport_urls_id = [], self.get_people_by_id(idname)[transport]
        for i in range(len(transport_urls_id)):
            url_id = transport_urls_id[i].split('/')[-2]
            speed = self._by_idtransports_return_its_speed(transport, url_id)
            ldata = [{'transport_id': url_id, 'Max. Speed': speed}]
            lss.append(ldata)
        return lss

    def _by_idtransports_return_its_speed(self, transport, idtrans):
        return self._get_transport(transport, idtrans)['max_atmosphering_speed']

    def starships_speed_by_people(self, idpeople):
        return self._by_idpeople_return_transport_speed(self.STAR_SHIPS, idpeople)

    def vehicles_speed_by_people(self, idpeople):
        return self._by_idpeople_return_transport_speed(self.VEHICLES, idpeople)

    def _fastest_person(self, transport):
        return self._name_and_max_speed(transport)[0]

    def fastest_person_with_v(self):
        """ Retorna o nome da pessoa, do vehicle e velocidade máxima """
        return self._fastest_person(self.VEHICLES)

    def fastest_person_with_s(self):
        """ Retorna o nome da pessoa, da starship e velocidade máxima """
        return self._fastest_person(self.STAR_SHIPS)


s = GetStars()

""" StarPy CLI """
# if __name__ == '__main__':
#     fire.Fire(GetStars)