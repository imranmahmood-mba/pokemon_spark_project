import pokemon as p
import os
import logging
import logging.config
import pandas as pd
import numpy as np

# Get the absolute directory of the current script
abs_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the logging configuration file
logging_config_path = os.path.join(abs_dir, '..', 'util', 'logging_to_file.conf')

logging.config.fileConfig(fname=logging_config_path)

# Get the custom Logger from Configuration File
logger = logging.getLogger(__name__)

class Dataset:
    def __init__(self, pokemon_object:p.PokemonAPI, number_of_pokemon:int):
        self.pokemon = pokemon_object
        self.number_of_pokemon = number_of_pokemon
        self.list_of_pokemon_ids = self.create_list_of_pokemon_ids()

    def create_list_of_pokemon_ids(self):
        return list(range(1, self.number_of_pokemon + 1))

    def format_weight(self, list_of_pokemon_ids):
        list_of_weights = []
        for id in list_of_pokemon_ids:
            pokemon = p.Pokemon(p.PokemonAPI(), id=id)
            weight = pokemon.weight
            list_of_weights.append({'id':id, 'weight':weight})
        return list_of_weights  
    
    def format_height(self, list_of_pokemon_ids):
        list_of_heights = []
        for id in list_of_pokemon_ids:
            pokemon = p.Pokemon(p.PokemonAPI(), id=id)
            height = pokemon.height
            list_of_heights.append({'id':id, 'height':height})
        return list_of_heights  
    
    def format_stats(self, list_of_pokemon_ids):
        list_of_stats = []
        for id in list_of_pokemon_ids:
            pokemon = p.Pokemon(p.PokemonAPI(), id=id)
            stats = pokemon.get_stats
            stats.append({'id':id})
            list_of_stats.append(stats)
        return list_of_stats
    
    def format_moves(self, list_of_pokemon_ids):
        list_of_moves = []
        for id in list_of_pokemon_ids:
            pokemon = p.Pokemon(p.PokemonAPI(), id=id)
            moves = pokemon.get_moves
            moves.append({'id':id})
            list_of_moves.append(moves)            
        return list_of_moves
    
    def format_abilities(self, list_of_pokemon_ids):
        list_of_abilities = []
        for id in list_of_pokemon_ids:
            pokemon = p.Pokemon(p.PokemonAPI(), id=id)
            abilities = pokemon.get_abilities
            abilities['id'] = id
            list_of_abilities.append(abilities)            
        return list_of_abilities
    
    def format_games(self, list_of_pokemon_ids):
        list_of_games = []
        for id in list_of_pokemon_ids:
            pokemon = p.Pokemon(p.PokemonAPI(), id=id)
            games = pokemon.get_games
            games['id'] = id
            list_of_games.append(games)            
        return list_of_games

df = Dataset(p.PokemonAPI(), 3)
print(df.format_games(df.list_of_pokemon_ids))