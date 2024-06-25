import pygame
import random
import sys
from player import Player
from groups import SpriteGroups
from sprite import Sprite
from bullet import Bullet
from pytmx.util_pygame import load_pygame
from variablen import SCREEN_HEIGHT, SCREEN_WIDTH
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
        self.all_sprites = SpriteGroups()
        self.setup_map()
        # "bug"wenn Player vor Map initialisiert wird
        self.player = Player(self.player_image_path, self.all_sprites, (400, 360))
    def shoot_bullet(self):
        position = self.player.rect.center
        direction = self.player.direction
        Bullet( position, direction, self.all_sprites)
        
        
    def setup_map(self):
        # join( " pfad", "zur", "karte")= "pfad/zur/karte"
        map_path = load_pygame("/".join(["maps", "pygame_map_nils.tmx"]))
        for x, y, image in map_path.get_layer_by_name("Kachelebene").tiles():
            # mult. mit 32 da Kacheln 32x32 groß sind in Tiled
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
            
            # player.draw(screen, player_camera)
            
            self.all_sprites.update(self.dt)
            #self.screen.fill('black')
            self.all_sprites.draw(self.player.rect.center) 
            
            pygame.display.update()
        

        pygame.quit()

if __name__ == "__main__":
    game = Survivor()
    game.run()