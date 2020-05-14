import os

def ReadFromFile(fileName):
        Movie_files = open(fileName, "r")

        horror_movies = []
        for i in Movie_files:
            horror_movies.append(i)

        Movie_files.close()
        return horror_movies


def WriteToFile(filename, moviename):
        writefile = open(filename, "a")
        if os.path.getsize(filename) == 0:
                writefile.write(moviename)
        else:
                writefile.write("\n" + moviename)
        writefile.close()