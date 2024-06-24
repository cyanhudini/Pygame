import pygame
from variablen import SCREEN_HEIGHT, SCREEN_WIDTH

class SpriteGroups(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        
    def draw(self, spieler_rect):
        # da wir hier Group erweitern, können wir hier die Methode draw() überschreiben und mittels self auf alle Sprites in der Gruuppe zugreifen
        # hier wird die "Kamera" definiert, wir verschieben alles in die entgegen gesetzte Richtung der Bewegung des Spielers
        # target wird hierbei als Spieler definiert
        
        self.offset.x = -(spieler_rect[0] - SCREEN_WIDTH / 2)
        self.offset.y = -(spieler_rect[1] - SCREEN_HEIGHT / 2)
        # sprite wegen Superklasse
        for sprite in self:
            self.surface.blit(sprite.image, sprite.rect.topleft + self.offset)
        