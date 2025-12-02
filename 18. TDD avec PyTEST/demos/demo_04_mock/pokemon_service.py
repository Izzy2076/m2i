import requests

class PokemonService:
    def __init__(self):
        self.url_base = "https://pokeapi.co/api/v2/"

    def obtenir_pokemon(self, nom_ou_id):
        # https://pokeapi.co/api/v2//pokemon/5
        url = f"{self.url_base}pokemon/{nom_ou_id}"

        response = requests.get(url)

        if response.status_code != 200:
            raise ValueError(f"Erreur API : {response.status_code}")
        
        data = response.json()

        # print(data)

        return {
            "nom" : data.get("name"),
            "poids" : data.get("weight"),
            "taille" : data.get("height")
        }
    
pokemonService = PokemonService()

print(pokemonService.obtenir_pokemon("5"))