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
    pokemon_api = p.PokemonAPI()
    dataset = dp.Dataset(pokemon_api=pokemon_api, number_of_pokemon=number_of_pokemon)
    name = dataset.pokemon_formatter.format_names(dataset.list_of_pokemon_ids)
    evolutions = dataset.pokemon_formatter.format_previous_evolutions(dataset.list_of_pokemon_ids)
    types = dataset.pokemon_formatter.format_types(dataset.list_of_pokemon_ids)
    field_list = [name, evolutions, types]
    return dp.Dataset.create_table(field_list)


f = pokemon_dimension(3)
print(f)