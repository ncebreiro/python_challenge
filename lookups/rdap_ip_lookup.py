from lookups.lookup_helper import LookupHelper

class RDAPIpLookup(LookupHelper):

    service_url    = "https://rdap.arin.net/registry/ip/"
    response_names = ['name', 'startAddress']
    lookup_name    = 'RDAP'

    def __init__(self, list_of_ips):
        """ 
            Performs RDAPIp lookup for a list of ips.

            Parameters:
            list_of_ips: is the list of ips filtered by cache
        """
        super().__init__(list_of_ips)