import discord
import time
import json
from difflib import SequenceMatcher
import random

def return_most_similar(inputStr):
    with open('sampleRates.json') as json_data:
        d = json.load(json_data)

        pair_similarity_ratio = {}
        for key in d['exchangeRates']:
            pair_similarity_ratio[key] = SequenceMatcher(None, key, inputStr).ratio()
        
        most_similar = max(pair_similarity_ratio, key=pair_similarity_ratio.get)
        #print(pair_similarity_ratio)
        #print("most similar", most_similar)
        return most_similar

TOKEN = 'NTQwNzczMzIwNzI0MDU0MDI0.DzWB7A.EUTm3Ok7tGafxa_2eLbZXKv0arM'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() in ['hi', 'hello', 'hello!', 'hi!', 'start', 'begin', 'help' ]:
        with open('sampleRates.json') as json_data:
            d = json.load(json_data)
            welcome_msg = "Hi,\nThe valid currency symbols are:\n"\
                        + str(d['validCurrencySymbols'])\
                        + "\nPlease input a pair like \"AUD GBR\" (no quotation marks in your input) ..."
            await client.send_message(message.channel, welcome_msg)
            return

    closest = return_most_similar(message.content.upper())

    i = 5
    while i>0:
        if closest != message.content.upper():
            result = "\nThe most similar valid pair to your input is \""\
                    + closest + "\". The rate is: "
        else:
            result = message.content.upper() + " exchange rate is: "

        with open('sampleRates.json') as json_data:
            d = json.load(json_data)
            result += str(random.choice(d['exchangeRates'][closest])) # 'choice' randomly selects a value from the list
            await client.send_message(message.channel, result)
        time.sleep(1)
        i = i-1

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)

