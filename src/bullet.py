import pygame
from settings import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self):

        #create the bullet image
        super(Bullet, self).__init__()
        self.image = pygame.image.load("assets/Sprites/pixel_laser.png").convert_alpha()
        self.rect = self.image.get_rect()

        #define its positioninig and velocity
        self.velx = 15
        self.vely = 0

    def update(self):
        self.rect.x +=  self.velx
        self.rect.y +=  self.vely
