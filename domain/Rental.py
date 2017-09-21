from domain.IDobject import *
from domain.Date import *
from domain.ValidatorException import *

class Rental (IDobject):

    def __init__ (self, ID, movieID, clientID, rentedDate, dueDate):
        IDobject.__init__(self, ID)

        self._movieID = movieID
        self._clientID = clientID
        self._rentedDate = rentedDate
        self._dueDate = dueDate
        self._returnedDate = None

    def getMovieID (self):
        return self._movieID

    def getClientID (self):
        return self._clientID

    def getRendetDate (self):
        return self._rentedDate

    def getDueDate (self):
        return self._dueDate

    def getReturnedDate (self):
        return self._returnedDate

    def setDueDate (self, newDate):
        self._rentedDate = newDate

    def setReturnedDate (self, newDate):
        self._returnedDate = newDate


    def __eq__ (self, c):
        if isinstance (c, Rental) == False:
            return False
        return self._objID == c._objID

    def __str__ (self):
        return "Rental [ Movie ID: " + str(self._movieID) + ", Client ID: " + str(self._clientID) + ", Rented Date: " + str(self._rentedDate) + ", Due Date: " + str(self._dueDate) + ", Returned Date: " + str(self._returnedDate) + ", Rental ID: " + str(self._objID) + " ]"

    def __repr__ (slef):
        return str(self)






class RentalValidator():

    def __init__ (self):
        self._errors = ""

    def validate (self, rental):
        """
        Used to validate a rental, if the provided date instance is invalid
        Returns a list of validation errors.
        """

        if isinstance(rental, Rental) == False:
            raise TypeError("Can only validate Rental objects")

        self._errors = []

        if len (rental.getID()) == 0:
            self._errors.append("Invalid rental ID")

        if len (rental.getMovieID()) == 0:
            self._errors.append("Invalid movie ID")

        if len (rental.getClientID()) == 0:
            self._errors.append("Invalid client ID")

        dateValidator = DateValidator()
        self._errors.append(dateValidator.validate(rental._rentedDate))


        return self._errors
