

import pygame
import time

from configs                     import *
from Screens.screen_manager      import ScreenManager
from Screens.Screens.game_screen import GameScreen
from Managers.image_manager      import ImageManager



def set_full_screen():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("")
    return screen


def set_screen():
    pygame.init()
    screen = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))
    pygame.display.set_caption("")
    return screen


def set_screen_manager():
    screen_manager = ScreenManager()
    game_screen    = GameScreen(screen_manager)
    
    screen_manager.add_screen("GameScreen", game_screen)
    screen_manager.set_screen("GameScreen")
    return screen_manager


def setup():
    image_manager = ImageManager()
    image_manager.load_image("Rock",    "Images\Rock.png")
    image_manager.load_image("Paper",   "Images\Paper.png")
    image_manager.load_image("Scissor", "Images\Scissor.png")


def start_app(screen, screen_manager):

    clock = pygame.time.Clock()
    while screen_manager.running:
        events = pygame.event.get()
        screen_manager.handle_events(events)
        screen_manager.render(screen)
        screen_manager.update()
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()
    
def main():
    screen = set_screen()
    setup()
    
    screen_manager = set_screen_manager()
    start_app(screen, screen_manager)


if __name__ == "__main__":
    main()