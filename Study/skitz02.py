# MISSION: The complete set of examples and source code for ''Python 2100: Objects,
# Factories & Frameworks''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2100
# DATE: 2018-03-07 15:30:00
# FILE: skitz02.py
# AUTHOR: Randall Nagy
#
class Skitz:

    def __init__(self, zName=None, zAge=None, zPhone=None):
        self.name=zName;self._age=zAge;self.phone=zPhone

    def set_age(self, age):
        if age < 0:
            raise ValueError("Error: Age is negative")
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, zAge):
        self.set_age(zAge)
    
var = Skitz()

