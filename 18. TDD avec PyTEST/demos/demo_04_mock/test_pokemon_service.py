import pytest
from unittest.mock import Mock, patch
from pokemon_service import PokemonService

@pytest.fixture
def service():
    return PokemonService()

def test_obtenir_pokemon_success(service):
    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "name" : "charmeleon",
            "weight": 190,
            "height": 11
        }

        mock_get.return_value = mock_response

        pokemon = service.obtenir_pokemon("5")


        assert pokemon["nom"] == "charmeleon"
        assert pokemon["poids"] == 190
        assert pokemon["taille"] == 11
        mock_get.assert_called_once_with("https://pokeapi.co/api/v2/pokemon/5")
