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
    def __init__(self, pokemon_api: PokemonAPI, pokemon_name:str=None, id:int=None):
        self.pokemon = pokemon_api.get_pokemon(pokemon_name, id)
    @property
    def get_name(self):
        return self.pokemon['name']
    @property
    def get_id(self):
        return self.pokemon['id']
    @property
    def get_base_experience(self):
        return self.pokemon['base_experience']
    @property
    def get_height(self):
        return self.pokemon['height']
    @property
    def get_is_default(self):
        return self.pokemon('is_default')
    @property
    def get_order(self):
        return self.pokemon['order']
    @property
    def get_weight(self):
        return self.pokemon['weight']
    @property
    def get_abilities(self):
        return self.pokemon['abilities']
    @property
    def get_forms(self):
        return self.pokemon['forms']
    @property
    def get_game_indices(self):
        return self.pokemon['game_indices']
    @property
    def get_held_items(self):
        return self.pokemon['held_items']
    @property
    def get_location_area_encounters(self):
        return self.pokemon['location_area_encounters']
    @property
    def get_moves(self):
        return self.pokemon['moves']
    @property
    def get_past_types(self):
        return self.pokemon['past_types']
    @property
    def get_sprites(self):
        return self.pokemon['sprites']
    @property
    def get_species(self):
        return self.pokemon['species']
    @property
    def get_stats(self):
        return self.pokemon['stats']
    @property
    def get_types(self):
        return self.pokemon['types']

char = Pokemon(pokemon_api=PokemonAPI(), pokemon_name='charizard').get_types
print(char)
