
import pygame
import time
from   utils import *

class UI_manager():
    
    def __init__(self):
        self.pause_time = None

    def draw_button(self, screen ,message, x, y, width, height, font, inactive_color=BUTTON_IDLE, active_color=BUTTON_ACTIVE):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(screen, active_color, (x, y, width, height))
            if click[0] == 1:
                return True
        else:
            pygame.draw.rect(screen, inactive_color, (x, y, width, height))
        
        text_surface = font.render(message, True, BLACK)
        text_rect = text_surface.get_rect(center=((x + (width // 2)), (y + (height // 2))))
        screen.blit(text_surface, text_rect)
        return False
    
    
    def draw_restart_button(self, screen):
        return self.draw_button(screen, "RESTART", RESTART_BUTTON_X, RESTART_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, font=pygame.font.Font(None, 36))
    
    
    def draw_end_button(self, screen):
        return self.draw_button(screen, "END", END_BUTTON_X, END_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, font=pygame.font.Font(None, 36))
    
    
    def draw_pause_button(self, screen, is_paused):
        if is_paused:
            text = "CONTINUE"
        else:
            text = "PAUSE"
        is_clicked = self.draw_button(screen, text, PAUSE_BUTTON_X, PAUSE_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, font=pygame.font.Font(None, 36))
        if is_clicked:
            is_valid = self.check_click_valid()
            if is_valid:
                self.pause_time = datetime.now()
            return is_valid

        return is_clicked
    
    def check_click_valid(self):
        if self.pause_time == None:
            return True
        time_passed = (datetime.now() - self.pause_time).total_seconds()
        if time_passed > 0.2:
            return True
        else:
            return False
