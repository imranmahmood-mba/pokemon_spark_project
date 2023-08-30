import dimensional_model as dm
import data_preprocessing as dp
import create_database as db
import pokemon as p
import pandas as pd


def get_pokemon_fact_data():
    pokemon_data = dp.Dataset(p.PokemonAPI(), 3)
    weight = pokemon_data.format_weight(pokemon_data.list_of_pokemon_ids)
    height = pokemon_data.format_height(pokemon_data.list_of_pokemon_ids)

    # types = pokemon_data.
    # stats = pokemon.stats
    # abilities = pokemon.get_abilities
    # games = pokemon.get_games
    # moves = pokemon.get_moves
    # p_id = pokemon.id
    # name = pokemon.name
    # height = pokemon.height
    # moves = pokemon.get_stats
    # evolutions = pokemon.get_previous_evolution_ids
    
    # pokemon_list.extend([evolutions, types, stats, abilities, 
    #                      games, moves, p_id, name, weight, height])
    # return pokemon_list
    print(weight)
    print(height)

get_pokemon_fact_data()