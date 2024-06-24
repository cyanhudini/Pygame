import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.direction = pygame.math.Vector2()
        self.speed = 10
        
    def update(self, time):
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed

        # Check if bullet goes off-screen and remove it
        #if self.rect.top < 0 or self.rect.bottom > height or \
        #   self.rect.left < 0 or self.rect.right > width:
        #    self.kill()