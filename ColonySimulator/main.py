import pygame
import random
import sys

from configs import *
from cell import Cell
from simulation_manager import SimulationManager

def set_screen():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("")
    return screen


def start_app(screen):

    total_count = (SCREEN_WIDTH // CELL_SIZE) * (SCREEN_HEIGHT // CELL_SIZE)
    all_list = [i for i in range(total_count)]
    #idx_list = random.sample(all_list, START_LIVE_CELL_COUNT)

    simulation_manager = SimulationManager(screen)
    simulation_manager.set_by_click()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        simulation_manager.update()
        pygame.display.flip()

    pygame.quit()
    sys.exit()


def main():
    screen = set_screen()
    start_app(screen)


if __name__ == "__main__":
    main()