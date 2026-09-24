# MISSION: The complete set of examples and source code for ''Python 2100: Objects,
# Factories & Frameworks''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2100
# DATE: 2026-09-24 05:47:41
# FILE: 04_controller.py
# AUTHOR: Randall Nagy
# Basic controller class
#
from MyFramework.Person import Person as zThing

class ThingCtrlr01:
    @staticmethod
    def Create():
        return zThing()
    
    @classmethod
    def Create(cls, myOrder):
        print(str(cls))
        return zThing()

var = ThingCtrlr01.Create("Fries & Soda")

if var.create() is True:
    print("Testing Success")




    








    


