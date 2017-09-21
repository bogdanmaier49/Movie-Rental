from repository.RepositoryException import *
from domain.IDobject import*

class Repository:

    def __init__(self):
        self._objects = []

    def exists (self, objectID):
        for obj in self._objects:
            if objectID == obj.getID():
                return True
        return False

    def get (self, objectID):
        for obj in self._objects:
            if obj.getID() == objectID:
                return obj
        return None

    def add (self, object):

        if self.exists(object.getID()) == False:
            self._objects.append(object)
        else:
            raise RepositoryException("Object with id:" + str(object.getID()) + " allready exists")


    def remove (self, object):
        obj = self.get(object.getID())
        if obj == None:
            raise RepositoryException("Object with id:" + str(obj.getID()) + " not in repository!")
        self._objects.remove(obj)

    def update (self, objectID, newObject):
        '''
            Updates the object with id = objectID with the new given object
        '''
        for index in range(0, len(self._objects)):
            if self._objects[index].getID() == objectID:
                self._objects[index] = newObject
                return True
        return False

    def getAll (self):
        return self._objects

    def __len__(self):
        return len(self._objects)

    def __str__(self):
        r = "Repository:\n"
        for e in self._objects:
            r += str(e)
            r += "\n"
        return r
