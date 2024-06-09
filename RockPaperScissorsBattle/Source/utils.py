
from enum import Enum
from configs import *

BACKGROUND  = (40, 40, 40)
DARK_GREY   = (169, 169, 169)
WHITE       = (255, 255, 255)
BLACK       = (0, 0, 0)
RED         = (255, 0, 0)
GREEN       = (0, 255, 0)

class ObjectType(Enum):
    ROCK     = 1
    PAPER    = 2
    SCISSOR  = 3