import requests
import image_lib 
import os 

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'
 
def main():
    # Test out the get_pokemon_into() function
    # Use breakpoints to view returned dictionary
    #poke_info = str(poke_info).strip().lower
    poke_info = get_pokemon_info("Rockruff")
    poke_info = get_pokemon_info(123)
    return
 
def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.
 
    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)
 
    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # Clean the Pokemon name parameter by:
    # - Converting to a string object, 
    # - Removing leading and trailing whitespace, and
    # - Converting to all lowercase letters
    pokemon_name = str(pokemon_name).strip().lower()
 
    # Build the clean URL for the GET request
    url = POKE_API_URL + pokemon_name
 
    # Send GET request for Pokemon info
    print(f'Getting information for {pokemon_name}...', end='')
    resp_msg = requests.get(url)
 
    # Check if request was successful
    if resp_msg.status_code == requests.codes.ok:
        print('success')
        # Return dictionary of Pokemon info
        return resp_msg.json()
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')         
        return


def get_pokename_name(offset=0, limit=100000):
    query_str_params = {
        'offset' :offset,
        'limit' :limit
        
    }
    print(f' Getting Pokemon Names...', end='')
    resp_message = requests.get(POKE_API_URL, params=query_str_params)
    if resp_message.status_code == requests.codes.ok:
        pokemon_dict = resp_message.json() 
        
        pokemon_name_list = [p['name'] for p in pokemon_dict['results']]
        return pokemon_name_list
    else:
        print('failure')
        print (f' Response Code: {resp_message.status_code, {resp_message.reason}}')
        return 
    
    def download_pokemon_artwork(pokemoon_name, save_dir):
        pokemon_info = get_pokemon_info(pokemon_info) 
        if pokemon_info in None: 
            return 
        artwork_url = pokemon_info['spirits']['other']['offical-artwork']['front_default'] 
    
    def image_lib_download_image(artwork_url):
        if image_bytes is None:
            return 
    image_path = os.path.join(save_dir, f'{pokemon_name}. {file_ext}')
    image_lib.save_image_file(image_bytes, image_path)
    
if __name__ == '__main__':
    main()
