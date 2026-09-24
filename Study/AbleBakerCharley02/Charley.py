# MISSION: The complete set of examples and source code for ''Python 2100: Objects,
# Factories & Frameworks''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2100
# DATE: 2026-09-24 05:47:41
# FILE: Charley.py
# AUTHOR: Randall Nagy
# "Abstract Class" / Python Framework Testing ...
#
from AbsAble import absAble

class Charley(absAble):

    @classmethod
    def Create(cls, order):
        print("Charley: Creating", order)
        return cls()

    def say_hello(self):
        print("Greetings from Charley!")
        return True

