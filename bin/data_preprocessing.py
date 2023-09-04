import pokemon as p
import os
import logging
import logging.config
import pandas as pd
import numpy as np
from abc import ABC, abstractmethod

# Get the absolute directory of the current script
abs_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the logging configuration file
logging_config_path = os.path.join(abs_dir, '..', 'util', 'logging_to_file.conf')

logging.config.fileConfig(fname=logging_config_path)

# Get the custom Logger from Configuration File
logger = logging.getLogger(__name__)

class Dataset:
    def __init__(self, pokemon_api, number_of_pokemon:int):
        self.pokemon_formatter = PokemonFormatter(pokemon_api)
        self.number_of_pokemon = number_of_pokemon
        self.list_of_pokemon_ids = self.create_list_of_pokemon_ids()

    def create_list_of_pokemon_ids(self):
        return list(range(1, self.number_of_pokemon + 1))
    
    @staticmethod
    def flatten_dict(pokemon_field_list):
        flattened_pokemon = {}
        for item in pokemon_field_list:
            pokemon_id = item['pokemon_id']
            if pokemon_id not in flattened_pokemon:
                flattened_pokemon[pokemon_id] = {}
            flattened_pokemon[pokemon_id].update(item) 
        return flattened_pokemon
        
    def flatten_field(self, pokemon_field_list, field_name):
        flattened_pokemon = {}
        for item in pokemon_field_list:
            pokemon_id = item['pokemon_id']
            if pokemon_id not in flattened_pokemon:
                flattened_pokemon[pokemon_id] = {}
            flattened_pokemon[pokemon_id].update({field_name: item[field_name]})
        return flattened_pokemon
    
    @staticmethod
    def create_table(list_of_fields):
        for field in list_of_fields:
            flattened_pokemon = Dataset.flatten_dict(pokemon_field_list=field)
        return flattened_pokemon    

class IPokemonFormatter(ABC):
    @abstractmethod
    def format_weight(self, list_of_pokemon_ids):
        pass
    @abstractmethod
    def format_height(self, list_of_pokemon_ids):
        pass
    @abstractmethod
    def format_stats(self, list_of_pokemon_ids):
        pass
    @abstractmethod
    def format_moves(self, list_of_pokemon_ids):
        pass
    @abstractmethod
    def format_abilities(self, list_of_pokemon_ids):
        pass
    @abstractmethod
    def format_games(self, list_of_pokemon_ids):
        pass
    @abstractmethod
    def format_previous_evolutions(self, list_of_pokemon_ids):
        pass
    @abstractmethod
    def format_types(self, list_of_pokemon_ids):
        pass
    @abstractmethod
    def format_names(self, list_of_pokemon_ids):
        pass

class PokemonFormatter(IPokemonFormatter):
    def __init__(self, pokemon_api):
        self.pokemon_api = pokemon_api

    def format_weight(self, list_of_pokemon_ids):
        list_of_weights = []
        for id in list_of_pokemon_ids:
            pokemon = p.Pokemon(self.pokemon_api, id=id)
            weight = pokemon.weight
            list_of_weights.append({'pokemon_id':id, 'weight':weight})
        return list_of_weights  
    
    def format_height(self, list_of_pokemon_ids):
        list_of_heights = []
        for id in list_of_pokemon_ids:
            pokemon = p.Pokemon(self.pokemon_api, id=id)
            height = pokemon.height
            list_of_heights.append({'pokemon_id':id, 'height':height})
        return list_of_heights  
    
    def format_stats(self, list_of_pokemon_ids):
        list_of_stats = []
        for id in list_of_pokemon_ids:
            pokemon = p.Pokemon(self.pokemon_api, id=id)
            stats = pokemon.get_stats
            stats[0]['pokemon_id'] = id
        list_of_stats.append(stats)
        return list_of_stats
    
    def format_moves(self, list_of_pokemon_ids):
        list_of_moves = []
        for id in list_of_pokemon_ids:
            pokemon = p.Pokemon(self.pokemon_api, id=id)
            moves = pokemon.get_moves
            for i in range(len(moves)):
                moves[i]['pokemon_id'] = id
            list_of_moves.append(moves)            
        return list_of_moves
    
    def format_abilities(self, list_of_pokemon_ids):
        list_of_abilities = []
        for id in list_of_pokemon_ids:
            pokemon = p.Pokemon(self.pokemon_api, id=id)
            abilities = pokemon.get_abilities
            abilities['pokemon_id'] = id
            list_of_abilities.append(abilities)            
        return list_of_abilities
    
    def format_games(self, list_of_pokemon_ids):
        list_of_games = []
        for id in list_of_pokemon_ids:
            pokemon = p.Pokemon(self.pokemon_api, id=id)
            games = pokemon.get_games
            inner_games = games.get('games', [])  # Get the inner 'games' list
            for inner_game in inner_games:
                inner_game['pokemon_id'] = id  # Add the pokemon_id to each inner game dictionary
            list_of_games.append(games)
        return list_of_games
    
    def format_previous_evolutions(self, list_of_pokemon_ids):
        list_of_evolutions = []
        for id in list_of_pokemon_ids:
            pokemon = p.Pokemon(self.pokemon_api, id=id)
            evolution = pokemon.get_previous_evolution_id
            pokemon_dict = {'pokemon_id': id, 'evolution_id': evolution if evolution is not None else 0}
            list_of_evolutions.append(pokemon_dict)            
        return list_of_evolutions
    
    def format_types(self, list_of_pokemon_ids):
        list_of_types = []
        for id in list_of_pokemon_ids:
            pokemon = p.Pokemon(self.pokemon_api, id=id)
            types = pokemon.get_types
            types['pokemon_id'] = id
            list_of_types.append(types)            
        return list_of_types
    
    def format_names(self, list_of_pokemon_ids):
        list_of_names = []
        for id in list_of_pokemon_ids:
            pokemon = p.Pokemon(self.pokemon_api, id=id)
            name = pokemon.name
            name_dict = {'pokemon_id':id, 'name':name}
            list_of_names.append(name_dict)            
        return list_of_names   
    

# pokemon_api = p.PokemonAPI()  # Assuming PokemonAPI is your API class
# dataset = Dataset(pokemon_api, 10)

# formatted_weights = dataset.pokemon_formatter.format_weight(dataset.list_of_pokemon_ids)
# print(formatted_weights)