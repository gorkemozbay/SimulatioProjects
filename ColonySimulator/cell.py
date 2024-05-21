
from datetime import datetime

class Cell():
    def __init__(self, x, y, is_alive = False, neighbor_count = 0, dead_time = None):
        self.x = x
        self.y = y
        self.is_alive = is_alive
        self.neighbor_count = neighbor_count
        self.dead_time = dead_time