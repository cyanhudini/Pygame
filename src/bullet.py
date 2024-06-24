import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, direction, groups):
        super().__init__(groups)
        self.image = pygame.Surface((25, 25))
        self.image.fill('red')
        self.rect = self.image.get_rect(center = position)
        #self.direction = pygame.math.Vector2()
        self.speed = 40
        self.direction = direction
        self.ttl = pygame.time.get_ticks() #Lebenszeit Bullet
        
    def update(self, time):
        # self.direction Vector is zero, 
        self.rect.center += self.direction * self.speed * time
        if pygame.time.get_ticks() - self.ttl >= 1000:
            self.kill()
        # check ob Bullet außerhalb des Bildschirms ist
        #if self.rect.top < 0 or self.rect.bottom > height or \
        #   self.rect.left < 0 or self.rect.right > width:
        #    self.kill()