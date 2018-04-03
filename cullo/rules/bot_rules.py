from random import randint

INIT=0
VALID=1
DELIVERED=2
ORDERED=3

import time

air_fare_list = ['ACM Air Charter -> 23EUR',   'ADAC Luftrettung -> 34EUR',   'Aero-Dienst -> 456EUR',   'AeroLogic -> 67EUR',   'Air Hamburg -> 68EUR',   'Air Independence -> 234EUR',   'air-taxi europe -> 56EUR',   'AirGO Flugservice -> 678EUR',   'Arcus-Air -> 678EUR',   'Avanti Air -> 678EUR',   'Bin Air -> 896EUR',   'Businesswings -> 150EUR',   'Condor -> 234EUR',   'DC Aviation -> 678EUR',   'Deutsche Lufthansa Berlin-Stiftung -> 242EUR',   'Deutsche Zeppelin Reederei -> 78EUR',   'DRF Stiftung Luftrettung gemeinnützige -> 78EUR',   'European Air Transport Leipzig -> 65EUR',   'Eurowings -> 23EUR',   'FAI rent-a-jet -> 456EUR',   'FLN Frisia Luftverkehr -> 234EUR',   'Germania -> 78EUR',   'Hahn Air -> 45EUR',   'Jet Executive -> 12EUR',   'Luftfahrtgesellschaft Walter -> 789EUR',   'Lufthansa -> 435EUR',   'Lufthansa Cargo -> 67EUR',   'Lufthansa CityLine -> 89EUR',   'OFD-Ostfriesischer- Flug-Dienst -> 456EUR',   'PrivatAir (Germany) -> 456EUR',   'Private Wings -> 67EUR',   'RWL German Flight Academy -> 234EUR',   'Stuttgarter Flugdienst -> 150EUR',   'Sundair -> 78EUR',   'SunExpress Deutschland -> 24EUR',   'Sylt Air -> 78EUR',   'TUIfly -> 234EUR',   'WDL Aviation -> 456EUR',   'Wiking Helikopter Service ->  45EUR',   'Windrose Air -> 212' ]
flight_list = ['ACM Air Charter',   'ADAC Luftrettung',   'Aero-Dienst',   'AeroLogic',   'Air Hamburg',   'Air Independence',   'air-taxi europe',   'AirGO Flugservice',   'Arcus-Air',   'Avanti Air',   'Bin Air',   'Businesswings',   'Condor',   'DC Aviation',   'Deutsche Lufthansa Berlin-Stiftung',   'Deutsche Zeppelin Reederei',   'DRF Stiftung Luftrettung gemeinnützige',   'European Air Transport Leipzig',   'Eurowings',   'FAI rent-a-jet',   'FLN Frisia Luftverkehr',   'Germania',   'Hahn Air',   'Jet Executive',   'Luftfahrtgesellschaft Walter',   'Lufthansa',   'Lufthansa Cargo',   'Lufthansa CityLine',   'OFD-Ostfriesischer- Flug-Dienst',   'PrivatAir (Germany)',   'Private Wings',   'RWL German Flight Academy',   'Stuttgarter Flugdienst',   'Sundair',   'SunExpress Deutschland',   'Sylt Air',   'TUIfly',   'WDL Aviation',   'Wiking Helikopter Service',   'Windrose Air'];
def random_fare_list():
    return air_fare_list[randint(0, 9)] + ", " + air_fare_list[randint(0, 9)] + ", "+air_fare_list[randint(0, 9)] + ", " + air_fare_list[randint(0, 9)]


def random_flights():
    return flight_list[randint(0, 9)] + ", " + flight_list[randint(0, 9)] + ", "+flight_list[randint(0, 9)] + ", " + flight_list[randint(0, 9)]


def get_bot_rules():
    """This method returns the chatbot rules"""
    return{
        (INIT, "atis_airfare"): (INIT, "Please enter your ID number for validation", VALID),
        (INIT, "number"): (VALID, "Perfect, welcome back!, ", None),
        (VALID, "atis_flight"): (DELIVERED, "The available flights are: " + random_flights(), None),
        (VALID, "atis_airfare"): (DELIVERED, "The best fares for you are: " + random_fare_list() , None),
        (DELIVERED, "atis_flight"): (DELIVERED, "The available flights are: " + random_flights(), None),
        (DELIVERED, "atis_airfare"): (DELIVERED, "The best fares for you are: " + random_fare_list() , None)
    }