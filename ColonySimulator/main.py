import pygame

from datetime import datetime

from configs import *
from simulation_manager          import SimulationManager
from Screens.screen_manager      import ScreenManager
from Screens.Screens.game_screen import GameScreen


def set_screen():
    pygame.init()
    display_info = pygame.display.Info()
    print(display_info)
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("")
    return screen


def set_screen_manager():
    screen_manager = ScreenManager()
    game_screen   = GameScreen(screen_manager)
    
    screen_manager.add_screen("GameScreen", game_screen)
    screen_manager.set_screen("GameScreen")
    return screen_manager


def start_app(screen, screen_manager):

    while screen_manager.running:
        events = pygame.event.get()
        screen_manager.handle_events(events)
        screen_manager.render(screen)
        screen_manager.update()
        pygame.display.flip()
    
    pygame.quit()
    
def main():
    screen = set_screen()
    screen_manager = set_screen_manager()
    start_app(screen, screen_manager)


if __name__ == "__main__":
    main()