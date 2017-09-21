from repository.Repository import *
from domain.Client import *
from domain.Movie import *
from domain.Rental import *
from controller.MovieController import *



class UI:

    def __init__ (self, movieController, rentalController, clientController):
        self._movieController = movieController
        self._rentalController = rentalController
        self._clientController = clientController


    def toInt (self, value):
        try:
            return int(value)
        except TypeError:
            print ("Failed to convert expresion to int")

    def readDate (self, msg):
        string = input(msg)
        string.replace(" ", "")
        splitString = string.split("/")

        if not len(splitString) == 3:
            return None

        day = self.toInt(splitString[0])
        month = self.toInt(splitString[1])
        year = self.toInt(splitString[2])

        if day == False:
            print("Day must be a number")
            return None
        if day < 1 or day > 31:
            print("Day must be betwen 1 and 31")
            return

        if month == False:
            print("Month must be a number")
            return None
        if month < 1 or month > 12:
            print("Month must be betwen 1 and 12")
            return

        if year == False:
            print("Year must be a number")
            return None
        if year < 1900 or year > 2016:
            print("Year must be betwen 1900 and 2016")
            return

        date = Date(int(splitString[0]),int(splitString[0]),int(splitString[0]))
        return date

    def addMovieMenu (self):
        print ("========================== Add a movie =========================")
        ID = input("Movie ID: ")
        if self.movieController.exists(ID):
            print ("Movie ID " + ID + " allready exists")
            return None
        title = input("Movie title: ")
        desc = input("Movie description: ")
        genere = input("Movie genere: ")

        self._movieController.create(ID, title, desc, genere)

    def addClientMenu (self):
        print ("========================== Add a client ========================")
        ID = input("Client ID:")
        if self._clientController.exists(ID):
            print ("Client ID " + ID + " allready exists")
            return None
        name = input("Client name: ")

        self._clientController.create(ID, name)

    def readRental (self):
        ID = input("Rental ID:")
        if self._rentalController.exists(ID):
            print ("Rental ID " + ID + " allready exists")
            return None
        movieID = input("Movie ID: ")
        if self._movieController.exists(movieID) == False:
            print ("Movie id: " + movieID + " not found!")
            return None
        clientID = input("Client ID: ")
        if self._rentalController.clientCanRent(clientID) == False:
            print ("Cleint " + cleintID + " cant rent any movie")
            return None
        if self._clientController.exists(clientID) == False:
            print ("Client id: " + clientID + " not found!")
            return None
        rentedDate = self.readDate("Rented date(zi/luna/an): ")
        dueDate = self.readDate("Due date(zi/luna/an): ")

        return Rental(ID, movieID, clientID, rentedDate, dueDate)

    def addRentalMenu (self):
        print ("========================== Add a rental ========================")
        rental = self.readRental()
        if rental == None:
            print ("Invalid rental object")
        else:
            self._rentalController.create(rental)


    def updateRentalMenu (self):
        print ("======================== Update Rental =========================")
        id = input ("Update rental ID: ")
        if self._rentalController.exists(id):
            rental = self.readRental()
            if rental == None:
                print ("Invalid rental object")
            else:
                self._rentalController.update(id, rental)
        else:
            print("rental with id: "  + id + " does not exits.")

    def removeClientMenu (self):
        print ("======================  Remove Client ==========================")
        ID = input ("Client ID: ")
        self._clientController.remove( self._clientController.getByID(ID) )
        #removes the rentals that contains the clientID
        client = self._rentalController.getByClientID(ID)
        if client == None:
            return
        self._rentalController.remove( client )

    def removeMovieMenu (self):
        print ("======================  Remove Movie ==========================")
        ID = input ("Movie ID: ")
        self._movieController.remove( self._movieController.getByID(ID) )
        #removes the rentals that contains the movieID
        movie = self._rentalController.getByMovieID(ID)
        if movie == None:
            return
        self._rentalController.remove( movie )

    def removeRentalMenu (self):
        print ("======================  Remove Rental ==========================")
        ID = input ("Rental ID: ")
        self._rentalController.remove( self._rentalController.getByID(ID) )

    def returnMovieMenu (self):
        print ("====================== Return Movie ============================")
        ID = input ("Rental ID: ")
        date = self.readDate("Returned Date: ")
        self._rentalController.returnMovie(ID, date)


    def searchMovie (self):
        print("===================== Search Movie ==============================")
        key = input ("Search: ")
        result = self._movieController.search(key)
        if len(result) == 0:
            print ("No movie found!")
            return

        for r in result:
            print (r)

    def printMainMenu (self):
        print ("========================== Dandy Movies ========================")
        print ("\t 1C - Add a client")
        print ("\t 2C - Remove a client")
        print ("________________________________________________________________")
        print ("\t 1M - Add a movie")
        print ("\t 2M - Remove a movie")
        print ("________________________________________________________________")
        print ("\t 1R - Add a rental")
        print ("\t 2R - Remove a rental")
        print ("\t 3R - Update a rental")
        print ("\t 4R - Return a movie")
        print ("________________________________________________________________")
        print ("\t 1S - Seach Cleint")
        print ("\t 2S - Search Movie")
        print ("________________________________________________________________")
        print ("\t 0 - Exit")
        print ("================================================================")



    def mainMenu (self):
        self.printMainMenu()

        while True:
            command = input("Please enter the command: ")

            if command == "1C" :
                self.addClientMenu()
            elif command == "2C" :
                self.removeClientMenu()
            elif command == "1M" :
                self.addMovieMenu()
            elif command == "2M":
                self.removeMovieMenu()
            elif command == "1R" :
                self.addRentalMenu()
            elif command == "2R" :
                self.removeRentalMenu()
            elif command == "print":
                print(str(self._clientController.getRepository()))
                print(str(self._movieController.getRepository()))
                print(str(self._rentalController.getRepository()))
            elif command == "0":
                break
            elif command == "3R":
                self.updateRentalMenu()
            elif command == "4R":
                self.returnMovieMenu()
            elif command == "2S":
                self.searchMovie()
            else:
                print("Unknown command!")
