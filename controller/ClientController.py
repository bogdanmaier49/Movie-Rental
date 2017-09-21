from repository.Repository import *
from domain.Client import *

class ClientController():

    def __init__ (self, repository, validator):
        self._repository = repository
        self._validator = validator

    def getByID (self, clientID):
        return self._repository.get(clientID)

    def create (self, clientID, name):
        '''
            Adds a new client to the repository
        '''
        client = Client(clientID, name)
        self._validator.validate(client)
        self._repository.add(client)

    def remove (self, client):
        self._repository.remove(client)

    def exists (self, clientID):
        return self._repository.exists(clientID)

    def getRepository(self):
        return self._repository

    def search (self, key):
        data = self._repository.getAll()
        for client in data:
            

        return None
