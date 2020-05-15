import os

def ReadFromFile(fileName):
        Movie_files = open(fileName, "r")

        horror_movies = Movie_files.readlines()

        Movie_files.close()
        return horror_movies


def WriteToFile(filename, moviename):
        writefile = open(filename, "a")
        if os.path.getsize(filename) == 0:
                writefile.write(moviename)
        else:
                writefile.write("\n" + moviename)
        writefile.close()


def check_if_file_contains(path, title):
        read_file = open(path, "r")
        for line in read_file:
                if line.lower() == title.lower():
                        return True
        return False

def delete_from_file(path, title):
        content = ReadFromFile(path)
        for i in range(0, len(content)):
                if content[i] == title:
                        del content[i]
                        break
        writer = open(path, "w")
        for movie in content:
                writer.write(movie)
        writer.close()