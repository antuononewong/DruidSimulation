'''
This is a quantitative approach to creating a unit.  This module will test the damage output
within a certain time frame based on the class, Balance Druid, within the game World of Warcraft.
There's various classes and specializations (i.e Subtlety Rogue, Fury Warrior, Beast Mastery Hunter) within the game, 
and we can figure out how strong each one is by simulating an optimal use of abilities.  This method can also be used
to create and tune different units as the strength/numbers of abilities can be easily adjusted.
'''
from collections import namedtuple

#--------------GLOBALS FOR ABILITIES/BASE GAMEPLAY NUMBERS-----------------
SPELL = namedtuple()

STARSURGE = 0
SOLAR_WRATH = 0
LUNAR_STRIKE = 0
MOONFIRE = 0
SUNFIRE = 0
ASTRAL_POWER = 0
SOLAR_EMPOWERMENTS = 0
LUNAR_EMPOWERMENTS = 0
SOLAR_EMPOWERMENT_CHANCE = 0
LUNAR_EMPOWERMENT_CHANCE = 0

GCD = 1 # Global Cooldown of 1 second - time delay after using an ability
DAMAGE_DONE = 0
TIMER = 0
#----------------------------------------------------

# Optimal Rotation:
#    1. Maintain Moonfire and Sunfire as they are DOT's (damage over time), so very time efficient damage
#    2. Use Starsurge if you have >40 AP (heavy hitting resource spell)
#    3. Use Solar Wrath if you have Solar Empowerments (empowerments buff the spells)
#    4. Use Lunar Strike if you have Lunar Empowerments
#    5. Use Solar Wrath if all above are false

# Takes in a global spell, then adds overall time used and damage done to our totals
def cast (spell : namedtuple):
    return

# If we cast Lunar Strike, we have a chance to generate Solar Empowerments. This uses
# a randomization scheme to get more Solar Empowerments from casts.
def getSolarEmpowerments():
    return 

# If we cast Solar Wrath, we have a chance to generate Lunar Empowerments. This uses
# a randomization scheme to get more Lunar Empowerments from casts.
def getLunarEmpowerments():
    return 

# Checks if we have any Solar Empowerments stored. If so, uses then and adds the 
# adjusted values of time and damage done to our totals rather than baseline ones.
def checkSolarEmpowerments():
    return 

# Checks if we have any Lunar Empowerments stored. If so, uses them and adds the
# adjusted values of time and damage done to our totals rather than baseline ones.
def checkLunarEmpowerments():
    return

# Base function that will handle the rotation described above based on the inputted timer
def run (time : int): 
    return

if __name__ == '__main__':
    run(300)