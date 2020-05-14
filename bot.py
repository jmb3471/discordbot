# bot.py

import discord
import random
import MovieLists
import auth
import os.path
import IDcollector
from os import path
URL = "http://www.omdbapi.com/?apikey=" + auth.API_KEY + "&"
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
    filename = filename[0:]
    if parts[0] == "!myList":
        if path.exists(message.author + "list.txt"):
            mylist = MovieLists.ReadFromFile(filename)
            randomNum = random.randint(0, len(mylist) - 1)
            await message.channel.send(mylist[randomNum])
        else:
            await message.channel.send("You have nothing in your list")
    #Checks if the user is looking for a movie of a specific genre
    for genre in genres:
        if parts[0] == "!" + genre:
            movieList = MovieLists.ReadFromFile("GenreLists/" + genre + "Titles.txt")
            randomNum = random.randint(0, len(movieList) - 1)
            for i in range(1, 4):
                movieTitle = movieList[randomNum + i]
                await message.channel.send(":clapper:**" + movieTitle+ "**"  + "\n**Director**: " + IDcollector.getDirector(movieTitle) + "\n" + "**IMDB Rating**: " + IDcollector.getIMDBRating(movieTitle) + "\n"
                                           + ":thought_balloon:**Description**: " + IDcollector.getPlot(movieTitle) + "\n" + IMDB_URL_START + IDcollector.getID(movieTitle) + IMDB_URL_END + "\n")
    if parts[0] == "!help":
        await  message.channel.send("Here are my commands:")
        await  message.channel.send("!(genre) - Picks a random movie from a given genre. Genres include sci-fi, animation, action, comedy, adventure, fantasy, thriller, horror, mystery and drama")
        await  message.channel.send("!add (movie title) - Adds a movie to the given list")
        await  message.channel.send("!create (list name) - Creates a list with the given name")
        await  message.channel.send("!(list name) - picks movie from the given list")

    elif parts[0] == "!add":
        try:
            new_movie = ""
            for i in range(1, len(parts)):
                if i < len(parts):
                    new_movie += parts[i] + " "
                else:
                    new_movie += parts[i]
            MovieLists.WriteToFile(message.author + "list.txt", new_movie)
            await message.channel.send(new_movie + " added to your list.")

        except IOError:
            writefile = open("PersonalLists/" + message.author + "list.txt", "w")
            new_movie = ""
            for i in range(1, len(parts)):
                if i < len(parts):
                    new_movie += parts[i] + " "
                else:
                    new_movie += parts[i]
            MovieLists.WriteToFile(parts[1] + "list.txt", new_movie)
            writefile.close()
            await message.channel.send("Your list is created")

    else:
        await message.channel.send("Command not recognized, use !help for a list of commands")
client.run(auth.TOKEN)
