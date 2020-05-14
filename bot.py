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

    parts = message.content.split()
    filename = parts[0]
    filename = filename[0:]
    command = parts[0].lower()
    if command[0] == '!':
        #Checks if the user is looking for a movie of a specific genre
        for genre in genres:
            if command == "!" + genre:
                movieList = MovieLists.ReadFromFile("GenreLists/" + genre + "Titles.txt")
                randomNum = random.randint(0, len(movieList) - 1)
                for i in range(1, 4):
                    movieTitle = random.choice(movieList)
                    bot_message = ":clapper:**" + movieTitle + "**" + "\n**Director**: " + IDcollector.getDirector(movieTitle) + "\n" + "**IMDB Rating**: " + IDcollector.getIMDBRating(movieTitle) + "\n" \
                                + ":thought_balloon:**Description**: " + IDcollector.getPlot(movieTitle) + "\n"
                    if IDcollector.getID(movieTitle) != "N/A":
                        bot_message += IMDB_URL_START + IDcollector.getID(movieTitle) + IMDB_URL_END + "\n"
                    await message.channel.send(bot_message)
                return
        if command == "!help":
            await  message.channel.send("Here are my commands:")
            await  message.channel.send("!(genre) - Picks a random movie from a given genre. Genres are sci-fi, animation, action, comedy, adventure, fantasy, thriller, horror, mystery and drama")
            await  message.channel.send("!add (movie title) - Adds a movie to the given list")
            await  message.channel.send("!myList - picks movie from your list")

        elif command == "!mylist":
            file_path = "PersonalLists/" + str(message.author) + "list.txt"
            if path.exists(file_path):
                mylist = MovieLists.ReadFromFile(file_path)
                randomNum = random.randint(0, len(mylist) - 1)
                movieTitle = mylist[randomNum]
                bot_message = ":clapper:**" + movieTitle + "**" + "\n**Director**: " + IDcollector.getDirector(
                    movieTitle) + "\n" + "**IMDB Rating**: " + IDcollector.getIMDBRating(movieTitle) + "\n" \
                            + ":thought_balloon:**Description**: " + IDcollector.getPlot(movieTitle) + "\n"
                if IDcollector.getID(movieTitle) != "N/A":
                    bot_message += IMDB_URL_START + IDcollector.getID(movieTitle) + IMDB_URL_END + "\n"
                await message.channel.send(bot_message)
            else:
                await message.channel.send("You have nothing in your list")
        elif command == "!add":
            new_movie = ""
            for i in range(1, len(parts)):
                if i < len(parts) - 1:
                    new_movie += parts[i] + " "
                else:
                    new_movie += parts[i]
            MovieLists.WriteToFile("PersonalLists/" + str(message.author) + "list.txt", new_movie)
            await message.channel.send(new_movie + " added to your list.")
        elif command == "!recommended":
            if path.exists("PersonalLists/" + str(message.author) + "list.txt"):
                user_list = MovieLists.ReadFromFile("PersonalLists/" + str(message.author) + "list.txt")
                base_movie = random.choice(user_list)
                recommended_title = IDcollector.get_recommended(base_movie)
                bot_message = ":clapper:**" + recommended_title + "**" + "\n**Director**: " + IDcollector.getDirector(
                    recommended_title) + "\n" + "**IMDB Rating**: " + IDcollector.getIMDBRating(recommended_title) + "\n" \
                            + ":thought_balloon:**Description**: " + IDcollector.getPlot(recommended_title) + "\n"
                if IDcollector.getID(recommended_title) != "N/A":
                    bot_message += IMDB_URL_START + IDcollector.getID(recommended_title) + IMDB_URL_END + "\n"
                await message.channel.send(bot_message)
            else:
                await message.channel.send("Add something to your list first with the !add command!")

        else:
            await message.channel.send("Command not recognized, use !help for a list of commands")
client.run(auth.TOKEN)
