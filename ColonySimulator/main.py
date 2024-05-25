import pygame
import sys
import time

from datetime import datetime

from configs import *
from cell import Cell
from simulation_manager import SimulationManager


def set_screen():
    pygame.init()
    display_info = pygame.display.Info()
    print(display_info)
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("")
    return screen


def start_app(screen):

    # total_count = (SCREEN_WIDTH // CELL_SIZE) * (SCREEN_HEIGHT // CELL_SIZE)
    # all_list = [i for i in range(total_count)]
    # idx_list = random.sample(all_list, START_LIVE_CELL_COUNT)

    simulation_manager = SimulationManager(screen)

    running = True
    stop    = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not stop:
            simulation_manager.update()
        else:
            pass
        is_end, stop = simulation_manager.update_UI()
        running = not is_end
        pygame.display.flip()
        time.sleep(GAME_INTERVAL)

    pygame.quit()
    sys.exit()


def main():
    screen = set_screen()
    start_app(screen)


if __name__ == "__main__":
    main()