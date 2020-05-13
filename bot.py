# bot.py
import os

import discord
import random
import MovieLists
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
    parts = message.content.split()
    if(parts[0] == "!horror"):
        horrorMovies = MovieLists.ReadFromFile("MovieLists/horrorTitles.txt")
        randomNum = random.randint(0, len(horrorMovies))
        await message.channel.send(horrorMovies[randomNum])
        await message.channel.send(horrorMovies[randomNum + 1])
        await message.channel.send(horrorMovies[randomNum + 2])
    if(parts[0] == "!add"):
        newMovie = ""
        for i in range(1, len(parts)):
            if(i < len(parts) - 1):
                newMovie += parts[i] + " "
            else:
                newMovie += parts[i]
        MovieLists.WriteToFile("horrormovies.txt", newMovie)

client.run(auth.TOKEN)
