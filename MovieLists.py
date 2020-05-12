
def ReadFromFile(fileName):
        Movie_files = open(fileName, "r")

        horror_movies = []
        for i in Movie_files:
            horror_movies.append(i)

        Movie_files.close()
        return horror_movies

def WriteToFile(fileName, movieName):
        writeFile = open(fileName, "a")
        writeFile.write("\n" + movieName)
        writeFile.close()