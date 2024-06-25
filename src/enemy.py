import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos, groups, image_path):
        super().__init__(groups)
        self.groups = groups
        self.width = 50
        self.height = 50
        
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image.fill("red")
        self.rect = self.image.get_rect(center=pos)

       
