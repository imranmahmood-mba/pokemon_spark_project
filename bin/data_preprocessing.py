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
        # self.dataset = self.create_dataframe()
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
    

    
#     def take_comma_separated_values_column_and_create_row_for_each_value(self, column_name: str):
#         filtered_data = self.dataset[column_name]
#         value_list = []
        
#         for value in filtered_data:
#             split_values = str(value).split(', ')  # Split the values by comma
#             value_list.extend(split_values)   # Extend the list with the split values

#         return list(set(value_list))
    
#     @staticmethod
#     def add_id_to_a_column(list_of_values: list, id_col_name='id', value_col_name='value'):
#         return [{id_col_name: idx + 1, value_col_name: value} for idx, value in enumerate(list_of_values)]
    
#     @property
#     def get_dataset(self):
#         return self.dataset
# df = Dataset(p.PokemonAPI())


# def encode_column(df: pd.DataFrame, column_name: str):
#     # Use factorize to encode the unique values
#     encoded_values, unique_values = pd.factorize(df[column_name])

#     # Increment the encoded values by 1
#     encoded_values += 1

#     # Update the specified column in the DataFrame with the encoded values
#     df[column_name] = encoded_values

# def create_content_dimension(df: pd.DataFrame):
#     # Create a function to separate duration into seasons and minutes
#     def separate_duration(value):
#         if "Season" in str(value):
#             return str(value).split(' ')[0], None
#         elif "min" in str(value):
#             return None, str(value).split(' ')[0]
#         else:
#             return None, None

#     # Apply the separate_duration function to the duration column
#     df['seasons'], df['minutes'] = zip(*df['duration'].apply(separate_duration))

#     # Drop the original duration column
#     df.drop('duration', axis=1, inplace=True)

#     # Create a new column for content_id
#     df['content_id'] = range(1, len(df) + 1)

# def split_and_assign_id(df: pd.DataFrame, names_col: str, id_col_name='id', movie_col=None):
#     # Splitting the names column into multiple rows
#     s = df[names_col].str.split(', ').apply(pd.Series, 1).stack()
#     s.index = s.index.droplevel(-1)
#     s.name = names_col
#     df_split = df.drop(names_col, axis=1).join(s).reset_index(drop=True)

#     # Sorting the unique names (excluding NaN)
#     unique_names = sorted([name for name in df_split[names_col].unique() if isinstance(name, str)])
    
#     # Creating a mapping from unique values (including NaN) to IDs
#     name_to_id = {name: idx + 1 for idx, name in enumerate(unique_names)}
#     name_to_id[np.nan] = len(unique_names) + 1

#     # Applying the mapping to the 'name' column
#     df_split[id_col_name] = df_split[names_col].map(name_to_id)

#     if movie_col:
#         df_split[movie_col] = df_split[movie_col]

#     return df_split
