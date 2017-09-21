from repository.Repository import *
from domain.Rental import *

class RentalController():

    def __init__ (self, repository, validator):
        self._repository = repository
        self._validator = validator

    def create (self, ID, movieID, clientID, rentedDate, dueDate):
        '''
            Adds a new rental to the repository
        '''
        rental = Rental(ID, movieID, clientID, rentedDate, dueDate)
        self._validator.validate(rental)
        self._repository.add(rental)

    def create (self, rental):
        if self.clientCanRent(rental.getClientID()):
            self._validator.validate(rental)
            self._repository.add(rental)

    def returnMovie (self, rentalID, returnedDate):
        rentals = self._repository.getAll()
        for rental in rentals:
            if rental.getID() == rentalID:
                rental.setReturnedDate(returnedDate)

    def remove (self, rental):
        '''
            Removes a rental from the repository
        '''
        self._repository.remove(rental)

    def exists (self, rentalID):
        return self._repository.exists(rentalID)

    def update (self, objectID, newObject):
        self._repository.update(objectID, newObject)

    def clientCanRent (self, clientID):
        rentals = self._repository.getAll()
        ok = True
        for rental in rentals:
            if rental.getClientID() == clientID:
                if ( not rental.getReturnedDate() == None ) and rental.getReturnedDate().greater(rental.getDueDate()) == False:
                    ok = False
        return ok

    def getRepository(self):
        return self._repository


    def getByID (self, rentalID):
        return self._repository.get(rentalID)

    def getByClientID (self, clientID):
        data = self._repository.getAll()
        for rental in data:
            if rental.getClientID() == clientID:
                return rental
        return None

    def getByMovieID (self, movieID):
        data = self._repository.getAll()
        for rental in data:
            if rental.getMovieID() == movieID:
                return rental
        return None
