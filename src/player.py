import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self, image_path, groups, pos):
        # mit superklasse übernimmt Player auch die Methode von Sprite
        # wie z.B. update()
        
        super().__init__(groups)
        self.direction = pygame.math.Vector2()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.speed = 500

    def getInput(self):
        
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        
    def update(self, time):
        self.getInput()
        self.rect.center += self.direction * self.speed * time
    
    def calculate_shooting_direction():
        # schieße entweder in die Richtung des nächsten Gegners oder in die Laufrichtung
        
        pass