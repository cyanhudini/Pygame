import pygame

class CollisionObject(pygame.sprite.Sprite):
    def __init__(self, pos,surface, groups, ):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_rect(topleft=pos)
        