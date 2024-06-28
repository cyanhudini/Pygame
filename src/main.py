import pygame
import random
import sys
import math
import os
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
        #self.map_size_x = 10000
        #self.map_size_y = 10000
        self.screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
    # camera = Camera(800, 600)

        pygame.display.set_caption("Player Movement")
        self.player_path = "/".join(["player", "down", "1.png"])
        self.bullet_sprite_image ="/".join(["player","projektil", "projektil3png.png"])
        # "bug"wenn Player vor Map initialisiert wird, ist Spieler nicht sichtbar bzw. hinter der Map
        
    # assets wie Sprite PNG's müsste man in einen extra Ordner machen
        #self.player_image_path = "r.png"  # 
        #self.player_image_path = self.  # R
        
        # die Gruppen tragen dazu bei das wir anhand dieser Zuordnung die Sprites anders behandeln können (objektorient)
        self.enemy_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.spawn_points = []
        self.player_sprites = {}
        self.bat_sprites = {}
        self.skeleton_sprites = {}
        self.zombie_sprites = {}
        #Liste von Bildpfaden
        #player_camera = Camera(screen_width, screen_height)
        self.bullet_direction = pygame.Vector2(1, 0)
        self.clock = pygame.time.Clock()
        self.all_sprites = SpriteGroups()
        self.last_shot = pygame.time.get_ticks()
        self.attack_speed_limit = 300 # je höher die Zahl desto niedirger die Frequenz
        
        # self.load_sprites_to_animate()
        self.bullet_speed = 30
        self.t2 = 0
        
        self.load_sprites_to_animate()
        self.setup_map()
        #self.load_animation_sprites_walking_direction()
     
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
            
            "up": [
                    pygame.image.load("/".join(["player", "up", "1.png"])),
                    pygame.image.load("/".join(["player", "up", "2.png"])),
                    #pygame.image.load("/".join(["player", "up", "3.png"]))
                   ],
            "down": [
                    pygame.image.load("/".join(["player", "up", "1.png"])),
                    pygame.image.load("/".join(["player", "down", "2.png"])),
                    #pygame.image.load("/".join(["player", "down", "3.png"]))
                     ],
            "left": [
                    #pygame.image.load("/".join(["player", "left", "1.png"])),
                    pygame.image.load("/".join(["player", "left", "2.png"])),
                     #pygame.image.load("/".join(["player", "left" "3.png"]))
                     ],
            "right": [
                    #pygame.image.load("/".join(["player", "right", "1.png"])),
                    pygame.image.load("/".join(["player", "right", "2.png"])),
                    pygame.image.load("/".join(["player", "right", "3.png"]))]
        }
        
        ''' self.franky = {
            "up": [pygame.image.load("/".join(["enemy", "franky","up", "1.png"])),
                   pygame.image.load("/".join(["enemy", "franky","up", "2.png"])),
                   pygame.image.load("/".join(["enemy", "franky","up", "3.png"]))],
            "down": [pygame.image.load("/".join(["enemy", "franky","down", "1.png"])),
                     pygame.image.load("/".join(["enemy", "franky","down", "2.png"])),
                     pygame.image.load("/".join(["enemy", "franky","down" "3.png"]))],
            "left": [pygame.image.load("/".join(["enemy", "franky","left" "1.png"])),
                     pygame.image.load("/".join(["enemy", "franky","left", "2.png"])),
                     pygame.image.load("/".join(["enemy", "franky","left", "3.png"]))],
            "right": [pygame.image.load("/".join(["enemy", "franky","right", "1.png"])),
                      pygame.image.load("/".join(["enemy", "franky","right", "2.png"])),
                      pygame.image.load("/".join(["enemy", "franky","right", "3.png"]))]
            }
            
        self.bat_sprites = {
            "up": [pygame.image.load("/".join(["enemy", "bat","up", "1.png"])),
                   pygame.image.load("/".join(["enemy", "bat","up" "2.png"])),
                   pygame.image.load("/".join(["enemy", "bat","up", "3.png"]))],
            "down": [pygame.image.load("/".join(["enemy", "bat","down", "1.png"])),
                     pygame.image.load("/".join(["enemy", "bat","down", "2.png"])),
                     pygame.image.load("/".join(["enemy", "bat","down", "3.png"]))],
            "left": [pygame.image.load("/".join(["enemy", "bat","left", "1.png"])),
                     pygame.image.load("/".join(["enemy", "bat","left", "2.png"])),
                     pygame.image.load("/".join(["enemy", "bat", "left","3.png"]))],
            "right": [pygame.image.load("/".join(["enemy", "bat","right", "1.png"])),
                      pygame.image.load("/".join(["enemy", "bat", "right","2.png"])),
                      pygame.image.load("/".join(["enemy", "bat","right", "3.png"]))]
        }
        
        self.skeleton_sprites = {
            "up": [pygame.image.load("/".join(["enemy", "skeleton","up", "1.png"])),
                   pygame.image.load("/".join(["enemy", "skeleton","up", "2.png"])),
                   pygame.image.load("/".join(["enemy", "skeleton","up", "3.png"]))],
            "down": [pygame.image.load("/".join(["enemy", "skeleton","down", "1.png"])),
                     pygame.image.load("/".join(["enemy", "skeleton","down", "2.png"])),
                     pygame.image.load("/".join(["enemy", "skeleton","down", "3.png"]))],
            "left": [pygame.image.load("/".join(["enemy", "skeleton","left", "1.png"])),
                     pygame.image.load("/".join(["enemy", "skeleton","left", "2.png"])),
                     pygame.image.load("/".join(["enemy", "skeleton","left", "3.png"]))],
            "right": [pygame.image.load("/".join(["enemy", "skeleton","right", "1.png"])),
                      pygame.image.load("/".join(["enemy", "skeleton","right", "2.png"])),
                      pygame.image.load("/".join(["enemy", "skeleton","right", "3.png"]))]
        }
        '''
        self.zombie_sprites = {
            "up": [pygame.image.load("/".join(["enemy", "zombie","up" ,"1.png"])),
                   pygame.image.load("/".join(["enemy", "zombie","up", "2.png"])),
                   pygame.image.load("/".join(["enemy", "zombie","up", "3.png"])),
                   pygame.image.load("/".join(["enemy", "zombie","up", "4.png"]))],
            "down": [pygame.image.load("/".join(["enemy", "zombie","down", "1.png"])),
                     pygame.image.load("/".join(["enemy", "zombie","down", "2.png"])),
                     pygame.image.load("/".join(["enemy", "zombie","down", "3.png"])),
                     pygame.image.load("/".join(["enemy", "zombie","down", "4.png"]))],
            "left": [pygame.image.load("/".join(["enemy", "zombie","left", "1.png"])),
                     pygame.image.load("/".join(["enemy", "zombie","left", "2.png"])),
                     pygame.image.load("/".join(["enemy", "zombie","left", "3.png"])),
                     pygame.image.load("/".join(["enemy", "zombie","left", "4.png"]))],
            "right": [pygame.image.load("/".join(["enemy", "zombie","right", "1.png"])),
                      pygame.image.load("/".join(["enemy", "zombie","right", "2.png"])),
                      pygame.image.load("/".join(["enemy", "zombie","right", "3.png"])),
                      pygame.image.load("/".join(["enemy", "zombie","right", "4.png"]))]
        }
    
    def load_animation_sprites_walking_direction(self):
        enemy_sprites_base = os.path("/".join(["enemy"]))
        # da Namen mit Zahlen beginnen kann man easy sortieren
        # lambda ist eine anonyme Funktion, nach Split für 1.png: split[0] = "1" und split[1] = "png"
        
        folders = list(walk(enemy_sprites_base))[0][1]
        for folder in folders:
            print("folder: ", folder)
            for folder_path, sub_folders, files in os.walk("/".join([enemy_sprites_base, folder])):
            # if folder ==
                match folder:
                    case "1":
                        self.franky_sprites.append(sub_folders)
                    case "2":
                        self.bat_sprites.append(sub_folders)
                    case "3":
                        self.mino_sprites.append(sub_folders)
                    case "4":
                        self.skeleton_sprites.append(sub_folders)
                    
        
        
        
        #match enemy_type_number:
        #    case 1:
        #        self.mino_sprites[himmelrichtung] = [pygame.image.load(( "/".join([enemy_sprites_base, f]).sort(key = lambda x: int(x.split(".")[0])))) for f in files]
        #    case 2:
        #        self.bat_sprites[himmelrichtung] = [pygame.image.load(( "/".join([enemy_sprites_base, f]).sort(key = lambda x: int(x.split(".")[0])))) for f in files]
        #    case 3:
        #        self.skeleton_sprites[himmelrichtung] = [pygame.image.load(( "/".join([enemy_sprites_base, f]).sort(key = lambda x: int(x.split(".")[0])))) for f in files]
        #    case 4:
        #        self.franky_sprites[himmelrichtung] = [pygame.image.load(( "/".join([enemy_sprites_base, f]).sort(key = lambda x: int(x.split(".")[0])))) for f in files]
    
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
                self.player = Player(self.player_sprites, self.all_sprites, self.collision_sprites, (obj.x, obj.y), ) 
            else: # da auf Objektebene 1 nur spawn punkte und spieler start punkt sind, füge die restlichen koordinaten als spawn punkte für Gegner hinzu
                self.spawn_points.append((obj.x, obj.y))
                
        
        #for i in range(100):
        #    x = random.randint(0, self.map_size_x)
        #    y = random.randint(0, self.map_size_y)
        #    Enemy((x, y), (self.all_sprites, self.enemy_sprites), self.enemy_sprite_image, self.player, self.collision_sprites, 100)
    
    def set_enemy_flag(self):
        spawn_indikator = random.randint(0,1)
        '''Verteilung Wahrscheinlichkeiten von Spawnchancen
        Bat: 0- 0.4
        Zombie: 0.4 - 0.75
        Skeleton: 0.75 - 0.9
        Franky: 0.9 - 1
        '''
        
        # case spawn_indikator is in range of self.spawn_rate[1]

        match spawn_indikator:
            case rate if 0 <= rate < 0.4:
                return 1
            case rate if 0.4 <= rate < 0.75:
                return 2
            case rate if 0.75 <= rate < 0.9:
                return 3
            case rate if 0.9 <= rate <= 1:
                return 4

    
    
    def spawn_enemies(self):
        #  randomly select a whole number between inclusive 1 and 4
        # different enemy types should have different spawn rates, f.e. 1: 50%, 2: 30%, 3: 15%, 4: 5%
        # random_enemy_type = random.randint(1, 4)
        '''Verteilung Wahrscheinlichkeiten von Spawnchancen
        Bat: 0- 0.4
        Zombie: 0.4 - 0.75
        Skeleton: 0.75 - 0.9
        Franky: 0.9 - 1
        '''
        
        spawn_chance_world = 0.01
        limit = random.random()
        if limit < spawn_chance_world:
            random_enemy_type = self.set_enemy_flag()
            random_enemy_type = 2
            match random_enemy_type:
                case 1:
                    Enemy(random.choice(self.spawn_points), (self.all_sprites, self.enemy_sprites), self.player, self.collision_sprites, 50, self.bat_sprites)
                case 2:
                    Enemy(random.choice(self.spawn_points), (self.all_sprites, self.enemy_sprites), self.player, self.collision_sprites, 150, self.zombie_sprites)
                case 3:
                    Enemy(random.choice(self.spawn_points), (self.all_sprites, self.enemy_sprites), self.player, self.collision_sprites, 200, self.skeleton_sprites)
                case 4:
                    Enemy(random.choice(self.spawn_points), (self.all_sprites, self.enemy_sprites), self.player, self.collision_sprites, 350, self.franky_sprites)
                    
            
        #sprites = load_animation_sprites_walking_direction("down", random_spawn_point)
        # Enemy(self.spawn_points[random_spawn_point], (self.all_sprites, self.enemy_sprites), self.player, self.collision_sprites, 100, sprites)
           
    
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
        
        if t_delta >= self.attack_speed_limit:
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
    
    def spawn_enemy(self):
        # spawn enemies in random intervals
        # generate a random float between 0 and 1
        
        spawn_chance = 0.01
        limit = random.random()
        if limit < spawn_chance:
            random_spawn_point = random.randint(0, len(self.spawn_points) - 1)
            path_mino = "/".join(["enemy", "1","down", "2.png"])
            
            Enemy(self.spawn_points[random_spawn_point], (self.all_sprites, self.enemy_sprites), self.player, self.collision_sprites, 100, path_mino)
    
    
    def run(self):
        #self.load_sprites_to_animate()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #player_camera.update(player, map_size_x, map_size_y)
            
            self.time = self.clock.tick() / 1000
            
            # player.draw(screen, player_camera)
            self.check_closest_enemy()
            self.spawn_enemies()
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