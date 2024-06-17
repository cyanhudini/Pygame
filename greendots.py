import pygame

class GreenDot():
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        
        
    def draw(self, screen):
      
        pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y ), self.radius)
        