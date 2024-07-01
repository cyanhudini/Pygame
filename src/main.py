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
from upgrade import Upgrade
from health_bar import HealthBar
from pytmx.util_pygame import load_pygame
from variablen import SCREEN_HEIGHT, SCREEN_WIDTH


# Todo; fix das Anvisieren, mehr Schaden am SPieler o. weniger Leben
# Todo: andere shootng Modes, Health Bar
# Todo:
class Survivor:
    def __init__(self):

        pygame.init()   
        self.screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
        pygame.display.set_caption("Survivor")
        self.player_path = "/".join(["player", "down", "1.png"])
        self.bullet_sprite_image ="/".join(["player","projektil", "projektil3png.png"])
        
        
        # die Gruppen tragen dazu bei das wir anhand dieser Zuordnung die Sprites anders behandeln können (objektorient)
        #Sprite Groups
        self.enemy_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        self.upgrade_card_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.all_sprites = SpriteGroups()
        
        self.spawn_points = []
        self.upgrade_types = ["dmg", "defense", "health"]
        
        self.player_sprites = {}
        self.goblin_sprites = {}
        self.skeleton_sprites = {}
        self.zombie_sprites = {}
        self.franky_sprites = {}
        self.card_sprites = {}
        
        #Liste von Bildpfaden
        #player_camera = Camera(screen_width, screen_height)
        self.player_can_be_hit = True
        self.bullet_direction = pygame.Vector2(1, 0)
        self.clock = pygame.time.Clock()
        
        self.game_ticks = pygame.time.get_ticks()
        
        # Variablen zum Ändern
        self.attack_speed_limit = 300 # je höher die Zahl desto niedirger die Frequenz
        self.bullet_speed = 29
        self.t2 = 0
        self.t4 = 0
        
        self.load_sprites_to_animate()
        self.setup_map()
        # Upgrade((self.all_sprites,self.upgrade_card_sprites), self.player.pos,"dmg", self.card_sprites)
       
       
        self.paused = False
    
    def shoot_bullet(self):
        position = self.player.rect.center
        #direction = self.player.direction if (not self.player.direction.x == 0 and not self.player.direction.y == 0) else self.bullet_direction
        #self.bullet_direction = direction
        #print("position: ", position, "direction: ", self.bullet_direction)
        direction = pygame.Vector2(1,0)
        if self.player.direction.x == 0 and self.player.direction.y == 0:
            direction = self.bullet_direction
        direction = direction.normalize() * self.bullet_speed
        # print("position: ", position, "direction: ", direction)
        Bullet(self.bullet_sprite_image, position, direction, (self.all_sprites, self.bullet_sprites))
    
    
    def shoot_bullets(self):
        position = self.player.rect.center
        
        
        direction = self.bullet_direction.normalize() * self.bullet_speed
        # print("position: ", position, "direction: ", direction)
        Bullet(self.bullet_sprite_image, position, direction, (self.all_sprites, self.bullet_sprites))

    def load_sprites_to_animate(self):
        # keine schöne Lösung, aber es funktioniert
        
        # hier könnte man noch mehr sprite cards einfügen, nach dem Muster wie z.B. upgrade_defense.xfc in gimp lädt
        self.card_sprites = {
            "dmg": ("/".join(["player", "upgrade", "upgrade_dmg.png"])),
            "defense": ("/".join(["player", "upgrade", "upgrade_defense.png"])),
            "health": ("/".join(["player", "upgrade", "upgrade_health.png"]))

        }
        
        self.player_sprites = {
            
            "up": [
                    pygame.image.load("/".join(["player", "up", "1.png"])),
                    pygame.image.load("/".join(["player", "up", "2.png"])),
                    pygame.image.load("/".join(["player", "up", "3.png"])),
                    pygame.image.load("/".join(["player", "up", "4.png"]))
                   ],
            "down": [
                    pygame.image.load("/".join(["player", "down", "1.png"])),
                    pygame.image.load("/".join(["player", "down", "2.png"])),
                    pygame.image.load("/".join(["player", "down", "25.png"])),
                    pygame.image.load("/".join(["player", "down", "3.png"])),
                    pygame.image.load("/".join(["player", "down", "4.png"]))
                     ],
            "left": [
                    pygame.image.load("/".join(["player", "left", "1.png"])),
                    pygame.image.load("/".join(["player", "left", "2.png"])),
                    pygame.image.load("/".join(["player", "left", "3.png"])),
                    pygame.image.load("/".join(["player", "left" ,"4.png"]))
                     ],
            "right": [
                    #pygame.image.load("/".join(["player", "right", "1.png"])),
                    pygame.image.load("/".join(["player", "right", "2.png"])),
                    pygame.image.load("/".join(["player", "right", "3.png"])),
                    pygame.image.load("/".join(["player", "right", "4.png"])),
                    pygame.image.load("/".join(["player", "right", "5.png"])),
                    pygame.image.load("/".join(["player", "right", "6.png"])),
                    ]
        }
        
        self.franky_sprites = {
            "up":[
                    pygame.image.load("/".join(["enemy", "franky","up", "1.png"])),
                    pygame.image.load("/".join(["enemy", "franky","up", "2.png"])),
                    pygame.image.load("/".join(["enemy", "franky","up", "3.png"])),
                   pygame.image.load("/".join(["enemy", "franky","up", "4.png"]))
                    ],
            "down":[
                    pygame.image.load("/".join(["enemy", "franky","down", "1.png"])),
                     pygame.image.load("/".join(["enemy", "franky","down", "2.png"])),
                     pygame.image.load("/".join(["enemy", "franky","down", "3.png"])),
                    pygame.image.load("/".join(["enemy", "franky","down" ,"4.png"]))
                     ],
            "left": [pygame.image.load("/".join(["enemy", "franky","left" ,"1.png"])),
                     pygame.image.load("/".join(["enemy", "franky","left", "2.png"])),
                     pygame.image.load("/".join(["enemy", "franky","left", "3.png"])),
                     pygame.image.load("/".join(["enemy", "franky","left", "4.png"]))
                    ],
            "right": [
                    pygame.image.load("/".join(["enemy", "franky","right", "1.png"])),
                    pygame.image.load("/".join(["enemy", "franky","right", "2.png"])),
                    pygame.image.load("/".join(["enemy", "franky","right", "3.png"])),
                    pygame.image.load("/".join(["enemy", "franky","right", "4.png"]))
                    ]
            }
            
        self.goblin_sprites = {
            "up": [pygame.image.load("/".join(["enemy", "goblin","up", "1.png"])),
                   pygame.image.load("/".join(["enemy", "goblin","up", "2.png"])),
                   pygame.image.load("/".join(["enemy", "goblin","up", "3.png"])),
                   pygame.image.load("/".join(["enemy", "goblin","up", "4.png"]))
                   ],
            "down": [pygame.image.load("/".join(["enemy", "goblin","down", "1.png"])),
                     pygame.image.load("/".join(["enemy", "goblin","down", "2.png"])),
                     pygame.image.load("/".join(["enemy", "goblin","down", "3.png"])),
                     pygame.image.load("/".join(["enemy", "goblin","down", "4.png"]))
                     ],
            "left": [pygame.image.load("/".join(["enemy", "goblin","left", "1.png"])),
                     pygame.image.load("/".join(["enemy", "goblin","left", "2.png"])),
                     pygame.image.load("/".join(["enemy", "goblin", "left","3.png"])),
                     pygame.image.load("/".join(["enemy", "goblin", "left","4.png"]))
                     ],
            "right": [pygame.image.load("/".join(["enemy", "goblin","right", "1.png"])),
                      pygame.image.load("/".join(["enemy", "goblin", "right","2.png"])),
                      pygame.image.load("/".join(["enemy", "goblin","right", "3.png"])),
                      pygame.image.load("/".join(["enemy", "goblin","right", "4.png"]))
                      ]
        }
        
        self.skeleton_sprites = {
            "up": [pygame.image.load("/".join(["enemy", "skeleton","up", "1.png"])),
                   pygame.image.load("/".join(["enemy", "skeleton","up", "2.png"])),
                   pygame.image.load("/".join(["enemy", "skeleton","up", "3.png"])),
                   pygame.image.load("/".join(["enemy", "skeleton","up", "4.png"]))
                   ],
            "down": [pygame.image.load("/".join(["enemy", "skeleton","down", "1.png"])),
                     pygame.image.load("/".join(["enemy", "skeleton","down", "2.png"])),
                     pygame.image.load("/".join(["enemy", "skeleton","down", "3.png"])),
                    pygame.image.load("/".join(["enemy", "skeleton","down", "4.png"]))
                    ],
            "left": [
                    pygame.image.load("/".join(["enemy", "skeleton","left", "1.png"])),
                     pygame.image.load("/".join(["enemy", "skeleton","left", "2.png"])),
                     pygame.image.load("/".join(["enemy", "skeleton","left", "3.png"])),
                     pygame.image.load("/".join(["enemy", "skeleton","left", "4.png"]))
                     ],
            "right": [
                    pygame.image.load("/".join(["enemy", "skeleton","right", "1.png"])),
                    pygame.image.load("/".join(["enemy", "skeleton","right", "2.png"])),
                    pygame.image.load("/".join(["enemy", "skeleton","right", "3.png"])),
                    pygame.image.load("/".join(["enemy", "skeleton","right", "4.png"]))
                    ]
        }
        
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
                    
    def setup_map(self):
        # join( " pfad", "zur", "karte")= "pfad/zur/karte"
        
        
        map_path = load_pygame("/".join(["maps", "pygame_map_loads1.tmx"]))
        for x, y, image in map_path.get_layer_by_name("Kachelebene").tiles():
            # mult. mit 32 da Kacheln 32x32 groß sind in Tiled
            Sprite((x * 32, y * 32), image, self.all_sprites)
        # spawn alle Collision Objects
        for coll_ob in map_path.get_layer_by_name("Objektebene 2"):
            # mult. mit 32 da Kacheln 32x32 groß sind in Tiled
        
            CollisionObject((coll_ob.x, coll_ob.y), coll_ob.image, (self.all_sprites, self.collision_sprites))
            
        for obj in map_path.get_layer_by_name("Objektebene 1"):
            if obj.name == "Spawn_Player":
                self.player = Player(self.player_sprites, self.all_sprites, self.collision_sprites, (obj.x, obj.y), 1000) 
            else: # da auf Objektebene 1 nur spawn punkte und spieler start punkt sind, füge die restlichen koordinaten als spawn punkte für Gegner hinzu
                self.spawn_points.append((obj.x, obj.y))
          
    def trigger_upgrade_event(self):
        # if player level up, player can choose between three different upgrades
      
        if self.player.is_level_up == True:
            upgrades = self.determine_upgrade_type()
        
            for i in range(3):
                # damit die Karte von links nach rechts gerendert werden und nicht außerhalb des Bildschirms sind
                position = (self.player.pos[0] + 170 * i, self.player.pos[1]) - pygame.Vector2(170, 0)
                Upgrade((self.all_sprites, self.upgrade_card_sprites), position, upgrades[i], self.card_sprites)
            self.paused = True
            self.player.is_level_up = False
     
    def set_enemy_flag(self):
        spawn_indikator = random.randint(0,1)
        '''Verteilung Wahrscheinlichkeiten von Spawnchancen
        Bat: 0- 0.4
        Zombie: 0.4 - 0.75
        Skeleton: 0.75 - 0.9
        Franky: 0.9 - 1
        '''

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
        '''Verteilung Wahrscheinlichkeiten von Spawnchancen
        Bat: 0- 0.4
        Zombie: 0.4 - 0.75
        Skeleton: 0.75 - 0.9
        Franky: 0.9 - 1
        '''
        t = pygame.time.get_ticks()
        #print("ingame ticks: ", t)
        spawn_chance_world = (0.30/(0.15*((t/1000)*60) + 1))
        # https://riskofrain2.fandom.com/wiki/Tougher_Times
        # je länger das Spiel dauert, desto höher die Spawnchance
        # erhöhe den Zähler um die Spawn Chance zu erhöhen
        
        limit = random.random()
        if limit < spawn_chance_world:
            random_enemy_type = self.set_enemy_flag()
            print("Enemy spawned")
            #random_enemy_type = 1
            match random_enemy_type:
                case 1:
                    Enemy(random.choice(self.spawn_points), (self.all_sprites, self.enemy_sprites), self.player, self.collision_sprites, 50, 10, 2, self.goblin_sprites)
                case 2:
                    Enemy(random.choice(self.spawn_points), (self.all_sprites, self.enemy_sprites), self.player, self.collision_sprites, 110, 30, 7, self.zombie_sprites)
                case 3:
                    Enemy(random.choice(self.spawn_points), (self.all_sprites, self.enemy_sprites), self.player, self.collision_sprites, 200, 80, 15 ,self.skeleton_sprites)
                case 4:
                    Enemy(random.choice(self.spawn_points), (self.all_sprites, self.enemy_sprites), self.player, self.collision_sprites, 350,140, 33, self.franky_sprites)
                    
    def can_player_take_damage(self):
        # wenn Spieler Schaden nimmt, kann dieser für eine bestimmte Zeit nicht
        # ähnlich wie beim Schießen
        if self.player_can_be_hit == False:
            self.t3 = pygame.time.get_ticks()
            t_delta = self.t3 - self.t4
            #print("t_delta: ", t_delta)
            if t_delta >= 700:
                #print("Player can be hit again")
                self.player_can_be_hit = True
                self.t4 = self.t3
        
        
    def check_player_collision_with_enemy(self):
        # check if player collides with enemy
        self.can_player_take_damage()
        for enemy in self.enemy_sprites:
            if pygame.sprite.spritecollide(self.player, self.enemy_sprites, False):
        #if pygame.sprite.spritecollide(self.player, self.enemy_sprites, False):
                if self.player_can_be_hit:
                    total_damage = enemy.damage * (0.9589) ** self.player.amount_defense_upgrade
                    #print("Total damage: ", total_damage)
                    #print("Player health: ", self.player.current_health)
                    self.player.current_health -= total_damage
                    if self.player.current_health <= 0:
                        print("Game Over")
                        pygame.quit()
                        sys.exit()
                    # https://riskofrain2.fandom.com/wiki/Alien_Head
                    #The skill cooldown is determined by the formula cooldown ⋅ 0.75 ^ amount
                    self.player_can_be_hit = False

    
        
    def check_bullet_collision_with_enemy(self):
        if self.bullet_sprites:
            for bullet in self.bullet_sprites:
                hit_sprite = pygame.sprite.spritecollide(bullet, self.enemy_sprites, None)
                if hit_sprite:
                    #print("Bullet collided with enemy")
                    #gleiche Logik wie bei Bullet
                    for hit_enemy in hit_sprite:
                        hit_enemy.health -= 15 * self.player.damage_multiplier
                        # print("Enemy health: ", hit_enemy.health)
                        if hit_enemy.health <= 0:
                          
                            self.player.gain_exp(hit_enemy.experience_on_death)
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
        threshold_distance = 330
        for enemy in self.enemy_sprites:
            distance = math.sqrt((self.player.hitbox.centerx - enemy.hitbox.centerx) ** 2 + (self.player.hitbox.centery - enemy.hitbox.centery) ** 2)
            if distance <= threshold_distance:
                # print("enemy in range")
                self.bullet_direction = pygame.Vector2(enemy.hitbox.center) - pygame.Vector2(self.player.hitbox.center)
            
                
    def determine_upgrade_type(self):
        possible_upgrades = []
        # shuffle ändert die Reihenfolge der Liste, gib dann die ersten drei aus       
        random.shuffle(self.upgrade_types)
        # code geändert damit auch tatsächlich eine beliebig große anzahl an upgrades möglich ist
        # da es nur drei upgrades gibt, sinds immer die gleichen drei
        possible_upgrades = self.upgrade_types[:3]
        return possible_upgrades
        
    def remove_upgrade_cards(self):
        for upgrade in self.upgrade_card_sprites:
                upgrade.kill()
        self.paused = False
    
    def run(self):
        #self.load_sprites_to_animate()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and self.paused == True:
                    
                    if event.key == pygame.K_1:
                        self.upgrade_card_sprites.sprites()[0].is_clicked(self.player)
                        #t = self.upgrade_card_sprites.sprites()[1]
                        #self.paused = False
                        self.remove_upgrade_cards()
                        
                    if event.key == pygame.K_2:
                        self.upgrade_card_sprites.sprites()[1].is_clicked(self.player)
                        #self.paused = False
                        self.remove_upgrade_cards()
                    if event.key == pygame.K_3:
                        self.upgrade_card_sprites.sprites()[2].is_clicked(self.player)
                        #self.paused = False
                        self.remove_upgrade_cards()              
             
                    
                    
                                        
            #player_camera.update(player, map_size_x, map_size_y)
            #self.health_bar.draw()
            if self.paused == False:
                self.time = self.clock.tick() / 1000
                self.trigger_upgrade_event()
                # player.draw(screen, player_camera)
                self.check_closest_enemy()
                self.spawn_enemies()
                self.check_player_collision_with_enemy()
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