import pygame

class SpriteGroups(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        
    def draw(self):
        # da wir hier Group erweitern, können wir hier die Methode draw() überschreiben und mittels self auf alle Sprites in der Gruuppe zugreifen
        
        
        pass