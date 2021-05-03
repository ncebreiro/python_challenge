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
```

Running the code:
To run the code you only need to call to main.py


```bash
$ python3 main.py
```

## configs
Some configs are detailed here, at the moment we only have requests timeout and the regex for IPs.

## lookups
There is a class called LookupHelper at lookups/lookup_helper.py that holds all the calls to a certain lookup service which is defined at a child level:
- RDAP: rdap_ip_lookup.py
- GEO: geo_ip_lookup.py

LookupHelper uses ultiproccesing in order to achieve a faster result with multiples calls in pararel. A lookup receives a list of IPs and returns the same list with the data added, this is allocated inside a key defined by the attribute lookup_name.

## parsing
In this project we can find a parser at parsers/parser.py which receives a txt path, it will search for ips using regex. A dictionary with empty values and ips as keys is going to be returned.

## main
main.py is the python code that runs the whole project, it has an interactive menu.

# Things that can be improved
Due lack of time, I was not able to implement:
- A Redis or Mongodb cache. If we were using Redis, the performance of the cache would be increased. Using mongodb or any disk db would be nice if we want to have the data stored for ever.
- Unit testing. Especially for lookup_helper.py. Mocking a service there would be great. Curretly doesn't have coverage.