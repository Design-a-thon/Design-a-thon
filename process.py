# Import modules

import pandas as pd
import numpy as np
import random
import re
import json
from datetime import datetime, UTC
from zoneinfo import ZoneInfo

url = "https://docs.google.com/spreadsheets/d/1jMsdB4HaBWjWi500dIrSt2CM8DEQkd6ApevQRR9FbZU/export?format=csv&gid=2011480512"
df = pd.read_csv(url)

event_df = df[df["What do you wish to submit a tracking for?"] == "Event Participation"]
transaction_df = df[df["What do you wish to submit a tracking for?"] == "Shop Transaction"]
daily_df = df[df["What do you wish to submit a tracking for?"] == "Daily Challenge Participation"]

#Usernames
with open("data/signups.txt", "r") as file:
    lines = file.read().splitlines()
    usernames = [user for user in lines if user != ""]

START_TICKETS = 10
ticket_balance = {}

for user in usernames:
    ticket_balance[user] = START_TICKETS

cleaned_transactions = []
bad_usernames = []

def normalize_username(name: str) -> str:
    #Account for additional space at end of username
    name = name.strip()
    if name[0] == '@':
        name = name[1:]
    return re.sub(r"[-_]+", "_", name.lower())

def tally(row, event):
    name = row['What is your Scratch Username? (without the @)']

    #Account for wrong capitalization
    if (name not in usernames):
        for user in usernames:
            if (normalize_username(name) == normalize_username(user)):
                name = user

    #Print out bad usernames
    if (name not in usernames):
        if event == "Event":
            bad_usernames.append(name)
            print(name)
        return
    
    if event == "Event":
        ticket_balance[name] += 15
    elif event == "Daily":
        ticket_balance[name] += 5

def transact(row):
    seller = row['What is your Scratch Username? (without the @)']
    buyer = row["What is the username of the buyer? (without the @)"]
    amt = int(row["What is the ticket amount of the transaction?"])

    seller = seller.strip()
    buyer = buyer.strip()

    #Account for wrong capitalization
    if (buyer not in usernames):
        for user in usernames:
            normalized_buyer = normalize_username(buyer)
            normalized_user = normalize_username(user)
            if (normalized_buyer.lower() == normalized_user.lower()):
                buyer = user
    

    if (seller not in usernames):
        for user in usernames:
            normalized_seller = normalize_username(seller)
            normalized_user = normalize_username(user)
            if (normalized_seller.lower() == normalized_user.lower()):
                seller = user

    #Print out bad usernames
    if (buyer not in usernames):
        print(buyer)
        bad_usernames.append(buyer)
        return
    
    if (seller not in usernames):
        print(seller)
        bad_usernames.append(seller)
        return


    ticket_balance[seller] += amt
    ticket_balance[buyer] -= amt


event_df.apply(lambda row: tally(row, "Event"), axis=1)
daily_df.apply(lambda row: tally(row, "Daily"), axis=1)
transaction_df.apply(transact, axis=1)

final = []
for user in ticket_balance:
    line = f'@{user}: {ticket_balance[user]}'
    final.append(line)

# Add last updated timestamp
time = datetime.now(ZoneInfo("America/Los_Angeles"))
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")
    
with open('data/ticket_balance.txt', 'w') as f:
    f.write(f'Last Updated: {formatted_time}\n\n')
    for line in final:
        f.write(line)
        f.write('\n')

with open('data/bad_usernames.txt', 'w') as f:
    f.write(f'Last Updated: {formatted_time}\n\n')
    for line in bad_usernames:
        f.write(line)
        f.write('\n')

output = {
    "last_updated": time.isoformat(),
    "ticket_balance": {
        f"@{user}": balance
        for user, balance in ticket_balance.items()
    }
}

with open("data/ticket_balance.json", "w") as f:
    json.dump(output, f, indent=2)

print(ticket_balance)
