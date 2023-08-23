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
    @property
    def get_types(self):
        type_list = []
        types = self.types
        for type in types:
            type_list.append(type['type']['name'])
        return {'types':type_list}
    @property
    def get_abilities(self):
        abilities_list = []
        abilities = self.abilities
        for ability in abilities:
            abilities_list.append(ability['ability']['name'])
        return {'abilities':abilities_list}
    @property
    def get_forms(self):
        forms_list = []
        forms = self.forms
        for form in forms:
            forms_list.append(form['name'])
        return {'forms':forms_list}
    @property
    def get_games(self):
        games_list = []
        games = self.game_indicies
        for game in games:
            games_list.append(game['version']['name'])
        return {'games':games_list}
    @property
    def get_held_items(self):
        held_items_list = []
        held_items_dict = {}
        version_list = []
        held_items = self.held_items
        for item in held_items:
            held_items_dict['item'] = item['item']['name']
            for version in item['version_details']:
                version_list.append(version['version']['name'])
            held_items_dict['version'] = version_list
            held_items_list.append(held_items_dict)
        return held_items_list
    @property
    def get_moves(self):
        move_list = []
        moves = self.moves
        for move in moves:
            move_list.append(move['move']['name'])
        return move_list
        