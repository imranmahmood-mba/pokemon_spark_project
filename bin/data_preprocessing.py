import pokemon as p

# instantiate pokemon object to interact with api
pokemon = p.PokemonAPI()

def fact_table(pokemon_object:p.PokemonAPI):
    pokemon_list=[]
    for i in range(1, 1015):
        previous_evolution_id = p.Pokemon(pokemon_object, id=i).get_previous_evolution_id

        pokemon_list.append({'previous_evolution':previous_evolution_id})

