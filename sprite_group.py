import pygame
from player import Player
class SpriteGroup(pygame.sprite.Group):
    def __init__(self, position, surface, groups):
        super().__init__()
        self.surface = surface
        self.offset = self.surface.get_frect(topleft=position)
    # überschreibe die draw() Methode von Sprite
    def draw(self, target):
        self.offset = target[0]
        for sprite in self:
            self.surf.blit(sprite.image, sprite.rect)