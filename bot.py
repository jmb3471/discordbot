# bot.py

import discord
import random
import MovieLists
import auth
import os.path
from os import path
API_KEY = "bb22565a"
URL = "http://www.omdbapi.com/?apikey=" + API_KEY + "&"
IMDB_URL_START = "https://www.imdb.com/title/"
IMDB_URL_END = "/?ref_=hm_fanfav_tt_1_pd_fp1"
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

    content = message.content.lower()
    parts = content.split()
    filename = parts[0]
    filename = filename[1:]
    if (path.exists(filename)):
        mylist = MovieLists.ReadFromFile(filename)
        randomNum = random.randint(0, len(mylist) - 1)
        await message.channel.send(mylist[randomNum])

    #Checks if the user is looking for a movie of a specific genre
    for genre in genres:
        if parts[0] == "!" + genre:
            movieList = MovieLists.ReadFromFile("GenreLists/" + genre + "Titles.txt")
            randomNum = random.randint(0, len(movieList) - 1)
            await message.channel.send(movieList[randomNum])
            await message.channel.send(movieList[randomNum + 1])
            await message.channel.send(movieList[randomNum + 2])
    if parts[0] == "!help":
        await  message.channel.send("Here are my commands:")
        await  message.channel.send("!genre - Picks a random movie from a given genre. Genres include sci-fi, animation, action, comedy, adventure, fantasy, thriller, horror, mystery and drama")
        await  message.channel.send("!add (movie title) - Adds a movie to the given list")
        await  message.channel.send("!create (list name) - Creates a list with the given name")
        await  message.channel.send("!(list name) - picks movie if the given list exist")

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
            await message.channel.send("Create your own personal list first")

    elif(parts[0] == "!create"):
        writeFile = open(str(parts[1]) + "list.txt", "w")
        writeFile.close()
        print("Done")


client.run(auth.TOKEN)
