import requests

base_url = "https://pokeapi.co/api/v2/"

def pookeamon_search(name):
    url = f"{base_url}pokemon/{name}"
    respo = requests.get(url)

    if respo.status_code == 200:
        data = respo.json()
        return data
    else:
        print("❌ Pokemon not Found")
        return None

pokemon_name = input("Enter your Pokemon name: ")
pokemon_info = pookeamon_search(pokemon_name)



if pokemon_info:
    print(f"\n🧬 Name      : {pokemon_info['name'].capitalize()}")
    print(f"🆔 ID        : {pokemon_info['id']}")
    print(f"📏 Height    : {pokemon_info['height'] / 10} m")
    print(f"⚖️ Weight    : {pokemon_info['weight'] / 10} kg")
