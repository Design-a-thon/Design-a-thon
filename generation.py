import pandas as pd
import numpy as np
import random
import json

def load_data(filename):
    with open(filename) as f:
        lines = f.readlines()
    loaded_list = []
    for line in lines:
        loaded_list.append(line.strip('\n'))
    return loaded_list

def write_data(filename, data):
    with open(filename, 'w') as f:
        for line in data:
            f.write(line + "\n")

usernames = load_data("data/signups.txt")

# Sweet Shop
#desserts = load_data("data/prompt-generation/winter desserts.txt")
desserts = load_data("data/prompt-generation/summer desserts.txt")

# Sounds of Creativity
songs = load_data("data/prompt-generation/songs.txt")

# Beasts of Fantasy
plants = load_data("data/prompt-generation/plants.txt")
birds = load_data("data/prompt-generation/birds.txt")
mammals = load_data("data/prompt-generation/mammals.txt")

# Aesthetic Accessories
aesthetics = load_data("data/prompt-generation/aesthetics.txt")
accessories = load_data("data/prompt-generation/accessories.txt")

#Sweet Shop & Sounds of Creativity Prompt Generation

random.seed(42)

sweetshop = []  
sounds = []
beasts = []
aa = []

for user in usernames:
    d = random.choice(desserts)
    sweetshop.append(f'@{user} - {d}')
        
    s = random.choice(songs)
    sounds.append(f'""@{user} - "{s}""')

    b1 = random.choice(plants)
    b2 = random.choice(mammals)
    beasts.append(f'@{user} - "{b1}" + "{b2}"')

    aes = random.choice(aesthetics)
    acc = random.choice(accessories)
    aa.append(f'@{user} - "{aes}" + "{acc}"')

write_data('data/prompts/sweetshop.txt', sweetshop)
write_data('data/prompts/sounds.txt', sounds)
write_data('data/prompts/beasts.txt', beasts)
write_data('data/prompts/aesthetic-accessories.txt', aa)

output = {
    "Sweet Shop": {
        f"@{user}": prompt for user, prompt in zip(usernames, sweetshop)
    },
    "Sounds of Creativity": {
        f"@{user}": prompt for user, prompt in zip(usernames, sounds)
    },
    "Beasts of Fantasy": {
        f"@{user}": prompt for user, prompt in zip(usernames, beasts)
    },
    "Aesthetic Accessories": {
        f"@{user}": prompt for user, prompt in zip(usernames, aa)
    }
}

with open("data/prompts/prompts.json", "w") as f:
    json.dump(output, f, indent=2)