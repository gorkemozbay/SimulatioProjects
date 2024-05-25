
from configs            import *

def round_up_screen_size(screen_size):
    remainder = screen_size % CELL_SIZE
    if remainder == 0:
        return screen_size
    else:
        return screen_size - remainder 