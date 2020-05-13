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
    try:
        filename = parts[0]
        filename = filename[1:]
        mylist = MovieLists.ReadFromFile(filename)
        randomNum = random.randint(0, len(mylist) - 1)
        await message.channel.send(mylist[randomNum])


    except IOError:
        if(parts[0] == "!horror"):
            horrorMovies = MovieLists.ReadFromFile("GenreLists/horrorTitles.txt")
            randomNum = random.randint(0, len(horrorMovies) - 1)
            await message.channel.send(horrorMovies[randomNum])
            await message.channel.send(horrorMovies[randomNum + 1])
            await message.channel.send(horrorMovies[randomNum + 2])
        elif(parts[0] == "!add"):
            try:
                print(parts[1] + "list.txt")

                newMovie = ""
                for i in range(2, len(parts)):
                    if(i < len(parts) - 1):
                        newMovie += parts[i] + " "
                    else:
                        newMovie += parts[i]
                MovieLists.WriteToFile(parts[1] + "list.txt", newMovie)

            except IOError:
                await message.channel.send("List doesn't exist")

        elif(parts[0] == "!create"):
            writeFile = open(str(parts[1]) + "list.txt", "w")
            writeFile.close()

        elif(parts[0] == "!pick"):
            writeFile = open(str(parts[1]) + "list.txt", "w")
            writeFile.write("\n" + parts[2])
            writeFile.close()



client.run(auth.TOKEN)
