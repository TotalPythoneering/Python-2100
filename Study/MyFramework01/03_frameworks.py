# MISSION: The complete set of examples and source code for ''Python 2100: Objects,
# Factories & Frameworks''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2100
# DATE: 2026-09-24 05:47:41
# FILE: 03_frameworks.py
# AUTHOR: Randall Nagy
#

from MyFramework.AbsThing import Thing
from MyFramework.Person import Person

var = Person()

zTest = var.create()

if zTest is True:
    print("Testing Success!")
elif zTest is False:
    print("Testing Failure")
else:
    print("Testing Problem")






    


