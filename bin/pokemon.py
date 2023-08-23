import requests as r
from abc import ABC, abstractmethod

class IPokemonAPI(ABC):
    @abstractmethod
    def get_pokemon(self, pokemon_name:str=None, id:int=None):
        pass


class PokemonAPI(IPokemonAPI):
    def __init__(self):
        self.base_url = 'https://pokeapi.co/api/v2'

    def get_pokemon(self, pokemon_name:str=None, id:int=None):
        if pokemon_name:
            endpoint = f"{self.base_url}/pokemon/{pokemon_name.lower()}"
        elif id:
            endpoint = f"{self.base_url}/pokemon/{id}"
        else:
            return "Please provide either a Pokémon name or ID" 

        response = r.get(endpoint)
        return response.json()

class Pokemon:
    def __init__(self, pokemon_api: IPokemonAPI, pokemon_name:str=None, id:int=None):
        self.pokemon = pokemon_api.get_pokemon(pokemon_name, id)
        self.id = self.pokemon['id']
        self.name = self.pokemon['name']
        self.base_experience = self.pokemon['base_experience']
        self.is_default = self.pokemon['is_default']
        self.height = self.pokemon['height']
        self.order = self.pokemon['order']
        self.weight = self.pokemon['weight']
        self.abilities = self.pokemon['abilities']
        self.forms = self.pokemon['forms']
        self.game_indicies = self.pokemon['game_indices']
        self.held_items = self.pokemon['held_items']
        self.location_area_encounters = self.pokemon['location_area_encounters']
        self.moves = self.pokemon['moves']
        self.past_types = self.pokemon['past_types']
        self.sprites = self.pokemon['sprites']
        self.species = self.pokemon['species']
        self.stats = self.pokemon['stats']
        self.types = self.pokemon['types']

char = Pokemon(pokemon_api=PokemonAPI(), pokemon_name='charizard').types
print(char)
