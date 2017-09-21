class IDobject():

    """
    Base class for all objects having unique id within the application
    """

    def __init__ (self, id):
        """
        Constructor method for building IDObject
        objectId - the unique objectId of the object in the application
        """
        self._objID = id

    def getID (self):
        """
        Returns the id of the curent object.
        """
        return self._objID
