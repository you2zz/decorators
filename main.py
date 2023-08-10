import requests
from tools import speed_check, printable, cached


cached_100 = cached(max_size=100)
@speed_check
# @cached(max_size=100)

@cached_100
def get_swapi_person(person_id):
    return requests.get(f'https://swapi.py4e.com/api/people/{person_id}').json()

get_swapi_person(4)

get_swapi_person(4)

