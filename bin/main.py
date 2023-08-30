import dimensional_model as dm
import data_preprocessing as dp
import create_database as db
import pokemon as p
import pandas as pd


def get_pokemon_fact_data():
    pokemon_data = dp.Dataset(p.PokemonAPI(), 3)
    weight = pokemon_data.format_weight(pokemon_data.list_of_pokemon_ids)
    height = pokemon_data.format_height(pokemon_data.list_of_pokemon_ids)
    types = pokemon_data.format_types(pokemon_data.list_of_pokemon_ids)
    stats = pokemon_data.format_stats(pokemon_data.list_of_pokemon_ids)
    abilities = pokemon_data.format_abilities(pokemon_data.list_of_pokemon_ids)
    games = pokemon_data.format_games(pokemon_data.list_of_pokemon_ids)
    moves = pokemon_data.format_moves(pokemon_data.list_of_pokemon_ids)
    name = pokemon_data.format_names(pokemon_data.list_of_pokemon_ids)
    evolutions = pokemon_data.format_previous_evolutions(pokemon_data.list_of_pokemon_ids)
    print(weight, height, types, stats, abilities, games, moves, name)

def game_dimension(number_of_pokemon:int):
    pokemon_data = dp.Dataset(p.PokemonAPI(), number_of_pokemon=number_of_pokemon)
    games = pokemon_data.format_games(pokemon_data.list_of_pokemon_ids)
    return games

def pokemon_dimension(number_of_pokemon:int):
    pokemon_data = dp.Dataset(p.PokemonAPI(), number_of_pokemon=number_of_pokemon)
    name = pokemon_data.format_names(pokemon_data.list_of_pokemon_ids)
    f_name = pokemon_data.flatten_names(name)
    evolutions = pokemon_data.format_previous_evolutions(pokemon_data.list_of_pokemon_ids)
    f_evolutions = pokemon_data.flatten_evolutions(pokemon_data.list_of_pokemon_ids, f_name)
    types = pokemon_data.format_types(pokemon_data.list_of_pokemon_ids)
    f_types = pokemon_data.format_types(pokemon_data.list_of_pokemon_ids, f_evolutions)
    print(f_types)





pokemon_dimension(3)