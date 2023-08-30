import requests as r
from abc import ABC, abstractmethod
from urllib.parse import urlparse

def get_number_from_url(url):
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.strip('/').split('/')
    return path_parts[-1] if path_parts[-1].isdigit() else None

class IPokemonAPI(ABC):
    @abstractmethod
    def get_pokemon(self, pokemon_name:str=None, id:int=None):
        pass
    def get_evolutions(self, id:int):
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
    
    def get_evolutions(self, pokemon_name:str=None, id:int=None):
        if pokemon_name:
            endpoint = f"{self.base_url}/pokemon-species/{pokemon_name.lower()}"
        elif id:
            endpoint = f"{self.base_url}/pokemon-species/{id}"
        else:
            return "Please provide either a Pokémon name or ID" 

        response = r.get(endpoint)
        return response.json()


class Pokemon:
    def __init__(self, pokemon_api: IPokemonAPI, pokemon_name:str=None, id:int=None):
        self.pokemon = pokemon_api.get_pokemon(pokemon_name, id)
        self.evolutions = pokemon_api.get_evolutions(pokemon_name, id)
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
        self.previous_evolution = self.evolutions['evolves_from_species']    
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
            games_list.append({'game_id':get_number_from_url(game['version']['url']), 
                                                             'game':game['version']['name']})
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
            move_list.append({'move_id': get_number_from_url(move['move']['url']),
                              'move':move['move']['name']})
        return move_list
    @property
    def get_previous_evolution_id(self):
        try:
            previous_evolution_name = self.previous_evolution['name']
            id = Pokemon(PokemonAPI(), pokemon_name=previous_evolution_name).id
        except TypeError:
            return None
        else:
            return id
    @property
    def get_stats(self):
        stat_list = []
        stat_dict = {}
        stats = self.stats
        for stat in stats:
            stat_dict[stat['stat']['name']] = stat['base_stat']
        stat_list.append(stat_dict)
        return stat_list
    
# pokemon = Pokemon(PokemonAPI(), 'charizard')
# print(pokemon.name)