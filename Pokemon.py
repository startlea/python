import random
import requests
#
#
# Task 1 - Generate a random number between 1 and 151 to use as the Pokemon ID number
def choose_pokemon(amount = 1):
    pokemon_number = random.randint(1,151)
#3. Create a dictionary that contains the returned Pokemon's name, id, height and weight
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)  # API URL
    response = requests.get(url)  # getting information from the API
    pokemon = response.json()    #returns a JSON object of the result (if the result was written in JSON format, if not it raises an error
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'exp': pokemon['base_experience']
        }
    
#2. Using the Pokemon API get a Pokemon based on its ID number
my_pokemon = choose_pokemon(3)
#4. Get a random Pokemon for the player and another for their opponent
print('You get {} with ID number {}'.format(my_pokemon['name'], my_pokemon['id']))

stat_choice = input('Which stat of your pokemon do you want to use? (id, height, weight, exp) ')   ##5. Ask the user which stat they want to use (id, height or weight)
opponent_pokemon = choose_pokemon()

print('The opponent gets {} with ID number {}'.format(opponent_pokemon['name'], opponent_pokemon['id']))
my_stat = my_pokemon[stat_choice]
opponent_stat = opponent_pokemon[stat_choice]

print('Your pokemon has {} of {} your opponent pokemon has {}.'.format(my_pokemon[stat_choice], stat_choice, opponent_pokemon[stat_choice]))
      
#6. Compare the player's and opponent's Pokemon on the chosen stat to decide who wins
if my_stat > opponent_stat:
    print('You Win!')
elif my_stat < opponent_stat:
    print('You Lose!')
else:
    print('Draw!')
