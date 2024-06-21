import pygame
from player import Player
class SpriteGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.surf = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(0, 0)
    # überschreibe die draw() Methode von Sprite
    def draw(self, target):
        self.offset = target[0]
        for sprite in self:
            self.surf.blit(sprite.image, sprite.rect)