'''
This is a quantitative approach to creating a unit.  This module will test the damage output
within a certain time frame based on the class, Balance Druid, within the game World of Warcraft.
There's various classes and specializations (i.e Subtlety Rogue, Fury Warrior, Beast Mastery Hunter) within the game, 
and we can figure out how strong each one is by simulating an optimal use of abilities.  This method can also be used
to create and tune different units as the strength/numbers of abilities can be easily adjusted.
'''
from collections import namedtuple
import random

#------------------SPELLS-------------------------
SPELL = namedtuple("SPELL", "damage castTime cost astralPowerGain")
SPELL_DOT = namedtuple("SPELL_DOT", "initialDamage tickDamage tickRate duration astralPowerGain")
STARSURGE = SPELL(2400, 0, 40, 0) 
SOLAR_WRATH = SPELL(800, 1.75, 0, 12)
LUNAR_STRIKE = SPELL(1100, 2.25, 0, 18)
MOONFIRE = SPELL_DOT(400, 180, 1, 24, 5)
SUNFIRE = SPELL_DOT(350, 210, 1, 18, 7)

#------------------EMPOWERMENTS-------------------
EMPOWERMENT = namedtuple("EMPOWERMENT", "damageBuffPercent castTimeReduction")
SOLAR_EMPOWERMENT = EMPOWERMENT(1.25, 0.8) # 25% dmg buff, 20% castTimeReduction
LUNAR_EMPOWERMENT = EMPOWERMENT(1.20, 0.6) # 20% dmg buff, 40% castTimeReduction
SOLAR_EMPOWERMENT_CHANCE = 13 # 13% chance to gain Solar Empowerment
LUNAR_EMPOWERMENT_CHANCE = 8 # 8% chance to gain Lunar Empowerment

#------------------CLASS RESOURCES-------------------------
ASTRAL_POWER = 40 # 100 Astral Power cap
SOLAR_EMPOWERMENT_COUNT = 0
LUNAR_EMPOWERMENT_COUNT = 0

#------------------BASE GAMEPLAY NUMBERS----------------------------
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
    global DAMAGE_DONE, TIMER, ASTRAL_POWER, SOLAR_EMPOWERMENT_COUNT, LUNAR_EMPOWERMENT_COUNT
    
    if (spell == STARSURGE):
        ASTRAL_POWER -= 40
        DAMAGE_DONE += STARSURGE.damage
        TIMER += GCD + STARSURGE.castTime
        SOLAR_EMPOWERMENT_COUNT += 1
        LUNAR_EMPOWERMENT_COUNT += 1
    
    elif (spell == SOLAR_WRATH):
        checkSolarEmpowerments()
        getLunarEmpowerments()
    
    elif (spell == LUNAR_STRIKE):
        checkLunarEmpowerments()
        getSolarEmpowerments()
        
    else:
        print("Error: Attempting to cast invalid spell.")
    
# If we cast Lunar Strike, we have a chance to generate Solar Empowerments. This uses
# a randomization scheme to get more Solar Empowerments from casts.
def getSolarEmpowerments():
    global SOLAR_EMPOWERMENT_COUNT
    chance = random.randint(1, 100)
    
    if (chance <= SOLAR_EMPOWERMENT_CHANCE):
        SOLAR_EMPOWERMENT_COUNT += 1 

# If we cast Solar Wrath, we have a chance to generate Lunar Empowerments. This uses
# a randomization scheme to get more Lunar Empowerments from casts.
def getLunarEmpowerments():
    global LUNAR_EMPOWERMENT_COUNT
    chance = random.randint(1, 100)
    
    if (chance <= LUNAR_EMPOWERMENT_CHANCE):
        LUNAR_EMPOWERMENT_COUNT += 1
        
# Checks if we have any Solar Empowerments stored. If so, uses then and adds the 
# adjusted values of time and damage done to our totals rather than baseline ones.
def checkSolarEmpowerments():
    global DAMAGE_DONE, TIMER, SOLAR_EMPOWERMENT_COUNT
    
    if (SOLAR_EMPOWERMENT_COUNT > 0):
        DAMAGE_DONE += (SOLAR_WRATH.damage * SOLAR_EMPOWERMENT.damageBuffPercent)
        TIMER += (SOLAR_WRATH.castTime * SOLAR_EMPOWERMENT.castTimeReduction) # castTime > GCD even with reduction, so ignore GCD
        SOLAR_EMPOWERMENT_COUNT -= 1
        
    else:
        DAMAGE_DONE += SOLAR_WRATH.damage
        TIMER += SOLAR_WRATH.castTime

# Checks if we have any Lunar Empowerments stored. If so, uses them and adds the
# adjusted values of time and damage done to our totals rather than baseline ones.
def checkLunarEmpowerments():
    global DAMAGE_DONE, TIMER, LUNAR_EMPOWERMENT_COUNT
    
    if (LUNAR_EMPOWERMENT_COUNT > 0):
        DAMAGE_DONE += (LUNAR_STRIKE.damage * LUNAR_EMPOWERMENT.damageBuffPercent)
        TIMER += (LUNAR_STRIKE.castTime * LUNAR_EMPOWERMENT.castTimeReduction) # castTIme > GCD always, so ignore GCD
        LUNAR_EMPOWERMENT_COUNT -= 1
        
    else:
        DAMAGE_DONE += LUNAR_STRIKE.damage
        TIMER += LUNAR_STRIKE.castTime

# Takes in the inputed runtime and calculates the DOT damage done over the course of the simulation.
# We're assuming a perfect rotation with 100% uptime on Moonfire and Sunfire.
def getDotDamage (time : int, dot : namedtuple):
    global DAMAGE_DONE, TIMER
     
    dotCasts = (time / dot.duration)
    dotTickDamage = (dot.tickDamage * time) # We lose 1 tick from initial cast
    dotInitialDamage = (dot.initialDamage * dotCasts)
    
    # Account for the extra astral power we gain from casting the dot - adjust timer accordingly
    astralPowerGained = (dot.astralPowerGain * dotCasts)
    starsurgeCasts = astralPowerGained / 40
    starsurgeDamage = (starsurgeCasts * STARSURGE.damage)
    
    TIMER += dotCasts + starsurgeCasts
    DAMAGE_DONE += dotTickDamage + dotInitialDamage + starsurgeDamage

# Base function that will handle the rotation described above based on the inputed timer
def run (time : int): 
    
    getDotDamage(time, MOONFIRE)
    getDotDamage(time, SUNFIRE)
    
    while (TIMER < time):
        
        if (ASTRAL_POWER >= 40):
            cast(STARSURGE)
            
        elif (SOLAR_EMPOWERMENT_COUNT > 0):
            cast(SOLAR_WRATH)
            
        elif (LUNAR_EMPOWERMENT_COUNT > 0):
            cast(LUNAR_STRIKE)
            
        else:
            cast(SOLAR_WRATH)
        
    
    # account for moonfire/sunfire damage with division of time
    # account for extra starsurge damage from gained Astral Power, add it onto the totals
    
    print(str(int(DAMAGE_DONE)) + " damage done over " + str(time) + " seconds - DPS = " + "{:0.2f}".format(DAMAGE_DONE/time))
            
    

if __name__ == '__main__':
    run(300)