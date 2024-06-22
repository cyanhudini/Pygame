import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_path, width, height):
        super().__init__()

        self.image = pygame.image.load(image_path).convert_alpha

#Rechteck um das Bild
        self.rect = self.image.get_rect()
        self.rect.width = width
        self.rect.height = height