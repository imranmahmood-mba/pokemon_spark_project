import dimensional_model as dm
import data_preprocessing as dp
import create_database as db
import pokemon as p
import pandas as pd


def get_pokemon_fact_data(number_of_pokemon:int):
    pokemon_api = p.PokemonAPI()
    dataset = dp.Dataset(pokemon_api=pokemon_api, number_of_pokemon=number_of_pokemon)    
    weight = dataset.pokemon_formatter.format_weight(datasets.list_of_pokemon_ids)
    height = dataset.pokemon_formatter.format_height(dataset.list_of_pokemon_ids)
    types = dataset.pokemon_formatter.format_types(dataset.list_of_pokemon_ids)
    stats = dataset.pokemon_formatter.format_stats(dataset.list_of_pokemon_ids)
    abilities = dataset.pokemon_formatter.format_abilities(dataset.list_of_pokemon_ids)
    games = dataset.pokemon_formatter.format_games(dataset.list_of_pokemon_ids)
    moves = dataset.pokemon_formatter.format_moves(dataset.list_of_pokemon_ids)
    name = dataset.pokemon_formatter.format_names(dataset.list_of_pokemon_ids)
    evolutions = dataset.pokemon_formatter.format_previous_evolutions(dataset.list_of_pokemon_ids)
    print(weight, height, types, stats, abilities, games, moves, name)

def game_dimension(number_of_pokemon:int):
    pokemon_api = p.PokemonAPI()
    dataset = dp.Dataset(pokemon_api=pokemon_api, number_of_pokemon=number_of_pokemon)
    games = dataset.pokemon_formatter.format_games(dataset.list_of_pokemon_ids)
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