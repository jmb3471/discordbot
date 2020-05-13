# bot.py
import os

import discord
import random
import MovieLists
import auth
import os.path
from os import path

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
    horrorMovies = MovieLists.ReadFromFile("horrorTitles.txt")
    if(parts[0] == "!horror"):
        horrorMovies = MovieLists.ReadFromFile("MovieLists/horrorTitles.txt")
        randomNum = random.randint(0, len(horrorMovies))
        await message.channel.send(horrorMovies[randomNum])
        await message.channel.send(horrorMovies[randomNum + 1])
        await message.channel.send(horrorMovies[randomNum + 2])
    elif(parts[0] == "!add"):
        try:
            writeFile = open(str(parts[1]) + "list.txt")
            writeFile.write("\n" + parts[2])
            writeFile.close()

            newMovie = ""
            for i in range(2, len(parts)):
                if(i < len(parts) - 1):
                    newMovie += parts[i] + " "
                else:
                    newMovie += parts[i]
            MovieLists.WriteToFile(str(parts[1]) + "list.txt", newMovie)
        except IOError:
            await message.channel.send("List doesn't exist")

    elif(parts[0] == "!create"):
        writeFile = open(str(parts[1]) + "list.txt", "w")
        writeFile.close()
        print("Done")

    elif(parts[0] == "!addto"):
        writeFile = open(str(parts[1]) + "list.txt", "w")
        writeFile.write("\n" + parts[2])
        writeFile.close()

>>>>>>> cf3945938c9bcdf0241e384a8b4ff6a9b7a2b11c

client.run(auth.TOKEN)
