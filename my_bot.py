# Work with Python 3.6
import discord
import json

TOKEN = 'NTQwNzczMzIwNzI0MDU0MDI0.DzWB7A.EUTm3Ok7tGafxa_2eLbZXKv0arM'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    
    with open('sampleRates.json') as json_data:
        d = json.load(json_data)
        #print("Valid Currency Symbols:", d['validCurrencySymbols'])
        #command = input("Please use symbols pairs like this: AUDUSD, USDAUD\n")
        #print("Your input:", command)

        try:
            result = d['exchangeRates'][message.content]
            await client.send_message(message.channel, result)
        except:
            error_msg = "Valid currency codes: " + str(d['validCurrencySymbols'])
            await client.send_message(message.channel, error_msg)

    #if message.content.startswith('!hello'):
        #msg = 'Hello {0.author.mention}'.format(message)
        #await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)