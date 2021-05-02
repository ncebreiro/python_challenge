from lookups.geo_ip_lookup import GEOIpLookup
from lookups.rdap_ip_lookup import RDAPIpLookup
from parsers.parser import TxtParser

class MainIterator(object):

    LOOKUPS_CLASSES = [GEOIpLookup, RDAPIpLookup]

    def __init__(self):
        self.list_of_ips = {}
    
    def menu(self):
        user_input = None
        while user_input != '4':
            print('Welcome, what would you like to do?')
            print('1- Look for collection of IPs inside a txt')
            print('2- Insert any IP manually')
            print('3- Print current values')
            print('4- Exit')
            print('----------------------------------')
            user_input = str(input()).strip()
            if user_input == '1':
                print('Please insert a path for the file OR leave a blank response for the default location which is the current one and the file must be called "list_of_ips.txt"')
                txt_path = str(input()).strip()

                # calling to parser. Sending txt path and current cache
                txt_parser = TxtParser(current_list_of_ips = self.list_of_ips.keys(), path = txt_path)

                # the response of TxtParser.parse() is a dictionary with empty values
                list_of_ips = txt_parser.parse()

                self.__asking_for_new_ip(list_of_ips)

            elif user_input == '2':
                print('Please write down the desired ip')
                new_ip =  str(input()).strip()
                is_ip_at_cache = self.list_of_ips.get(new_ip, None)

                # not calling to GEO or RDAP if ip is already retrieved
                if is_ip_at_cache:
                    print('The ip inserted has already been used, do you want to see it? (yes/no)')
                    current_data_input = str(input()).strip()
                    if current_data_input == 'yes':
                        print(list_of_ips_with_completed_data)
                else:
                    self.__asking_for_new_ip({new_ip: {}})

            elif user_input == '3':
                self.__return_current_cache()

        print('Bye!')

    def __asking_for_new_ip(self, list_of_ips):
        """
            receives dictionary with empty values and ips as keys
        """

        # iterates over list of ips which is initialy the current cache and then it's getting populated with lookup's data
        for lookup_class in self.LOOKUPS_CLASSES:
            lookup = lookup_class(list_of_ips)
            lookup.get_lookup_response()

        print('Do you want to see the new data? (yes/no)')
        current_data_input = str(input()).strip()
        if current_data_input == 'yes':
            self.__return_current_cache(list_of_ips)

        # adding completed data to cache
        self.list_of_ips.update(list_of_ips)

    def __return_current_cache(self, list_of_ips = None):
        '''
            prints current cache
        '''
        list_of_ips = list_of_ips if list_of_ips else self.list_of_ips
        for ip, data in list_of_ips.items():
            print('Ip %s. Current RDAP: %s. Current GEO: %s' % (ip, data.get('RDAP'), data.get('GEO') ) ) 

main_iterator = MainIterator()
main_iterator.menu()