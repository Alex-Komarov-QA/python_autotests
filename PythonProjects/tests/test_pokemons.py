import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ce6a804802e38127b8f8c2b47eea93d0'
HEADER =  {'Content-Type' : 'application/json', 'trainer_token' : TOKEN }
TRAINER_ID = '39132'

def test_status_code():
     response = requests.get(url= f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
     assert response.status_code==200

    
