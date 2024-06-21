import pygame
from player import Player
class Camera(pygame.sprite.Group):
    def __init__(self, screen_size_x, screen_size_y):
        super().__init__()
        self.x = 0
        self.y = 0
        self.camera_view_x = screen_size_x
        self.camera_view_y = screen_size_y
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2
        self.internal_surface_size = (2500,2500)
        self.internal_offset = pygame.math.Vector2()
        self.internal_offset.x = self.internal_surface_size[0] // 2 - self.half_w
        self.internal_offset.y = self.internal_surface_size[1] // 2 - self.half_h

    def center_target_camera(self,target):
	    self.offset.x = target.rect.centerx - self.half_w
	    self.offset.y = target.rect.centery - self.half_h
     
    def draw_player(self, player):
        self.center_target_camera(player)
        
        for sprite in self.sprites():
            offset_coordinate = sprite.rect.topleft - self.offset + self.internal_offset
            self.display_surface.blit(sprite.image, offset_coordinate)