from abc import ABCMeta, abstractmethod
from configs.configs import REQUESTS_TIMEOUT

import multiprocessing
import requests


class LookupHelper(metaclass=ABCMeta):

    @property
    @abstractmethod
    def lookup_name(self):
        '''
            Key name that contains lookup data for list of ips returned
        '''
        pass

    @property
    @abstractmethod
    def service_url(self):
        '''
            Service url that's going to be called and will add a IP at the back of it
        '''
        pass

    @property
    @abstractmethod
    def response_names(self):
        '''
            Must be a list with names that are going to be extracted from service response
        '''
        pass

    def __init__(self, list_of_ips):
        """ 
            Performs lookup for a list of ips.

            Parameters:
            list_of_ips: is the list of ips filtered by cache
        """
        self.list_of_ips = list_of_ips
        self.session = requests.Session()

    def get_lookup_response(self):
        """
            Initialices process. Will call to lookup services while declaring multiprocessing logic.
            Returns the list of ips with the lookup object value.
        """

        # uses multriprocessing logic to iterate over ips
        with multiprocessing.Pool() as pool:
            lookups = pool.map(self._get_lookup, self.list_of_ips.keys())

            # iterating over process response, will add lookup to self.list_of_ips
            for lookup in lookups:
                if lookup:
                    for ip, lookup_data in lookup.items():
                        self.list_of_ips[ip][self.lookup_name] = lookup_data

        return self.list_of_ips

    def _get_lookup(self, ip):
        """
            Multiprocessing logic, per each ip will call to service lookup and return the response formated
        """
        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        url = "%s%s" % (self.service_url, ip)

        try:
            with self.session.get(url, headers = headers, timeout=REQUESTS_TIMEOUT) as response:
                if response.status_code != 200:
                    # this should be a logging error not a print
                    print('[%s] Error while trying to get %s lookup for %s' % (self.lookup_name, self.response_names, ip) )
                    return None

                json_response = response.json()

                # with response, will iterate over abstract attribute self.response_names to retreive values
                return {ip: { item: json_response[item] for item in self.response_names } }

        except Exception as e:
            print('[%s] Error %s: %s' % ( self.lookup_name, url, str(e) ) )
