import pandas as pd
import numpy as np
import random
import json
from PIL import Image, ImageDraw, ImageFont

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

# Word Prompts

random.seed(42)

sweetshop = []  
sounds = []
beasts = []
aa = []

for user in usernames:
    d = random.choice(desserts)
    sweetshop.append(f'@{user} - {d}')
        
    s = random.choice(songs)
    sounds.append(f'@{user} - "{s}"')

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



# Combination Domination

adj1 = load_data("data/prompt-generation/adj1.txt")
adj2 = load_data("data/prompt-generation/adj2.txt")
adj3 = load_data("data/prompt-generation/adj3.txt")

cd = []

for user in usernames:
    rand_adj1 = random.choice(adj1)
    rand_adj2 = random.choice(adj2)
    rand_adj3 = random.choice(adj3)
    string = f'@{user} - ("{rand_adj1}", "{rand_adj2}" & "{rand_adj3}")'
    cd.append(string)

write_data('data/prompts/cd.txt', cd)

IMAGE_SIZE = (960,720)
BG_COLOR = (0,0,0,0)
BLACK = (0, 0, 0, 255)

RECT_TOP_LEFT_1 = (90, 175)
RECT_BOTTOM_RIGHT_1 = (870, 260)


RECT_TOP_LEFT_2 = (90, 335)
RECT_BOTTOM_RIGHT_2 = (870, 420)

RECT_TOP_LEFT_3 = (90, 490)
RECT_BOTTOM_RIGHT_3 = (870, 580)

RECT_COORDS_1 = (RECT_TOP_LEFT_1, RECT_BOTTOM_RIGHT_1)

RECT_COORDS_2 = (RECT_TOP_LEFT_2, RECT_BOTTOM_RIGHT_2)

RECT_COORDS_3 = (RECT_TOP_LEFT_3, RECT_BOTTOM_RIGHT_3)

RECT_COLOR = BLACK


my_image = Image.new(mode = 'RGBA', size = IMAGE_SIZE, color = BG_COLOR)
image_drawer = ImageDraw.Draw(my_image)

image_drawer.rectangle(RECT_COORDS_1, RECT_COLOR)
image_drawer.rectangle(RECT_COORDS_2, RECT_COLOR)
image_drawer.rectangle(RECT_COORDS_3, RECT_COLOR)

mf = ImageFont.truetype("assets/fonts/ARIAL.TTF", 40)
#mf = ImageFont.truetype('arial.ttf', 40)
count = 0

#print(len(usernames))

for i in range(1,(len(usernames))//3*3,3):
    count += 1
    new_image = Image.new(mode = 'RGBA', size = IMAGE_SIZE, color = BG_COLOR)
    image_drawer = ImageDraw.Draw(new_image)
    image_drawer.rectangle(RECT_COORDS_1, RECT_COLOR)
    image_drawer.rectangle(RECT_COORDS_2, RECT_COLOR)
    image_drawer.rectangle(RECT_COORDS_3, RECT_COLOR)

    palette1 = Image.open(f'data/prompt-generation/palette_files/{random.randint(1,200)}.png')
    palette2 = Image.open(f'data/prompt-generation/palette_files/{random.randint(1,200)}.png')
    palette3 = Image.open(f'data/prompt-generation/palette_files/{random.randint(1,200)}.png')
    #palette3 = Image.open(f'palettes/{random.randint(1,25)}.png')

    new_image.paste(palette1, (105, 190))
    new_image.paste(palette2, (105, 350))
    new_image.paste(palette3, (105, 510))
    
    user1 = "@" + usernames[i-1]
    user2 = "@" + usernames[i]
    user3 = "@" + usernames[i+1]

    image_drawer.text((180, 120), f'{user1}', font = mf, fill= BLACK)
    image_drawer.text((180, 280), f'{user2}', font = mf, fill = BLACK)
    image_drawer.text((180, 440), f'{user3}', font = mf, fill= BLACK)

    new_image.save(f"data/prompts/cd-palettes/{count}.png")
    #print(count)

if (len(usernames)%3) == 1:
    user1 = "@" + usernames[-1]
    count += 1
    new_image = Image.new(mode = 'RGBA', size = IMAGE_SIZE, color = BG_COLOR)
    image_drawer = ImageDraw.Draw(new_image)
    image_drawer.rectangle(RECT_COORDS_1, RECT_COLOR)

    palette1 = Image.open(f'data/prompt-generation/palette_files/{random.randint(1,25)}.png')
    new_image.paste(palette1, (105, 190))
    image_drawer.text((180, 120), f'{user1}', font = mf, fill= BLACK)
    new_image.save(f"data/prompts/cd-palettes/{count}.png")

elif (len(usernames)%3) == 2:
    count += 1
    user1 = "@" + usernames[-2]
    user2 = "@" + usernames[-1]

    new_image = Image.new(mode = 'RGBA', size = IMAGE_SIZE, color = BG_COLOR)
    image_drawer = ImageDraw.Draw(new_image)
    image_drawer.rectangle(RECT_COORDS_1, RECT_COLOR)
    image_drawer.rectangle(RECT_COORDS_2, RECT_COLOR)

    palette1 = Image.open(f'data/prompt-generation/palette_files/{random.randint(1,25)}.png')
    palette2 = Image.open(f'data/prompt-generation/palette_files/{random.randint(1,25)}.png')
    new_image.paste(palette1, (105, 190))
    new_image.paste(palette2, (105, 350))
    image_drawer.text((180, 120), f'{user1}', font = mf, fill= BLACK)
    image_drawer.text((180, 280), f'{user2}', font = mf, fill = BLACK)
    new_image.save(f"data/prompts/cd-palettes/{count}.png")

#username = "@Lemon24K"
#image_drawer.text((180, 120), username, font = mf, fill= BLACK)

#print(count)
