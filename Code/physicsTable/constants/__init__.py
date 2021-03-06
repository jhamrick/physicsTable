# ---------------------------------------------------
# physicsTable
#
# Written by Kevin A Smith (k2smith@ucsd.edu)
#
# ---------------------------------------------------

import pygame as pg

__all__ = ['WHITE','BLACK','BLUE','RED','GREEN','GREY','LIGHTGREY','YELLOW','GOLD','PURPLE',
           'TIMESTEP','DEACT_TIME','KAPV_DEF','KAPB_DEF','KAPM_DEF','PERR_DEF',
           'LEFT','RIGHT','BOTTOM','TOP','HORIZONTAL','VERTICAL',
           'TIMEUP','SUCCESS','FAILURE','OUTOFBOUNDS','UNCERTAIN',
           'REDGOAL','GREENGOAL','BLUEGOAL','YELLOWGOAL',
           'COLLTYPE_DEFAULT','COLLTYPE_WALL','COLLTYPE_BALL','COLLTYPE_GOAL','COLLTYPE_PAD',
           'SHAPE_RECT','SHAPE_BALL','SHAPE_POLY','getConst','CENTER']

# Set color names
WHITE = pg.Color('White')
BLACK = pg.Color('Black')
BLUE = pg.Color('Blue')
RED = pg.Color('Red')
GREEN = pg.Color('Green')
GREY = pg.Color('Grey')
LIGHTGREY = pg.Color('lightgrey')
YELLOW = pg.Color('Yellow')
GOLD = pg.Color('Gold')
PURPLE = pg.Color('Purple')

# Lenght of timestep
TIMESTEP = 1/1000.

# Number of timesteps (1000th of a second) to deactivate walls to avoid multiple bouncing
DEACT_TIME = 50

# Default uncertainty parameters
KAPV_DEF = 86.373
KAPB_DEF = 21.545
KAPM_DEF = 212327.787
PERR_DEF = 10.814
    
def getConst(key):
    constants = dict([(1,'LEFT'), (3,'RIGHT'), (2,'BOTTOM'), (4,'TOP'), (5,'HORIZONTAL'), (6,'VERTICAL'),(7,'CENTER'),
                  (101,'TIMEUP'),(102,'SUCCESS'),(103,'FAILURE'),(104,'OUTOFBOUNDS'),(105,'UNCERTAIN'),
                  (201,'REDGOAL'),(202,'GREENGOAL'),(203,'BLUEGOAL'),(204,'YELLOWGOAL'),
                  (1000,'COLLTYPE_DEFAULT'),(1001,'COLLTYPE_WALL'),(1002,'COLLTYPE_BALL'),(1003,'COLTYPE_GOAL'),(1004,'COLLTYPE_PAD'),
                  (10,'SHAPE_RECT'),(11,'SHAPE_BALL'),(12,'SHAPE_POLY')])
    if key not in constants.keys(): print "Unknown constant type:", key; return None
    return constants[key]

# Global direction names
LEFT = 1
RIGHT = 3
BOTTOM = 2
TOP = 4
HORIZONTAL = 5
VERTICAL = 6
CENTER = 7

# Constants for return
TIMEUP = 101
SUCCESS = 102
FAILURE = 103
OUTOFBOUNDS = 104
UNCERTAIN = 105
REDGOAL = 201
GREENGOAL = 202
BLUEGOAL = 203
YELLOWGOAL = 204

# Collision constants for pymunk
COLLTYPE_DEFAULT = 1000
COLLTYPE_WALL = 1001
COLLTYPE_BALL = 1002
COLLTYPE_GOAL = 1003
COLLTYPE_PAD = 1004

# Constants for shape type
SHAPE_RECT = 10
SHAPE_BALL = 11
SHAPE_POLY = 12