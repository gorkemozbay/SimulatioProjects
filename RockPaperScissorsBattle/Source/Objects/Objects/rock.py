
from Objects.object_base import ObjectBase
from utils               import *
from Managers.image_manager import ImageManager

class Rock(ObjectBase):
    
    def __init__(self, x, y, speed_x, speed_y):
        super().__init__(x, y, speed_x, speed_y)
        self.object_type = ObjectType.ROCK
        self.img         = ImageManager().get_image("Rock")
