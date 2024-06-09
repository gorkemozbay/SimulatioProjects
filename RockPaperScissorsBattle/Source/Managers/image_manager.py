
import pygame

from configs import *

class ImageManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._images = {}
        return cls._instance


    def load_image(self, name, path):
        img = pygame.image.load(path).convert_alpha()
        resized_img = pygame.transform.scale(img, (OBJ_SIZE, OBJ_SIZE))
        self._images[name] = resized_img


    def get_image(self, name):
        return self._images.get(name)


