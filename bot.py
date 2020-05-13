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
genres = ["sci-fi",
          "animation",
          "action",
          "comedy",
          "adventure",
          "fantasy",
          "thriller",
          "horror",
          "mystery",
          "drama"]

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

	content = message.content.toLowerCase()
    parts = content.split()
    #Checks if the user is looking for a movie of a specific genre
    for genre in genres:
        if parts[0] == "!" + genre:
            movieList = MovieLists.ReadFromFile("GenreLists/" + genre + "Titles.txt")
            randomNum = random.randint(0, len(movieList) - 1)
            await message.channel.send(movieList[randomNum])
            await message.channel.send(movieList[randomNum + 1])
            await message.channel.send(movieList[randomNum + 2])

    if(parts[0] == "!add"):
        try:
            print(parts[1] + "list.txt")

            newMovie = ""
            for i in range(2, len(parts)):
                if(i < len(parts) - 1):
                    newMovie += parts[i] + " "
                else:
                    newMovie += parts[i]
            MovieLists.WriteToFile("Jonathanlist.txt", newMovie)

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

client.run(auth.TOKEN)
