import pygame
import random
import sys
from player import Player
from greendots import GreenDot
from sprite_group import Sprite
from pytmx.util_pygame import load_pygame
from variable import SCREEN_HEIGHT, SCREEN_WIDTH
class Survivor:
    def __init__(self):

        pygame.init()

        #self.screen_width = 1000
        #self.screen_height = 1000
        self.map_size_x = 10000
        self.map_size_y = 10000
        self.screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
    # camera = Camera(800, 600)

        pygame.display.set_caption("Player Movement")

    # assets wie Sprite PNG's müsste man in einen extra Ordner machen
        #self.player_image_path = "r.png"  # Replace with your image path
        self.player_image_path = "/home/nils/Uni/ObjektOrientSprachen/Pygame/player/walking/down.png"  # Replace with your image path
        
        #Liste von Bildpfaden
    #player_camera = Camera(screen_width, screen_height)
    
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.setup_map()
        # bug: player wird praktisch unter die Karte gezeichnet
        self.player = Player(self.player_image_path, self.all_sprites, (400, 360))
        
        
    def setup_map(self):
        # join( " pfad", "zur", "karte")= "pfad/zur/karte"
        map_path = load_pygame("/home/nils/Uni/ObjektOrientSprachen/Pygame/maps/pygame_map_nils.tmx")
        for x, y, image in map_path.get_layer_by_name("Kachelebene").tiles():
            Sprite((x * 32, y * 32), image, self.all_sprites)
            print("x: ", x, "y: ", y, "image: ", image)
            
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #player_camera.update(player, map_size_x, map_size_y)
            
            self.dt = self.clock.tick() / 1000
            self.screen.fill('black')
            # player.draw(screen, player_camera)
            
            self.all_sprites.update(self.dt)
            self.all_sprites.draw(self.screen) 
            
            pygame.display.update()
        

        pygame.quit()

if __name__ == "__main__":
    game = Survivor()
    game.run()