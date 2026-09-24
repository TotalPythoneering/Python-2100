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
        if hasattr(cls, "Create") is False:
            return Controller.Create(Baker, "(Woof - Make Baker!)")           
        obj = cls.Create(order)
        if obj is None:
            return Controller.Create(Baker, "(Defaulting to Baker!)")
        print("Factory: Creating", order)
        return obj

class Dum:
    pass

classes = {"absAble":absAble, "Baker":Baker, "Charley":Charley, "Crazy":Dum}

for key in sorted(classes):
    zClass = classes[key]
    obj = Controller.Create(zClass, key)
    if issubclass(zClass, absAble) is False:
        print('-' * 5, "Avoidance")
        continue
    if isinstance(obj, zClass) is False:
        print("Error")
    else:
        print("Testing Success")
    obj.say_hello()
    print('*' * len(key))

