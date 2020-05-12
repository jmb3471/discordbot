# bot.py
import os

import discord
from dotenv import load_dotenv
import random
load_dotenv()
TOKEN = "Njk5NzcwNTIyODUzOTY1ODc0.XrogXg.RWYV6eAHDDfhwnHEwkeJa1rFNzg"
SERVER = "Sam's Simp Army"

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, fuck you'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    andrew_quotes = [
        'I\'m gay',

        'Im sick as fuck bro!',
    ]

    violet_quotes = [
        'uwu I wuv krish',
        (
            'You are a king'
        ),
    ]

    jacob_quotes = [
        'Thats the thing',
        'The thing is',
    ]


    dhaval_quotes = [
        'STFU Dhaval',
        'No one cares Dhaval',
    ]
    if message.content == '!Andrew':
        response = random.choice(andrew_quotes)
        await message.channel.send(response)

    elif message.content == '!Violet':
        response = random.choice(violet_quotes)
        await message.channel.send(response)

    elif message.content == '!Jacob':
        response = random.choice(jacob_quotes)
        await message.channel.send(response)

    elif message.content == '!Dhaval':
        response = random.choice(dhaval_quotes)
        await message.channel.send(response)

client.run(TOKEN)