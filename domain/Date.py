from domain.ValidatorException import *

class Date:

    def __init__ (self, day, month, year):
        self._day = day
        self._month = month
        self._year = year

    def getDay (self):
        return self._day
    def getMonth (self):
        return self._month
    def getYear (self):
        return self._year

    def __eq__ (self, c):
        if isinstance (c, Date) == False:
            return False
        return self

    def __str__ (self):
        return str(self._day) + "/" + str(self._month) + "/" + str(self._year)

    def greater(self, other):
        if self.getYear() > other.getYear():
            return True
        elif self.getYear() < other.getYear():
            return False
        else:
            if self.getMonth() > other.getMonth():
                return True
            elif self.getMonth() < other.getMonth():
                return False
            else:
                if self.getDay() > other.getDay():
                    return True
                elif self.getDay() < other.getDay():
                    return False
        return True



class DateValidator:

    def __init__ (self):
        self._errors = ""

    def validate (self, date):
        """
        Used to validate a date, if the provided date isinstance is valid
        Returns a list of validation errors.
        """

        if isinstance (date, Date) == False:
            raise TypeError("Can only validate Date objects!")
        self._errors = []
        if isinstance (date.getDay(), int) == False:
            self._errors.append("Invalid day type!")
        if isinstance (date.getMonth(), int) == False:
            self._errors.append("Invalid month type!")
        if isinstance (date.getYear(), int) == False:
            self._errors.append("Invalid year type!")
        if date.getYear() < 1900 and date.getYear() > 2016:
            self._errors.append("The year must be betwen [1900, 2016]! ")

        if len(self._errors) > 0:
            raise ValidatorException(_errors)
        return True
