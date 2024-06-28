import pygame
import spritesheet
import math
class Enemy(pygame.sprite.Sprite):
    # Enemy Class ist ähnlich wie die Player Klasse aufgebaut
    
    def __init__(self,pos, groups, player, collision_objects, health, sprites):
        super().__init__(groups)
        self.groups = groups        
        
        # select the first sprite from the folder "down" and the first sprite
        #
        self.sprites = sprites
        self.image =self.sprites["down"][0] #anfänglicher Sprite
        self.rect = self.image.get_rect(center=pos)
        self.player_target = player
        self.speed= 100
        self.direction = pygame.math.Vector2()
        # verkleinere die Hitbox um 10 Pixel
        self.hitbox = self.rect.inflate(-10, -10)
        self.collision_objects = collision_objects
        self.health= health
        self.sprites = sprites
        self.animation_index = 0
        self.animation_speed = 0.1
        
        # (64 x 585- 645) * 5
    
    
    def check_if_distance_is_zero(self, target_pos, self_pos):
        # check if the distance between the player and the enemy is zero
        distance = math.sqrt((target_pos[0] - self_pos[0])**2 + (target_pos[1] - self_pos[1])**2)
        if distance == 0:
            return pygame.math.Vector2(0,0)
        else:
            return ((target_pos - self_pos).normalize())
            
        
        
    
    def move(self,time):
        # genau die gleiche Methode wie bei Player
        target_position = pygame.math.Vector2(self.player_target.rect.center)
        self_position = pygame.math.Vector2(self.rect.center)
        
        self.direction = self.check_if_distance_is_zero(target_position, self_position)
        
        self.hitbox.x += self.direction.x * self.speed * time
        self.check_collision_with_objects("x")
        self.hitbox.y += self.direction.y * self.speed * time
        self.check_collision_with_objects("y")
        self.rect.center = self.hitbox.center
        
    def update(self, time):
        #pass
        self.move(time)
        self.animate_sprites()
    def animate_sprites(self):
        # if direction is up
        if self.direction.y < 0:
            self.himmelsrichtung = "up"
            self.image = (self.sprites[self.himmelsrichtung][math.floor(self.animation_index)]).convert_alpha()
            self.animation_index += self.animation_speed
            # wie schnell wird die Animation durchgeführt
            if self.animation_index >= len(self.sprites)- 1:
                self.animation_index = 0
        if self.direction.y > 0:
            self.himmelsrichtung = "down"
            self.image =self.sprites[self.himmelsrichtung][math.floor(self.animation_index)].convert_alpha()
            self.animation_index += self.animation_speed
            if self.animation_index >= len(self.sprites)-1:
                self.animation_index = 0
        if self.direction.x < 0:
            self.himmelsrichtung = "left"
            self.image =self.sprites[self.himmelsrichtung][math.floor(self.animation_index)].convert_alpha()
            self.animation_index += self.animation_speed
            if self.animation_index >= len(self.sprites)-1:
                self.animation_index = 0
        if self.direction.x > 0:
            self.himmelsrichtung = "right"
            self.image = self.sprites[self.himmelsrichtung][math.floor(self.animation_index)].convert_alpha()
            self.animation_index += self.animation_speed
            if self.animation_index >= len(self.sprites)-1:
                self.animation_index = 0
        
    
    def check_collision_with_objects(self, xy):
        for obj in self.collision_objects:
            if obj.rect.colliderect(self.hitbox):
                #print("Player collided with object")
                if xy == "x":
                    if self.direction.x > 0 : self.hitbox.right = obj.rect.left 
                    if self.direction.x < 0 : self.hitbox.left = obj.rect.right
                else:
                    if self.direction.y > 0 : self.hitbox.bottom = obj.rect.top
                    if self.direction.y < 0 : self.hitbox.top = obj.rect.bottom
           
