# MISSION: The complete set of examples and source code for ''Python 2100: Objects,
# Factories & Frameworks''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2100
# DATE: 2026-09-24 05:47:41
# FILE: Controller.py
# AUTHOR: Randall Nagy
# "Abstract Class" / Python Framework Testing ...
#
from AbsAble import absAble
from Baker import Baker
from Charley import Charley

class Controller():

    @staticmethod
    def Create(cls, order):
        print("Factory: Creating", order)
        return cls.Create(order)


classes = {"Baker":Baker, "Charley":Charley}

for key in classes:
    zClass = classes[key]
    obj = Controller.Create(zClass, key)
    if isinstance(obj, zClass) is False:
        print("Error")
    else:
        print("Testing Success")
    obj.say_hello()
    print('*' * len(key))

