
import pygame

from Screens.screen_base import *
from simulation_manager  import SimulationManager
from UI_manager import UI_manager

class GameScreen(ScreenBase):
    
    def __init__(self, screen_manager):
        super().__init__(screen_manager)
        self.simulation_manager = SimulationManager()
        self.UI_manager = UI_manager()
        self.is_start   = True
        
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.screen_manager.running = False
    
    
    def update(self):
        self.simulation_manager.update()


    def render(self, screen):
        
        if self.is_start:
            self.simulation_manager.set_by_click(screen)
            self.is_start = False
        
        self.simulation_manager.render(screen)
        restart, end, pause = self.UI_manager.render_UI(screen)
        if end:
            self.screen_manager.running = False
        elif restart:
            self.UI_manager.restart()
            self.simulation_manager.restart(screen)
        elif pause:
            self.simulation_manager.pause()


                