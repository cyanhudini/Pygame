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
        self.bullet_sprite_image ="/".join(["player","projektil", "projektil3png.png"])
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
        self.spawn_points = []
        #Liste von Bildpfaden
        #player_camera = Camera(screen_width, screen_height)
        self.bullet_direction = pygame.Vector2(1, 0)
        self.clock = pygame.time.Clock()
        self.all_sprites = SpriteGroups()
        self.last_shot = pygame.time.get_ticks()
        self.setup_map()
        # self.load_sprites_to_animate()
        self.bullet_speed = 40
        self.t2 = 0

        self.player_sprites = {}
        self.mino_sprites = {} 
        self.bat_sprites = {}
        self.skeleton_sprites = {}
        self.franky_sprites = {}
        
        
    def shoot_bullet(self):
        position = self.player.rect.center
        #direction = self.player.direction if (not self.player.direction.x == 0 and not self.player.direction.y == 0) else self.bullet_direction
        #self.bullet_direction = direction
        #print("position: ", position, "direction: ", self.bullet_direction)
        direction = self.player.direction
        if direction.x == 0 and direction.y == 0:
            # direction ist praktisch die Geschwindigkeit der Kugel bzw. mit
            direction = self.bullet_direction.normalize() * self.bullet_speed
            self.bullet_direction = direction
        # print("position: ", position, "direction: ", direction)
        Bullet(self.bullet_sprite_image, position, direction, (self.all_sprites, self.bullet_sprites))
        
    def load_sprites_to_animate(self):
        # keine schöne Lösung, aber es funktioniert
        self.player_sprites = {
            "up": [pygame.image.load("/".join(["player", "walking", "1.png"])).convert_alpha(),
                   pygame.image.load("/".join(["player", "walking", "2.png"])).convert_alpha(),
                   pygame.image.load("/".join(["player", "walking", "3.png"])).convert_alpha()],
            "down": [pygame.image.load("/".join(["player", "walking", "1.png"])).convert_alpha(),
                     pygame.image.load("/".join(["player", "walking", "2.png"])).convert_alpha(),
                     pygame.image.load("/".join(["player", "walking", "3.png"])).convert_alpha()],
            "left": [pygame.image.load("/".join(["player", "walking", "1.png"])).convert_alpha(),
                     pygame.image.load("/".join(["player", "walking", "2.png"])).convert_alpha(),
                     pygame.image.load("/".join(["player", "walking", "3.png"])).convert_alpha()],
            "right": [pygame.image.load("/".join(["player", "walking", "1.png"])).convert_alpha(),
                      pygame.image.load("/".join(["player", "walking", "2.png"])).convert_alpha(),
                      pygame.image.load("/".join(["player", "walking", "3.png"])).convert_alpha()]
        }
        
        self.mino_sprites = {
            "up": [pygame.image.load("/".join(["enemy", "mino", "1.png"])).convert_alpha(),
                   pygame.image.load("/".join(["enemy", "mino", "2.png"])).convert_alpha(),
                   pygame.image.load("/".join(["enemy", "mino", "3.png"])).convert_alpha()],
            "down": [pygame.image.load("/".join(["enemy", "mino", "1.png"])).convert_alpha(),
                     pygame.image.load("/".join(["enemy", "mino", "2.png"])).convert_alpha(),
                     pygame.image.load("/".join(["enemy", "mino", "3.png"])).convert_alpha()],
            "left": [pygame.image.load("/".join(["enemy", "mino", "1.png"])).convert_alpha(),
                     pygame.image.load("/".join(["enemy", "mino", "2.png"])).convert_alpha(),
                     pygame.image.load("/".join(["enemy", "mino", "3.png"])).convert_alpha()],
            "right": [pygame.image.load("/".join(["enemy", "mino", "1.png"])).convert_alpha(),
                      pygame.image.load("/".join(["enemy", "mino", "2.png"])).convert_alpha(),
                      pygame.image.load("/".join(["enemy", "mino", "3.png"])).convert_alpha()]
            }
        self.bat_sprites = {
            "up": [pygame.image.load("/".join(["enemy", "bat", "1.png"])).convert_alpha(),
                   pygame.image.load("/".join(["enemy", "bat", "2.png"])).convert_alpha(),
                   pygame.image.load("/".join(["enemy", "bat", "3.png"])).convert_alpha()],
            "down": [pygame.image.load("/".join(["enemy", "bat", "1.png"])).convert_alpha(),
                     pygame.image.load("/".join(["enemy", "bat", "2.png"])).convert_alpha(),
                     pygame.image.load("/".join(["enemy", "bat", "3.png"])).convert_alpha()],
            "left": [pygame.image.load("/".join(["enemy", "bat", "1.png"])).convert_alpha(),
                     pygame.image.load("/".join(["enemy", "bat", "2.png"])).convert_alpha(),
                     pygame.image.load("/".join(["enemy", "bat", "3.png"])).convert_alpha()],
            "right": [pygame.image.load("/".join(["enemy", "bat", "1.png"])).convert_alpha(),
                      pygame.image.load("/".join(["enemy", "bat", "2.png"])).convert_alpha(),
                      pygame.image.load("/".join(["enemy", "bat", "3.png"])).convert_alpha()]
        }
        self.skeleton_sprites = {
            "up": [pygame.image.load("/".join(["enemy", "skeleton", "1.png"])).convert_alpha(),
                   pygame.image.load("/".join(["enemy", "skeleton", "2.png"])).convert_alpha(),
                   pygame.image.load("/".join(["enemy", "skeleton", "3.png"])).convert_alpha()],
            "down": [pygame.image.load("/".join(["enemy", "skeleton", "1.png"])).convert_alpha(),
                     pygame.image.load("/".join(["enemy", "skeleton", "2.png"])).convert_alpha(),
                     pygame.image.load("/".join(["enemy", "skeleton", "3.png"])).convert_alpha()],
            "left": [pygame.image.load("/".join(["enemy", "skeleton", "1.png"])).convert_alpha(),
                     pygame.image.load("/".join(["enemy", "skeleton", "2.png"])).convert_alpha(),
                     pygame.image.load("/".join(["enemy", "skeleton", "3.png"])).convert_alpha()],
            "right": [pygame.image.load("/".join(["enemy", "skeleton", "1.png"])).convert_alpha(),
                      pygame.image.load("/".join(["enemy", "skeleton", "2.png"])).convert_alpha(),
                      pygame.image.load("/".join(["enemy", "skeleton", "3.png"])).convert_alpha()]
        }
        self.franky_sprites = {
            "up": [pygame.image.load("/".join(["enemy", "franky", "1.png"])).convert_alpha(),
                   pygame.image.load("/".join(["enemy", "franky", "2.png"])).convert_alpha(),
                   pygame.image.load("/".join(["enemy", "franky", "3.png"])).convert_alpha()],
            "down": [pygame.image.load("/".join(["enemy", "franky", "1.png"])).convert_alpha(),
                     pygame.image.load("/".join(["enemy", "franky", "2.png"])).convert_alpha(),
                     pygame.image.load("/".join(["enemy", "franky", "3.png"])).convert_alpha()],
            "left": [pygame.image.load("/".join(["enemy", "franky", "1.png"])).convert_alpha(),
                     pygame.image.load("/".join(["enemy", "franky", "2.png"])).convert_alpha(),
                     pygame.image.load("/".join(["enemy", "franky", "3.png"])).convert_alpha()],
            "right": [pygame.image.load("/".join(["enemy", "franky", "1.png"])).convert_alpha(),
                      pygame.image.load("/".join(["enemy", "franky", "2.png"])).convert_alpha(),
                      pygame.image.load("/".join(["enemy", "franky", "3.png"])).convert_alpha()]
        }
    
    def setup_map(self):
        # join( " pfad", "zur", "karte")= "pfad/zur/karte"
        
        # map_path = load_pygame("/home/nils/Uni/ObjektOrientSprachen/Pygame/maps/pygame_map_nils.tmx")
        map_path = load_pygame("/".join(["maps", "pygame_map_loads1.tmx"]))
        for x, y, image in map_path.get_layer_by_name("Kachelebene").tiles():
            # mult. mit 32 da Kacheln 32x32 groß sind in Tiled
            Sprite((x * 32, y * 32), image, self.all_sprites)
            # print("x: ", x, "y: ", y, "image: ", image)
        # spawn alle Collision Objects
        for coll_ob in map_path.get_layer_by_name("Objektebene 2"):
            # mult. mit 32 da Kacheln 32x32 groß sind in Tiled
        
            CollisionObject((coll_ob.x, coll_ob.y), coll_ob.image, (self.all_sprites, self.collision_sprites))
            
        
        for obj in map_path.get_layer_by_name("Objektebene 1"):
            if obj.name == "Spawn_Player":
                self.player = Player(self.player_path, self.all_sprites, self.collision_sprites, (obj.x, obj.y), ) 
            else: # da auf Objektebene 1 nur spawn punkte und spieler start punkt sind, füge die restlichen koordinaten als spawn punkte für Gegner hinzu
                self.spawn_points.append((obj.x, obj.y))
                pass
        
        #for i in range(100):
        #    x = random.randint(0, self.map_size_x)
        #    y = random.randint(0, self.map_size_y)
        #    Enemy((x, y), (self.all_sprites, self.enemy_sprites), self.enemy_sprite_image, self.player, self.collision_sprites, 100)
    
    def spawn_enemy(self):
        pass       
    
    def choose_random_for_spawing(self):
        pass
    
    def check_player_collision_with_enemy(self):
        # check if player collides with enemy
        if pygame.sprite.spritecollide(self.player, self.enemy_sprites, False):
            #print("Player collided with enemy")
            # pygame.quit()
            # sys.exit()
            pass
    def check_bullet_collision_with_enemy(self):
        if self.bullet_sprites:
            for bullet in self.bullet_sprites:
                hit_sprite = pygame.sprite.spritecollide(bullet, self.enemy_sprites, None)
                if hit_sprite:
                    #print("Bullet collided with enemy")
                    #gleiche Logik wie bei Bullet
                    for hit_enemy in hit_sprite:
                        hit_enemy.health -= 10
                        print("Enemy health: ", hit_enemy.health)
                        if hit_enemy.health <= 0:
                            print("Enemy killed")
                            hit_enemy.kill()

                    bullet.kill()
                    
    def attack_speed(self):
        # attack speed
        # die Clock bzw. der tick beeinflusst die Uhr -> Bug
        self.t1 = pygame.time.get_ticks()
        t_delta = self.t1 - self.t2
        print("t_delta: ", t_delta)
        if t_delta >= 150:
            self.shoot_bullet()
            self.t2 = self.t1
       
    
    def check_closest_enemy(self):
        threshold_distance = 200
        for enemy in self.enemy_sprites:
            distance = math.sqrt((self.player.rect.centerx - enemy.rect.centerx) ** 2 + (self.player.rect.centery - enemy.rect.centery) ** 2)
            if distance < threshold_distance:
                self.bullet_direction = pygame.Vector2(enemy.rect.center) - pygame.Vector2(self.player.rect.center)
                break
    def check_collision_with_enemies(self):
        # da, wenn die Player Klasse sowie die Enemy Klasse Gruppe "collision sprites" bekommt, entsteht ein Bug bei dem entweder Gegner sich nicht bewegen
        # deswegen ein simples Kollisions System, check ob zwei Sprites miteinander kollidieren
        if pygame.sprite.spritecollide(self.player, self.enemy_sprites, False, None):
            pass
        pass
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #player_camera.update(player, map_size_x, map_size_y)
            
            self.time = self.clock.tick() / 1000
            
            # player.draw(screen, player_camera)
            self.check_closest_enemy()
            #self.check_player_collision_with_enemy()
            self.check_bullet_collision_with_enemy()
            self.attack_speed()
            self.all_sprites.update(self.time)
            #self.screen.fill('black')
            self.all_sprites.draw(self.player.rect.center) 
            
            pygame.display.update()
        

        pygame.quit()

if __name__ == "__main__":
    game = Survivor()
    game.run()