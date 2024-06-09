
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


    def render_UI(self, screen):
        pygame.draw.line(screen, WHITE, (0, OFF_SET_POS), (MAP_WIDTH, OFF_SET_POS), 2)
        self.draw_text(screen, f"Rock: {self.object_counts[0]}", WHITE, (MAP_WIDTH * 0.05, 10))
        self.draw_text(screen, f"Paper: {self.object_counts[1]}", WHITE, (MAP_WIDTH * 0.40, 10))
        self.draw_text(screen, f"Scissor: {self.object_counts[2]}", WHITE, (MAP_WIDTH * 0.75, 10))

    
    def draw_text(self, screen, text, color, pos):
        text_surface = pygame.font.Font(None, 36).render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = pos
        screen.blit(text_surface, text_rect)

    
    def render(self, screen):
        screen.fill(BACKGROUND)
        self.render_UI(screen)
        self.object_manager.render_objects(screen)

                