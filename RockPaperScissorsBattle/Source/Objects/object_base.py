
import pygame
from configs import *


class ObjectBase:
    
    def __init__(self, x, y, speed_x, speed_y):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.img     = None
        self.object_type = None
    
    
    def update(self):
        if self.x <= 0 or self.x + OBJ_SIZE >= MAP_WIDTH:
            self.speed_x *= -1
        
        if self.y <= OFF_SET_POS or self.y + OBJ_SIZE >= MAP_HEIGHT:
            self.speed_y *= -1
            
        self.x += self.speed_x
        self.y += self.speed_y


    def render(self, screen):
        screen.blit(self.img, (self.x, self.y))
        
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, OBJ_SIZE, OBJ_SIZE)
         