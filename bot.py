# bot.py
import os

import discord
import random
import auth

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
    horror_movies = [
        "silence of the lambs",
        "the shining",
        "psycho",
        "hereditary",
        "the conjuring",
        "paranormal activity",
        "Alien",
        "The Thing",
        "The Exorcist",
        "Rosemary's Baby",
        "The Lighthouse",
        "Saw"
    ]
    if(message.content == "!horror"):
        return random.choice(horror_movies)


client.run(auth.TOKEN)