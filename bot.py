# bot.py

import discord
import random
import MovieLists
import auth
import os.path
import IDcollector
from os import path
#Static variables required throughout the programs
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

#Everytime a message is sent this event is ran
@client.event
async def on_message(message):
    #If the message is sent by this bot or does not begin with an exclamation mark then don't analyze it
    if message.author == client.user:
        return

    #Here we break down the message into its various parts
    parts = message.content.split()

    filename = parts[0]
    filename = filename[0:]
    command = parts[0].lower()
    if command[0] != "!":
        return
    #Checks if the user is looking for a movie of a specific genre
    for genre in genres:
        if command == "!" + genre:
            #If the user is looking for a movie from that genre we read from that genres file and take 3 random movies from it
            movieList = MovieLists.ReadFromFile("GenreLists/" + genre + "Titles.txt")
            randomNum = random.randint(0, len(movieList) - 1)
            #Loops 3 times
            for i in range(1, 4):
                #Picks a random choice from the movielist we read in above
                movieTitle = random.choice(movieList)
                #Creates the message that will later be sent
                await message.channel.send(set_up_message(movieTitle))
            return
    #This is our help command
    if command == "!help":
        #Simply prints out the information required for the user to use the program
        await  message.channel.send("Here are my commands:")
        await  message.channel.send("!(genre) - Picks a random movie from a given genre. Genres are sci-fi, animation, action, comedy, adventure, fantasy, thriller, horror, mystery and drama\n" +
                                    "!add (movie title) - Adds a movie to your list\n" +
                                    "!remove (movie title) - Removes a movie from your list\n" +
                                    "!myList - picks movie from your list\n" +
                                    "!recommended - recommends a movie based off the movies in your list")
    #This command gets a random movie from the person sending the messages list
    elif command == "!mylist":
        #Here we set up the path from which to read from
        file_path = "PersonalLists/" + str(message.author) + "list.txt"
        if path.exists(file_path):
            mylist = MovieLists.ReadFromFile(file_path)
            randomNum = random.randint(0, len(mylist) - 1)
            movieTitle = mylist[randomNum]
            await message.channel.send(set_up_message(movieTitle))
        else:
            await message.channel.send("You have nothing in your list")
    #Our commmand to add movies to your personal list
    elif command == "!add":
        new_movie = ""
        #Creating the movie title by adding the various parts together
        for i in range(1, len(parts)):
            if i < len(parts) - 1:
                new_movie += parts[i] + " "
            else:
                new_movie += parts[i]
        #Here we check to make sure that the movie actually exists in our database
        if IDcollector.getID(new_movie) != "N/A":
            MovieLists.WriteToFile("PersonalLists/" + str(message.author) + "list.txt", new_movie)
            await message.channel.send(new_movie + " added to your list.")
        else:
            await  message.channel.send("Please enter a valid movie.")
    #Recommends movies command using the TMDB API
    elif command == "!recommended":
        #Checks if the person has movies on their list first
        if path.exists("PersonalLists/" + str(message.author) + "list.txt"):
            user_list = MovieLists.ReadFromFile("PersonalLists/" + str(message.author) + "list.txt")
            base_movie = random.choice(user_list)
            recommended_title = IDcollector.get_recommended(base_movie)
            await message.channel.send(set_up_message(recommended_title))
        else:
            await message.channel.send("Add something to your list first with the !add command!")
    #Remove command
    elif command == "!remove":
        #Checks that the person has a list first
        if path.exists("PersonalLists/" + str(message.author) + "list.txt"):
            return;
        movie_remove = ""
        #Adds the parts that are supposed to be the movie title
        for i in range(1, len(parts)):
            if i < len(parts) - 1:
                movie_remove += parts[i] + " "
            else:
                movie_remove += parts[i]
        #Checks if the persons list contains the movie and deletes it if it does
        if MovieLists.check_if_file_contains("PersonalLists/" + str(message.author) + "list.txt", movie_remove + "\n"):
            MovieLists.delete_from_file("PersonalLists/" + str(message.author) + "list.txt", movie_remove + "\n")
            await message.channel.send("Removed " + movie_remove + " from your list.")
        else:
            await  message.channel.send("Your list is empty or does not contain that movie.")
    #If none of the commands are used tell the user the command was not recognized
    else:
        await message.channel.send("Command not recognized, use !help for a list of commands")


#method used to set up the the message with a given movie title
def set_up_message(movie_title):
    bot_message = ":clapper:**" + movie_title + "**" + "\n**Director**: " + IDcollector.getDirector(
        movie_title) + "\n" + "**IMDB Rating**: " + IDcollector.getIMDBRating(movie_title) + "\n" \
                  + ":thought_balloon:**Description**: " + IDcollector.getPlot(movie_title) + "\n"
    if IDcollector.getID(movie_title) != "N/A":
        bot_message += IMDB_URL_START + IDcollector.getID(movie_title) + IMDB_URL_END + "\n"
    return bot_message


client.run(auth.TOKEN)
