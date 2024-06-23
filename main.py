import pygame
import random
import sys
from player import Player
from greendots import GreenDot
from sprite_group import SpriteGroup
from pytmx.util_pygame import load_pygame

class Survivor:
    def __init__(self):

        pygame.init()

        self.screen_width = 800
        self.screen_height = 600
        self.map_size_x = 10000
        self.map_size_y = 10000
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
    # camera = Camera(800, 600)

        pygame.display.set_caption("Player Movement")

    # assets wie Sprite PNG's müsste man in einen extra Ordner machen
        #self.player_image_path = "r.png"  # Replace with your image path
        self.player_image_path = "/home/nils/Uni/ObjektOrientSprachen/Pygame/player/walking/down.png"  # Replace with your image path
        
        #Liste von Bildpfaden
        self.image_paths = ['Pygame/enemy/skellet/skull_down.png',
                    'Pygame/enemy/franky/franky_down.png',
                    'Pygame/enemy/kürbis/kurbis_down.png'
                    'Pygame/enemy/mino/mino_down.png'
                    'Pygame/enemy/skellet/skull_down.png']

    #player_camera = Camera(screen_width, screen_height)
    
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
    
        self.player = Player(self.player_image_path, self.all_sprites, (400, 360))
        self.setup_map()
        
    def setup_map(self):
        # join( " pfad", "zur", "karte")= "pfad/zur/karte"
        map_path = load_pygame("/".join(("maps", "map1.tmx")))
        for x, y, image in map_path.get_layer_by_name("Kachelebene").tiles():
            #SpriteGroup((x * 64, y * 64), image, self.all_sprites)
            print("x: ", x, "y: ", y, "image: ", image)
            
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #player_camera.update(player, map_size_x, map_size_y)
            
            self.player.direction = self.player.direction.normalize() if self.player.direction else self.player.direction
            self.dt = self.clock.tick(60) / 1000
            self.screen.fill((255, 255, 255))
            # player.draw(screen, player_camera)
            
            self.all_sprites.update(self.dt)
            self.all_sprites.draw(self.screen) 
            
            pygame.display.update()
        

        pygame.quit()

if __name__ == "__main__":
    game = Survivor()
    game.run()