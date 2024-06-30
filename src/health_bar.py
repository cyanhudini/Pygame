

import pygame

class HealthBar(pygame.sprite.Sprite):
    def __init__(self, player_health, groups):
        super().__init__(groups)
        
        self.healthbar_length = 100
        self.healthbar_height = 10
        self.max_health = player_health[1]
        self.current_health = player_health[0]
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(400, 600))
        
        
    def draw_health_bar(self):
        pygame.draw.rect(self.image, "red", (0, 0,self.healthbar_length ,self.healthbar_height))     
        pygame.draw.rect(self.image, "green", (0, 0, self.healthbar_length * self.current_health / self.max_health, self.healthbar_height))
    
    def update(self, time):
        self.draw_health_bar()
        