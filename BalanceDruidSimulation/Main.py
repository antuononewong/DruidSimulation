'''
This is a quantitative approach to creating a unit.  This module will test the damage output
within a certain time frame based on the class, Balance Druid, within the game World of Warcraft.
There's various classes and specializations (i.e Subtlety Rogue, Fury Warrior, Beast Mastery Hunter) within the game, 
and we can figure out how strong each one is by simulating an optimal use of abilities.  This method can also be used
to create and tune different units as the strength/numbers of abilities can be easily adjusted.
'''
from collections import namedtuple

#--------------GLOBALS FOR ABILITIES/BASE GAMEPLAY NUMBERS-----------------
SPELL = namedtuple("SPELL", "damage castTime cost astralPowerGain")

STARSURGE = SPELL(2000, 0, 40, 0) 
SOLAR_WRATH = SPELL
LUNAR_STRIKE = SPELL
MOONFIRE = SPELL
SUNFIRE = SPELL
ASTRAL_POWER = 40 # 100 Astral Power cap
SOLAR_EMPOWERMENTS = 0
LUNAR_EMPOWERMENTS = 0
SOLAR_EMPOWERMENT_CHANCE = 13
LUNAR_EMPOWERMENT_CHANCE = 8

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
    global DAMAGE_DONE, TIMER, ASTRAL_POWER
    
    if (spell == STARSURGE):
        ASTRAL_POWER -= 40
        DAMAGE_DONE += STARSURGE.damage
        TIMER += GCD + STARSURGE.castTime
    
    elif (spell == SOLAR_WRATH):
        return 
    
    elif (spell == LUNAR_STRIKE):
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
    
    while (TIMER < time):
        
        if (ASTRAL_POWER >= 40):
            cast(STARSURGE)
            
        elif (SOLAR_EMPOWERMENTS > 0):
            cast(SOLAR_WRATH)
            
        elif (LUNAR_EMPOWERMENTS > 0):
            cast(LUNAR_STRIKE)
            
        else:
            cast(SOLAR_WRATH)
        break
    
    print(str(DAMAGE_DONE) + " damage done over " + str(time) + " seconds - DPS = " + "{:0.2f}".format(DAMAGE_DONE/time))
            
    

if __name__ == '__main__':
    run(300)