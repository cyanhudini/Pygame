import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self,image, position, direction, groups):
        super().__init__(groups)
        #self.image = pygame.Surface((25, 25))
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect(center = position)
        #self.direction = pygame.math.Vector2()
        self.speed = 40
        self.direction = direction
        self.ttl = pygame.time.get_ticks() #Lebenszeit Bullet
    
    def check_if_distance_is_zero(self, target_pos, self_pos):
        # check if the distance between the player and the enemy is zero
        distance = math.sqrt((target_pos[0] - self_pos[0])**2 + (target_pos[1] - self_pos[1])**2)
        if distance == 0:
            return pygame.math.Vector2(0,0)
        else:
            return ((target_pos - self_pos).normalize())
    
    def update(self, time):
        # self.direction Vector is zero, 
        
        self.rect.center += self.direction * self.speed * time
        if pygame.time.get_ticks() - self.ttl >= 1000:
            self.kill()
        # check ob Bullet außerhalb des Bildschirms ist
        #if self.rect.top < 0 or self.rect.bottom > height or \
        #   self.rect.left < 0 or self.rect.right > width:
        #    self.kill()