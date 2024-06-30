import pygame
import math
class Player(pygame.sprite.Sprite):
    def __init__(self, player_sprites, groups, collision_objects, pos, max_health):
        # mit superklasse übernimmt Player auch die Methode von Sprite
        # wie z.B. update()
        
        super().__init__(groups)
        self.pos = pos
        self.player_sprites = player_sprites
        self.image = self.player_sprites["down"][0]
        self.direction = pygame.math.Vector2()
        self.himmelsrichtung = "down"

        # self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=self.pos)
        self.speed = 500
        self.collision_objects = collision_objects
        self.animation_index = 0
        self.animation_speed = 0.15
        self.hitbox = self.rect.inflate(-10, -10)
        self.shooting_mode = "single"
        
        # damage
        self.damage_multiplier = 1
        self.base_damage = 10
        
        self.amount_defense_upgrade = 0
        
        # HEALTH
        self.max_health = 100
        self.current_health = self.max_health
        
        # EXP
        self.exp_to_level = 0
        self.total_exp = 0
        self.level = 1
        self.exp_progression_formula = self.total_exp * (1 + (self.level ** 0.5)) 
        self.base_experience_threshold = 70
        self.exp_threshold_factor = 1.8
        self.is_level_up = False
        
        self.status_bar_height = 5
        self.status_bar_width = 100
        
    
        self.health_bar_image = pygame.Surface((50, 50))
        self.health_bar_image.fill((255, 0, 0))
        self.rect = self.health_bar_image.get_rect(center=(400, 600))

  
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
        self.pos = self.rect.topleft
    
    def animate_sprites(self):
        current_animation_sprite = (self.player_sprites[self.himmelsrichtung])
          
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
    def draw_health_bar(self):
        pygame.draw.rect(self.image, "red", (0, 0,self.status_bar_width ,self.status_bar_height))     
        pygame.draw.rect(self.image, "green", (0, 0,self.status_bar_width * self.current_health / self.max_health, self.status_bar_height))
    def draw_experience_bar(self):
        pygame.draw.rect(self.image, "grey", (0, 5,self.status_bar_width ,self.status_bar_height))     
        pygame.draw.rect(self.image, "blue", (0, 5, (self.status_bar_width * self.exp_to_level / self.base_experience_threshold), self.status_bar_height))
    def gain_exp(self, experience):
        self.total_exp += experience
        self.exp_to_level += experience
        
        self.level_up()
    def level_up(self):
        
        # damit diie Level nicht "gehardcoded" werden müssen muss Level grenze dynamisch sein also mit einem Faktor * Level z.B
        # oder vorherige_exp_grenze * Level * Faktor (1.1)
        # dazu muss es mehr Gegner geben über Zeit
        # mit jedem Level up soll es Upgrades geben

       
        if self.exp_to_level >= self.base_experience_threshold:
           
            self.base_experience_threshold = self.total_exp * self.exp_threshold_factor
            print("diff", self.base_experience_threshold - self.total_exp)
            print("threshold", self.base_experience_threshold)
            print("exp to level", self.exp_to_level)
           
            self.exp_to_level = 0
            self.level += 1
            print("Level up")
            self.is_level_up = True   
            
        
    def update(self, time):
        self.getInput()
        self.move(time)
        self.animate_sprites()
        # self.check_hitbox_of_player_with_objects()
        self.rect.center += self.direction * self.speed * time
        self.draw_health_bar()
        self.draw_experience_bar()

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
                
                