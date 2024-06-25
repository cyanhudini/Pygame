import pygame
import random
import sys
import math
from player import Player
from groups import SpriteGroups
from collision_objects import CollisionObject
from sprite import Sprite
from bullet import Bullet
from enemy import Enemy
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
        self.player_path = "/".join(["player", "walking", "down.png"])
        self.bullet_sprite_image ="/".join(["player","projektil", "pr_small_rot.png"])
        # "bug"wenn Player vor Map initialisiert wird, ist Spieler nicht sichtbar bzw. hinter der Map
        self.enemy_sprite_image = "/".join(["enemy","mino", "mino_down.png"])
        
        self.common_paths = [
            "/player/walking/down.png",
            "/maps/pygame_map_nils.tmx",
        ]
    # assets wie Sprite PNG's müsste man in einen extra Ordner machen
        #self.player_image_path = "r.png"  # 
        #self.player_image_path = self.  # R
        
        # die Gruppen tragen dazu bei das wir anhand dieser Zuordnung die Sprites anders behandeln können (objektorient)
        self.enemy_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        
        #Liste von Bildpfaden
        #player_camera = Camera(screen_width, screen_height)
        self.bullet_direction = pygame.Vector2(1, 0)
        self.clock = pygame.time.Clock()
        self.all_sprites = SpriteGroups()
        self.setup_map()
        
        self.player = Player(self.player_path, self.all_sprites, self.collision_sprites, (400, 360))
    def shoot_bullet(self):
        position = self.player.rect.center
        #direction = self.player.direction if (not self.player.direction.x == 0 and not self.player.direction.y == 0) else self.bullet_direction
        #self.bullet_direction = direction
        #print("position: ", position, "direction: ", self.bullet_direction)
        direction = self.player.direction * 250
        if direction.x == 0 and direction.y == 0:
            direction = self.bullet_direction.normalize() * 250
            self.bullet_direction = direction
        # print("position: ", position, "direction: ", direction)
        Bullet(self.bullet_sprite_image, position, direction, (self.all_sprites, self.bullet_sprites))
        
        
    def setup_map(self):
        # join( " pfad", "zur", "karte")= "pfad/zur/karte"
        
        # map_path = load_pygame("/home/nils/Uni/ObjektOrientSprachen/Pygame/maps/pygame_map_nils.tmx")
        map_path = load_pygame("/".join(["maps", "pygame_map.tmx"]))
        for x, y, image in map_path.get_layer_by_name("Kachelebene").tiles():
            # mult. mit 32 da Kacheln 32x32 groß sind in Tiled
            Sprite((x * 32, y * 32), image, self.all_sprites)
            # print("x: ", x, "y: ", y, "image: ", image)
        # spawn enemies in random locations zum testen
        for coll_ob in map_path.get_layer_by_name("Objektebene2"):
            # mult. mit 32 da Kacheln 32x32 groß sind in Tiled
            CollisionObject((coll_ob.x, coll_ob.y), coll_ob.image, (self.all_sprites, self.collision_sprites))
        
        #for i in range(1000):
        #    x = random.randint(0, self.map_size_x)
        #    y = random.randint(0, self.map_size_y)
        #    Enemy((x, y), (self.all_sprites, self.enemy_sprites, self.collision_sprites), self.enemy_sprite_image)
    def check_player_collision_with_enemy(self):
        # check if player collides with enemy
        if pygame.sprite.spritecollide(self.player, self.enemy_sprites, False):
            #print("Player collided with enemy")
            # pygame.quit()
            # sys.exit()
            pass
    def check_bullet_collision_with_enemy(self):
        for bullet in self.bullet_sprites:
            if pygame.sprite.spritecollide(bullet, self.enemy_sprites, False):
                #print("Bullet collided with enemy")
                bullet.kill()
    
    def check_closest_enemy(self):
        threshold_distance = 200
        for enemy in self.enemy_sprites:
            distance = math.sqrt((self.player.rect.centerx - enemy.rect.centerx) ** 2 + (self.player.rect.centery - enemy.rect.centery) ** 2)
            if distance < threshold_distance:
                self.bullet_direction = pygame.Vector2(enemy.rect.center) - pygame.Vector2(self.player.rect.center)
                break
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #player_camera.update(player, map_size_x, map_size_y)
            
            self.dt = self.clock.tick() / 1000
            
            # player.draw(screen, player_camera)
            self.check_closest_enemy()
            self.check_player_collision_with_enemy()
            self.check_bullet_collision_with_enemy()
            self.shoot_bullet()
            self.all_sprites.update(self.dt)
            #self.screen.fill('black')
            self.all_sprites.draw(self.player.rect.center) 
            
            pygame.display.update()
        

        pygame.quit()

if __name__ == "__main__":
    game = Survivor()
    game.run()