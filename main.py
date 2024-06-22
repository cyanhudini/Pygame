import pygame
import random
import sys
from player import Player
from greendots import GreenDot
from sprite_group import SpriteGroup
from pytmx.util_pygame import load_pygame

class Survivor:
    def __init__(self):

        self.pygame.init()

        self.screen_width = 800
        self.screen_height = 600
        self.map_size_x = 10000
        self.map_size_y = 10000
        self.screen = pygame.display.set_mode((screen_width, screen_height))
    # camera = Camera(800, 600)

    self.pygame.display.set_caption("Player Movement")

    # assets wie Sprite PNG's müsste man in einen extra Ordner machen
    self.player_image_path = "r.png"  # Replace with your image path
    player_image_path = "Pygame/player/walking/down.png"  # Replace with your image path
    
    #Liste von Bildpfaden
    self.image_paths = ['Pygame/enemy/skellet/skull_down.png',
                  'Pygame/enemy/franky/franky_down.png',
                  'Pygame/enemy/kürbis/kurbis_down.png'
                  'Pygame/enemy/mino/mino_down.png'
                  'Pygame/enemy/skellet/skull_down.png']

    #player_camera = Camera(screen_width, screen_height)
    
    self.clock = pygame.time.Clock()
    self.all_sprites = SpriteGroup()
  
    self.player = Player(player_image_path, all_sprites, (400, 360))
    
    def setup_map():
        map_path = load_pygame( )
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #player_camera.update(player, map_size_x, map_size_y)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.direction.x = -1
            if keys[pygame.K_RIGHT]:
                player.direction.x = 1
            if keys[pygame.K_DOWN]:
                player.direction.y = 1
            if keys[pygame.K_UP]:
                player.direction.y = -1
            self.player.direction = player.direction.normalize() if player.direction else player.direction
            self.dt = clock.tick(60) / 1000
            self.screen.fill((255, 255, 255))
            # player.draw(screen, player_camera)
            
            self.all_sprites.update(dt)
            all_sprites.draw(player.rect.center) 
            
            pygame.display.update()
        

        pygame.quit()

if __name__ == "__main__":
  main()
