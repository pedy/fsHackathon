import discord
import json
from difflib import SequenceMatcher

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

    result = return_most_similar(message.content.upper())
    await client.send_message(message.channel, result)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)

