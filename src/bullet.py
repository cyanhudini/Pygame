import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, direction, groups):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        #self.direction = pygame.math.Vector2()
        self.speed = 10
        
    def update(self, time):
        self.rect.center += self.direction * self.speed * time
        # check ob Bullet außerhalb des Bildschirms ist
        #if self.rect.top < 0 or self.rect.bottom > height or \
        #   self.rect.left < 0 or self.rect.right > width:
        #    self.kill()