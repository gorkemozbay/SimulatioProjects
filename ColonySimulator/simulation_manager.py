
import pygame
import time

from datetime import datetime

from UI_manager import UI_manager
from configs import *
from cell    import *
from utils   import *

class SimulationManager():

    def __init__(self, screen):
        self.cell_list = []
        self.screen = screen
        self.UI_manager = UI_manager()
        self.is_paused = False
        self.total_stop_time = 0
        self.last_stop_time  = None

        for i in range(0, SCREEN_WIDTH // CELL_SIZE):
            for j in range(0, SCREEN_HEIGHT // CELL_SIZE):
                self.cell_list.append(Cell(i, j))

        self.set_by_click()


    def update(self):
        self.screen.fill(BACKGROUND)
        new_ls = []
        for cell in self.cell_list:
            # draw
            if cell.is_alive:
                pygame.draw.rect(self.screen, WHITE, (cell.x * CELL_SIZE, cell.y * CELL_SIZE, CELL_SIZE - 2, CELL_SIZE - 2))
            else:
                color = self.get_dead_color(cell)
                pygame.draw.rect(self.screen, color, (cell.x * CELL_SIZE, cell.y * CELL_SIZE, CELL_SIZE - 2, CELL_SIZE - 2))
            # update
            cell.neighbor_count    = self.check_neighbors_count(cell)
            new_cell               = self.update_cell(cell)
            new_ls.append(new_cell)
        self.cell_list = new_ls


    def update_UI(self):
        restart = self.UI_manager.draw_restart_button(self.screen)
        end     = self.UI_manager.draw_end_button(self.screen)
        pause   = self.UI_manager.draw_pause_button(self.screen, self.is_paused)
        
        if restart:
            self.restart()
        else:
            if pause:
                self.is_paused = not self.is_paused 
                self.update_stop_time()
        return end, self.is_paused


    def update_cell(self, cell):
        is_alive_in_next_cycle = self.check_alive(cell)
        if is_alive_in_next_cycle: 
            new_cell = Cell(cell.x, cell.y, True, cell.neighbor_count)
        else:
            if cell.is_alive: 
                new_cell = Cell(cell.x, cell.y, False, cell.neighbor_count, datetime.now())
            else:
                new_cell = Cell(cell.x, cell.y, False, cell.neighbor_count, cell.dead_time)
                new_cell.is_paused = cell.is_paused 
        return new_cell
    

    def check_neighbors_count(self, current_cell):
        neighbor_count = 0
        neighbor_ls = self.generate_neighbor_ls(current_cell)
        for neighbor in neighbor_ls:
            cell_idx      = self.calculate_cell_idx(neighbor[0], neighbor[1])
            neighbor_cell = self.cell_list[cell_idx] 
            if neighbor_cell.is_alive:
                neighbor_count +=1 
        return neighbor_count    
    

    def generate_neighbor_ls(self, cell):
        neighbor_ls = []
        for x in range(cell.x - 1, cell.x + 2):
            for y in range(cell.y -1, cell.y +2):
                if (not (x == cell.x and y == cell.y)) and \
                (x >= 0 and x < (SCREEN_WIDTH//CELL_SIZE)) and \
                (y >= 0 and y < (SCREEN_HEIGHT//CELL_SIZE)):
                    neighbor_ls.append((x, y))
        return neighbor_ls


    def generate_all_cell_ls(self):
        all_cell_ls = []
        for cell in self.cell_list:
            if cell.is_alive:
                all_cell_ls.append((cell.x, cell.y))
        return all_cell_ls


    def check_alive(self, cell):
        count = cell.neighbor_count
        if cell.is_alive:
            if count < 2 or count > 3:
                return False
            elif count == 2 or count == 3:
                return True
        else:
            if count == 3:
                return True
            else:
                return False


    def set_cells_alive(self, cell_idx_ls):
        for idx in cell_idx_ls:
            self.cell_list[idx].is_alive   = True


    def set_by_click(self):
        setting_done = True
        while setting_done:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        setting_done = False
                else:
                    if pygame.mouse.get_pressed()[0]:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        cell = Cell(mouse_x // CELL_SIZE, mouse_y // CELL_SIZE)
                        cell_idx = self.calculate_cell_idx(cell.x, cell.y)
                        self.cell_list[cell_idx].is_alive = True
            self.draw()
            pygame.display.flip()

    
    def calculate_cell_idx(self, x, y):
        cell_idx = x * (SCREEN_HEIGHT//CELL_SIZE) + y
        return cell_idx
    
    
    def draw(self):
        self.screen.fill(BACKGROUND)
        for cell in self.cell_list:
            if not cell.is_alive:
                pygame.draw.rect(self.screen, BLACK, (cell.x * CELL_SIZE, cell.y * CELL_SIZE, CELL_SIZE - 2, CELL_SIZE - 2))
            else:
                pygame.draw.rect(self.screen, WHITE, (cell.x * CELL_SIZE, cell.y * CELL_SIZE, CELL_SIZE - 2, CELL_SIZE - 2))
    
    
    def get_dead_color(self, cell):
        if cell.dead_time == None:
            return BACKGROUND
        time_passed = (datetime.now() - cell.dead_time).total_seconds()
        if cell.is_paused:
            time_passed -= self.total_stop_time
        if time_passed >= FADE_OUT_TIMEOUT:
            return BACKGROUND
        else:
            return self.map_dead_time(time_passed)
    

    def map_dead_time(self, time_passed):
        color_code = max(BACKGROUND[0], 255 - (time_passed * FADE_INTENSITY))
        return (color_code, color_code, color_code)
        

    def restart(self):
        self.cell_list = []
        self.is_paused = False
        self.total_stop_time = 0

        for i in range(0, SCREEN_WIDTH // CELL_SIZE):
            for j in range(0, SCREEN_HEIGHT // CELL_SIZE):
                self.cell_list.append(Cell(i, j))
        
        self.set_by_click()
        
    
    def update_stop_time(self):
        if self.is_paused:
            for cell in self.cell_list:
                if not cell.is_alive:
                    cell.is_paused = True
            self.total_stop_time = 0
            self.last_stop_time = datetime.now()
        else:
            self.total_stop_time = (datetime.now() - self.last_stop_time).total_seconds()
