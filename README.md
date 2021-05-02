# IP Lookup challenge
Python challenge with interactive menu. Receives a list or a list of ips in order to get RDAP and GEO data of them.

# Structure
```bash
├── config
│   └── configs.py
├── lookups
│   ├── geo_ip_lookup.py
│   ├── lookup_helper.py
│   └── rdap_ip_lookup.py
├── parsers
│   ├── parser.py
│   └── list_of_ips.txt
├── main_program.py
├── parsing
│   ├── __init__.py
│   └── parsing.py
├── .gitignore
├── README.md
└── main.py


Running the code:
To run the code you only need to call to main.py

```bash
$ python3 main.py
```

## configs
Some configs are detailed here, at the moment we only have requests timeout and the regex for IPs.

## lookups
There is a class called LookupHelper at lookups/lookup_helper.py that holds all the calls to a certain lookup which is defined at a child level (rdap_ip_lookup.py for RDAP and geo_ip_lookup.py for GEO). Multiproccesing is the logic chosen to achieve a faster result when iterating over big chunks of data. A lookup receives a list of IPs and returns the same list with the data added, this is allocated inside a key defined by the attribute lookup_name.

## parsing
In this project we can find a parser at parsers/parser.py which receives a txt path, it will search for ips with the help of a regex, a dictionary with empty values and ips as keys is going to be returned.

## main
main.py is the python code that runs the whole project, it has a interactive menu.

# Things that can be improved
Due lack of time, I was not able to implement:
- A redis/mongodb cache for the current ips so it can work faster or it can be allocated inside a disk.
- Unit testing. Especially for lookup_helper.py. Mocking a service there would be great. Curretly doens't have coverage.