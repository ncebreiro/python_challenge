from configs.configs import REGEX_DEFINITION

import re


class TxtParser(object):

    def __init__(self, current_list_of_ips = None, path = None):
        '''
            current_list_of_ips: is the collection of cached ips that are not going to be parsed
            path: receives the txt's path or uses the default 
        '''
        self.path                = path if path else 'parsers/list_of_ips.txt'
        self.current_list_of_ips = current_list_of_ips if current_list_of_ips else []

    def parse(self):
        '''
            Parses self.path and filtering ips inside self.current_list_of_ips
            return: Dict with empty values
        '''
        with open(self.path) as fh:
            fstring = fh.readlines()
            
            # regex definition for ips
            pattern = re.compile(REGEX_DEFINITION)
            
            # initializing the list object
            ip_collection = []
            
            # extracting the IP addresses
            for line in fstring:
                # getting ips from txt line with regex's help
                ips = pattern.findall(line)

                # checking that our ips are not cached inside self.current_list_of_ips
                ip_collection_without_existing = [ ip for ip in ips if ip not in self.current_list_of_ips ]

                # adding new ips to our collection
                ip_collection += ip_collection_without_existing
            
            # Returning data as a dictionary
            return dict.fromkeys(ip_collection, {})
