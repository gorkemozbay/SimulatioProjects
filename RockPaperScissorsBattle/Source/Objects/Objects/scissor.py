
from Objects.object_base import ObjectBase
from utils               import *
from Managers.image_manager import ImageManager

class Scissor(ObjectBase):
    
    def __init__(self, x, y, speed_x, speed_y):
        super().__init__(x, y, speed_x, speed_y)
        self.object_type = ObjectType.SCISSOR
        self.img         = ImageManager().get_image("Scissor")
