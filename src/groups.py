import pygame

class SpriteGroups(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        
    def draw(self, ):
        # da wir hier Group erweitern, können wir hier die Methode draw() überschreiben und mittels self auf alle Sprites in der Gruuppe zugreifen
        # hier wird die "Kamera" definiert, wir verschieben alles in die entgegen gesetzte Richtung der Bewegung des Spielers
        self.offset.x = -(target_pos[0] - WINDOW_WIDTH / 2)
        self.offset.y = -(target_pos[1] - WINDOW_HEIGHT / 2)
        