
import random

from Objects.Objects.rock     import Rock
from Objects.Objects.paper    import Paper
from Objects.Objects.scissor  import Scissor
from utils   import *
from configs import *          

class ObjectManager():
    
    def __init__(self):
        self.object_ls = []


    def populate_objects(self):
        for i in range(NUMBER_OF_OBJ_PER_CLASS):
            x = random.randint(MAP_WIDTH * 0.4, MAP_WIDTH * 0.6)
            y = random.randint(OFF_SET_POS * 2, MAP_HEIGHT * 0.3)
            speed_x = random.uniform(-2, -0.1) if random.random() < 0.5 else random.uniform(0.1, 2)
            speed_y = random.uniform(-2, -0.1) if random.random() < 0.5 else random.uniform(0.1, 2)
            obj = Rock(x, y, speed_x, speed_y)
            self.add_object(obj)
            
        for i in range(NUMBER_OF_OBJ_PER_CLASS):
            x = random.randint(MAP_WIDTH * 0.1, MAP_WIDTH * 0.3)
            y = random.randint(MAP_HEIGHT * 0.6, MAP_HEIGHT * 0.9)
            speed_x = random.uniform(-2, -0.1) if random.random() < 0.5 else random.uniform(0.1, 2)
            speed_y = random.uniform(-2, -0.1) if random.random() < 0.5 else random.uniform(0.1, 2)
            obj = Paper(x, y, speed_x, speed_y)
            self.add_object(obj)
            
        for i in range(NUMBER_OF_OBJ_PER_CLASS):
            x = random.randint(MAP_WIDTH * 0.7, MAP_WIDTH * 0.9)
            y = random.randint(MAP_HEIGHT * 0.6, MAP_HEIGHT * 0.9)
            speed_x = random.uniform(-2, -0.1) if random.random() < 0.5 else random.uniform(0.1, 2)
            speed_y = random.uniform(-2, -0.1) if random.random() < 0.5 else random.uniform(0.1, 2)
            obj = Scissor(x, y, speed_x, speed_y)
            self.add_object(obj)
    

    def add_object(self, obj):
        self.object_ls.append(obj)
        
    
    def update_objects(self):
        for current_idx, current_obj in enumerate(self.object_ls):
            current_obj.update()
            for other_idx in range(len(self.object_ls)):
                if current_idx != other_idx:
                    other_object = self.object_ls[other_idx]
                    is_collided = current_obj.get_rect().colliderect(other_object.get_rect())
                    if is_collided:
                        current_obj, other_object = self.manage_collusion(current_obj, other_object)
                        self.object_ls[current_idx] = current_obj
                        self.object_ls[other_idx]   = other_object
        
        obj_counts = [0, 0, 0]            
        for obj in self.object_ls:
            obj_counts[obj.object_type.value - 1] += 1
            
        return obj_counts 

    
    def render_objects(self, screen):
        for obj in self.object_ls:
            obj.render(screen)
            
    
    def manage_collusion(self, obj1, obj2):
        if obj1.object_type == ObjectType.PAPER and obj2.object_type == ObjectType.ROCK:
            obj2 = Paper(obj2.x, obj2.y, obj2.speed_x, obj2.speed_y)
        elif obj1.object_type == ObjectType.ROCK and obj2.object_type == ObjectType.SCISSOR:
            obj2 = Rock(obj2.x, obj2.y, obj2.speed_x, obj2.speed_y)
        elif obj1.object_type == ObjectType.SCISSOR and obj2.object_type == ObjectType.PAPER:
            obj2 = Scissor(obj2.x, obj2.y, obj2.speed_x, obj2.speed_y)
        return obj1, obj2