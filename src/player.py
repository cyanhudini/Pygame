import pygame
import math
class Player(pygame.sprite.Sprite):
    def __init__(self, player_sprites, groups, collision_objects, pos):
        # mit superklasse übernimmt Player auch die Methode von Sprite
        # wie z.B. update()
        
        super().__init__(groups)
        self.starting_position = pos
        self.player_sprites = player_sprites
        self.image = self.player_sprites["down"][0]
        self.direction = pygame.math.Vector2()
        self.himmelsrichtung = "down"
        # self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=self.starting_position)
        self.speed = 500
        self.collision_objects = collision_objects
        self.animation_index = 0
        self.animation_speed = 0.1
        self.hitbox = self.rect.inflate(-10, -10)
        self.shooting_mode = "single"
        
    def getInput(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT]) # wenn pygame.K_RIGHT true ist, dann 1, sonst 0, also 1-0 = 1, wenn pygame.K_LEFT true ist, dann 1, sonst 0, also 0-1 = -1
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        
    def move(self, time):
        self.hitbox.x += self.direction.x * self.speed * time
        self.check_hitbox_of_player_with_objects("x")
        self.hitbox.y += self.direction.y * self.speed * time
        self.check_hitbox_of_player_with_objects("y")
        self.rect.center = self.hitbox.center
    
    def animate_sprites(self):
        current_animation_sprite = (self.player_sprites[self.himmelsrichtung])
        print("animation_index", self.animation_index)  
        if self.direction.y < 0:
            self.himmelsrichtung = "up"
            self.image = current_animation_sprite[(math.floor(self.animation_index))].convert_alpha()
            self.animation_index += self.animation_speed
            # wie schnell wird die Animation durchgeführt
            if self.animation_index >= len(current_animation_sprite)-1:
                self.animation_index = 0
        if self.direction.y > 0:
            self.himmelsrichtung = "down"
            self.image =current_animation_sprite[(math.floor(self.animation_index))].convert_alpha()
            self.animation_index += self.animation_speed
            if self.animation_index >= len(current_animation_sprite)-1:
                self.animation_index = 0
        if self.direction.x < 0:
            self.himmelsrichtung = "left"
            self.image =current_animation_sprite[(math.floor(self.animation_index))].convert_alpha()
            self.animation_index += self.animation_speed
            if self.animation_index >= len(current_animation_sprite)-1:
                self.animation_index = 0
        if self.direction.x > 0:
            self.himmelsrichtung = "right"
            self.image = current_animation_sprite[(math.floor(self.animation_index))].convert_alpha()
            self.animation_index += self.animation_speed
            if self.animation_index >= len(current_animation_sprite)-1:
                self.animation_index = 0
    
    def update(self, time):
        self.getInput()
        self.move(time)
        self.animate_sprites()
        # self.check_hitbox_of_player_with_objects()
        self.rect.center += self.direction * self.speed * time

    def check_hitbox_of_player_with_objects(self, xy):
        # check whether player collides with objects
        for obj in self.collision_objects:
            if obj.rect.colliderect(self.hitbox):
                #print("Player collided with object")
                if xy == "x":
                    if self.direction.x > 0 : self.hitbox.right = obj.rect.left 
                    if self.direction.x < 0 : self.hitbox.left = obj.rect.right
                else:
                    if self.direction.y > 0 : self.hitbox.bottom = obj.rect.top
                    if self.direction.y < 0 : self.hitbox.top = obj.rect.bottom
                
                