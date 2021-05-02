from lookups.lookup_helper import LookupHelper

class GEOIpLookup(LookupHelper):

    service_url    = "https://freegeoip.app/json/"
    response_names = ['latitude', 'longitude', 'country_name']
    lookup_name    = 'GEO'

    def __init__(self, list_of_ips):
        """ 
            Performs GEOIp lookup for a list of ips.

            Parameters:
            list_of_ips: is the list of ips filtered by cache
        """
        super().__init__(list_of_ips)
    