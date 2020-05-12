# bot.py
import os

import discord
import random

SERVER = "Sam's Simp Army"
TOKEN = "Njk5NzcwNTIyODUzOTY1ODc0.Xror2w.7csaUoGgxtAU0xVFcR7M9qXd1gI"
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
    horror_movies = [
        "silence of the lambs",
        "the shining",
        "psycho",
        "hereditary",
        "the conjuring",
        "paranormal activity",
        ""
    ]
    if(message.content == "!search horror")
        return random.choice(horror_movies)
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

client.run()