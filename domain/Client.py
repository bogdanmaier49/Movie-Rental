from domain.IDobject import *
from domain.ValidatorException import *

class Client(IDobject):

    def __init__ (self, clientID, name):
        IDobject.__init__(self, clientID)
        self._name = name

    def getName(self):
        return self._name

    def setName(slef, newName):
        self._name = newName

    def __str__ (self):
        return "Client [ ID: " + str(self.getID()) + ", Name: " + self._name + " ]"


    def __eq__ (self, c):
        if isinstance(c, Client) == False:
            return False
        return self._objID == c._objID

    def __repr__ (self):
        return str(self)

class ClientValidator:

    def __init__ (self):
        self._errors = ""

    def validate (self, client):
        """
        Used to validate a client, if the provided date isinstance is valid
        Returns a list of validation errors.
        """

        if isinstance (client, Client) == False:
            raise TypeError("Can only validate Client objects!")
        self._errors = []

        if len (client.getName()) == 0:
            self._errors.append("Client must have a name!")

        if len(self._errors) > 0:
            raise ValidatorException(_errors)
        return True
