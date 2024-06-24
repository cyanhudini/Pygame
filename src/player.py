import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self, image_path, groups, collision_objects, pos):
        # mit superklasse übernimmt Player auch die Methode von Sprite
        # wie z.B. update()
        
        super().__init__(groups)
        self.pos = pos
        self.direction = pygame.math.Vector2()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=self.pos)
        self.speed = 500
        self.collision_objects = collision_objects
    def getInput(self):
        print(self.pos)
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT]) # wenn pygame.K_RIGHT true ist, dann 1, sonst 0, also 1-0 = 1, wenn pygame.K_LEFT true ist, dann 1, sonst 0, also 0-1 = -1
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        
    def update(self, time):
        self.getInput()
        self.check_hitbox_of_player_with_objects()
        self.rect.center += self.direction * self.speed * time
    
    def calculate_shooting_direction():
        # schieße entweder in die Richtung des nächsten Gegners oder in die Laufrichtung
        
        pass
    def check_hitbox_of_player_with_objects(self):
        # check whether player collides with objects
        for obj in self.collision_objects:
            if obj.rect.colliderect(self.rect):
                print("Player collided with object")
                #if self.direction.x > 0 and self.rect.right > obj.rect.left: self.direction.x = 0
                #elif self.direction.x < 0 and self.rect.left < obj.rect.right: self.direction.x = 0
                #elif self.direction.y > 0 and self.rect.bottom > obj.rect.top: self.direction.y = 0
                #elif self.direction.y < 0 and self.rect.top < obj.rect.bottom: self.direction.y = 0
                
                if self.direction.y > 0:
                    self.rect.bottom = obj.rect.top
                    #self.pos.y = obj.rect.top
                elif self.direction.y < 0:
                    self.rect.top = obj.rect.bottom
                    #self.pos.y = obj.rect.bottom
                elif self.direction.x > 0:
                    self.rect.right = obj.rect.left
                    #self.pos.x = obj.rect.left
                elif self.direction.x < 0:
                    self.rect.left = obj.rect.right
                    #self.pos.x = obj.rect.right
                
    def zweite_methode(self):
        # for ob in collision object:
        # if collide_rect(self, ob):
        #   if obj.x.left = self.x.right:
        #       self.direction.x = 0
        #   if obj.x.right = self.x.left:
        #       self.direction.x = 0
        #   if obj.y.top = self.y.bottom:
        #       self.direction.y = 0
        pass
                