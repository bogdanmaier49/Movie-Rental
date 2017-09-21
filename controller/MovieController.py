from repository.Repository import *
from domain.Movie import *

class MovieController():

    def __init__ (self, repository, validator):
        self._repository = repository
        self._validator = validator

    def create (self, movieID, title, desc, genere):
        '''
            Adds a new movie to the repository
        '''
        movie = Movie(movieID, title, desc, genere)
        self._validator.validate(movie)
        self._repository.add(movie)

    def remove (self, movie):
        self._repository.remove(movie)

    def exists (self, movieID):
        return self._repository.exists(movieID)


    def getRepository(self):
        return self._repository

    def getByID (self, movieID):
        return self._repository.get(movieID)

    def search (self, key):
        result = []
        data = self._repository.getAll()

        key = key.replace(" ", "")
        key = key.lower()

        for movie in data:
            movieID =  movie.getID()
            movieID = movieID.replace(" ", "")
            movieID = movieID.lower()

            if movieID.find(key):
                result.append(movie)

        if len(result) == 0:
            for movie in data:
                movieTitle =  movie.getTitle()
                movieTitle = movieTitle.replace(" ", "")
                movieTitle = movieTitle.lower()

                if movieTitle.find(key):
                    result.append(movie)

        if len(result) == 0:
            for movie in data:
                movieDesc =  movie.getDescription()
                movieDesc = movieDesc.replace(" ", "")
                movieDesc = movieDesc.lower()

                if movieDesc.find(key):
                    result.append(movie)

        if len(result) == 0:
            for movie in data:
                movieGenere =  movie.getGenere()
                movieGenere = movieGenere.replace(" ", "")
                movieGenere = movieGenere.lower()

                if movieGenere.find(key):
                    result.append(movie)

        return result
