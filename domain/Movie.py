from domain.IDobject import *
from domain.ValidatorException import *

class Movie(IDobject):

    def __init__ (self, movieID, title, desc, genere):
        IDobject.__init__(self, movieID)

        self._title = title
        self._desc = desc
        self._genere = genere

    def getTitle (self):
        return self._title;

    def getDescription (self):
        return self._desc

    def getGenere (self):
        return self._genere



    def __str__ (self):
        return "Movie [ " + "Title: " + self._title + ", Genere: " + self._genere + ", Description: " + self._desc + ", ID: " + str(self.getID()) + " ]"

    def __eq__ (self, c):
        if isinstance (c, Movie) == False:
            return False
        return self._objID == c._objID

    def __repr__ (self):
        return str(self)


class MovieValidator:

    def __init__ (self):
        self._errors = ""

    def validate (self, movie):
        """
        Used to validate a movie, if the provided date isinstance is valid
        Returns a list of validation errors.
        """

        if isinstance (movie, Movie) == False:
            raise TypeError("Can only validate Movie objects!")
        self._errors = []

        if len (movie.getTitle()) == 0:
            self._errors.append("Movie must have a name!")

        if len (movie.getGenere()) == 0:
            self._errors.append("Movie must have a name!")

        if len(self._errors) > 0:
            raise ValidatorException(_errors)
        return True
