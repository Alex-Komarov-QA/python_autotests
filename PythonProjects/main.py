import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ce6a804802e38127b8f8c2b47eea93d0'
HEADER =  {'Content-Type' : 'application/json', 'trainer_token' : TOKEN }
body_registration = {
    "trainer_token": TOKEN ,
    "email": "alexanis@mail.ru",
    "password": "05051985Koma!"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 12
}
body_change = {
    "pokemon_id": "334971",
    "name": "Буба",
    "photo_id": 12
}
body_catch = {
    "pokemon_id": "334971"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER , json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER , json = body_confirmation) 
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER , json = body_create) 
print(response_create.text)'''

'''message = response_create.json()['message']
print(message)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER , json = body_change)
print(response_change.text)'''

'''response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER , json = body_catch)
print(response_catch.text)'''