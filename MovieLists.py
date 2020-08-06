import os
import Encryption
import auth
import io

def ReadFromFile(fileName, encrypted):
        Movie_files = open(fileName, "r")

        horror_movies = Movie_files.readlines()

        if encrypted == True:
                for i in range(0, len(horror_movies)):
                        horror_movies[i] = Encryption.decrypt_text(horror_movies[i], auth.SEED)

        Movie_files.close()
        return horror_movies


def WriteToFile(filename, moviename):
        with io.open(filename, "a", encoding="utf-8") as f:

                #moviename = Encryption.encrypt_text(moviename, auth.SEED)

                if os.path.getsize(filename) == 0:
                        f.write(moviename)
                else:
                        f.write("\n" + moviename)

                f.close()


def check_if_file_contains(path, title):
        read_file = open(path, "r")
        for line in read_file:
                if line.lower() == title.lower():
                        return True
        return False

def delete_from_file(path, title):
        title = Encryption.encrypt_text(title, auth.SEED)
        content = ReadFromFile(path)
        for i in range(0, len(content)):
                if content[i] == title:
                        del content[i]
                        break
        writer = open(path, "w")
        for movie in content:
                writer.write(movie)
        writer.close()