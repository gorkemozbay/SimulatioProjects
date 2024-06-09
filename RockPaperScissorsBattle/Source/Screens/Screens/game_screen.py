
import pygame

from utils import *
from Screens.screen_base    import *
from Objects.object_manager import ObjectManager


class GameScreen(ScreenBase):
    
    def __init__(self, screen_manager):
        super().__init__(screen_manager)
        self.object_manager = ObjectManager()
        self.object_manager.populate_objects()
        self.object_counts = [0, 0, 0]
        
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.screen_manager.running = False
    
    
    def update(self):
        self.object_counts = self.object_manager.update_objects()


    def render(self, screen):
        screen.fill(BACKGROUND)
        self.object_manager.render_objects(screen)
        self.render_UI(screen)
        
        
    def render_UI(self, screen):
        pygame.draw.line(screen, WHITE, (0, OFF_SET_POS), (MAP_WIDTH, OFF_SET_POS), 2)
        self.draw_text(screen, f"Rock: {self.object_counts[0]}",    WHITE, (MAP_WIDTH * 0.15, 20))
        self.draw_text(screen, f"Paper: {self.object_counts[1]}",   WHITE, (MAP_WIDTH * 0.45, 20))
        self.draw_text(screen, f"Scissor: {self.object_counts[2]}", WHITE, (MAP_WIDTH * 0.80, 20))
        is_done, idx = self.check_win_conditions()
        if is_done:
            self.draw_text(screen, f"{self.idx_to_object(idx)} is WINNER", WHITE, (MAP_WIDTH * 0.5, MAP_HEIGHT * 0.5))


    def draw_text(self, screen, text, color, pos):
        text_surface = pygame.font.Font(None, 36).render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = pos
        screen.blit(text_surface, text_rect)
        
    
    def check_win_conditions(self):
        for idx, count in enumerate(self.object_counts):
            if count == NUMBER_OF_OBJ_PER_CLASS * 3:
                return True, idx
        return False, 0
    

    def idx_to_object(self, idx):
        if idx == 0:
            return "Rock"
        elif idx == 1:
            return "Paper"
        elif idx == 2:
            return "Scissor"
        else:
            return "Error"