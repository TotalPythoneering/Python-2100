# MISSION: The complete set of examples and source code for ''Python 2100: Objects,
# Factories & Frameworks''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2100
# DATE: 2026-09-24 05:47:41
# FILE: Person.py
# AUTHOR: Randall Nagy
#
from MyFramework.AbsThing import Thing

class Person(Thing):

    @classmethod
    def Create(recipe, order=None):
        return recipe()
    
    def create(self):
        return True

    def read(self):
        return True

    def update(self):
        return True

    def delete(self):
        return True


