# MISSION: The complete set of examples and source code for ''Python 2100: Objects,
# Factories & Frameworks''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2100
# DATE: 2026-09-24 05:47:41
# FILE: attribute_testing.py
# AUTHOR: Randall Nagy
# demonstrate attribute management
#

class Eggs:
    def __init__(self):
        self.spam = None

    def say_hi(self):
        pass

    @classmethod
    def say_hiC(cls):
        pass

    @staticmethod
    def say_hiS(self):
        pass
    
names = ("spam", "say_hi", "say_hiC", "say_hiS", "noneya")
obj = Eggs()
for name in names:
    if hasattr(obj, name):
        print("Found", name)


    
