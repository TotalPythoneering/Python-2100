# MISSION: The complete set of examples and source code for ''Python 2100: Objects,
# Factories & Frameworks''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2100
# DATE: 2026-09-24 05:47:41
# FILE: 01_Inheritance.py
# AUTHOR: Randall Nagy
# Basic inheritance concepts ...
#

class Able:

    def say_hello(self):
        print("Hello - from Able")


class Baker(Able):

    def say_hello(self):
        print("Greetings from Baker!")


var = Baker()

var.say_hello()
