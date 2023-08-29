import dimensional_model as dm
import data_preprocessing as dp
import create_database as db
import pokemon as p
import pandas as pd


def get_pokemon_fact_data():
    pokemon_list = []
    for i in range(2, 3):
        pokemon = p.Pokemon(pokemon_api=p.PokemonAPI(), id=i)
        types = pokemon.get_types
        stats = pokemon.stats
        abilities = pokemon.get_abilities
        games = pokemon.get_games
        moves = pokemon.get_moves
        p_id = pokemon.id
        name = pokemon.name
        height = pokemon.height
        weight = pokemon.weight
        moves = pokemon.get_stats
        evolutions = pokemon.get_previous_evolution_idss
    pokemon_list.extend([evolutions, types, stats, abilities, 
                         games, moves, p_id, name, weight, height])
    return pokemon_list

