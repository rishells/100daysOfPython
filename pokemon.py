import requests
import json

url = 'http://pokeapi.co/api/v2/pokemon/'

def buscarPokemon():
    pokemon_number = int(input("Ingresa el numero de pokemon: "))
    peticion = requests.get(url + str(pokemon_number))
    respuesta = json.loads(peticion.content)
    print(respuesta['name'])

keep_searching_pokemons = True
while keep_searching_pokemons:
    buscarPokemon()
    user_response = input("¿Deseas buscar otro pokemon? y | n ")
    if user_response.lower() == 'y':
        keep_searching_pokemons = True
    elif user_response.lower() == 'n':
        keep_searching_pokemons = False
    else:
        print("Escribe una opcion valida")