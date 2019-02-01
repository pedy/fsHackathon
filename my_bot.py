import discord
import json

TOKEN = 'NTQwNzczMzIwNzI0MDU0MDI0.DzWB7A.EUTm3Ok7tGafxa_2eLbZXKv0arM'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    
    with open('sampleRates.json') as json_data:
        d = json.load(json_data)

        try:
            result = d['exchangeRates'][message.content]
            await client.send_message(message.channel, result)
        except:
            error_msg = "Valid currency codes: " + str(d['validCurrencySymbols'])
                        + "Please use symbols pairs like this: AUDUSD, USDAUD, ...\n"
            await client.send_message(message.channel, error_msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)