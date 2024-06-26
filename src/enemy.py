import pygame

class Enemy(pygame.sprite.Sprite):
    # Enemy Class ist ähnlich wie die Player Klasse aufgebaut
    
    def __init__(self,pos, groups, image_path, player):
        super().__init__(groups)
        self.groups = groups        
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image.fill("red")
        self.rect = self.image.get_rect(center=pos)
        self.player_target = player
        self.speed= 200
        # verkleinere die Hitbox um 10 Pixel
        self.hitbox = self.rect.inflate(-10, -10)
        
    def move(self, time):
           # vector from enemy to player
        player_positon = pygame.Vector2(self.player_target.rect.center)
        own_position = pygame.Vector2(self.rect.center)
        self.direction = pygame.Vector2( player_positon - own_position)
        self.direction = self.direction.normalize() if self.direction else self.direction
        x = self.direction.x * self.speed 
        y = self.direction.y * self.speed 
        self.rect.x += self.direction.x * time * self.speed
        self.rect.y += self.direction.y * time * self.speed
        
    def update(self, time):
        #pass
        self.move(time)
    
    def check_collision_with_player(self):
        for obj in self.collision_objects:
            if obj.rect.colliderect(self.hitbox):
                print("Player collided with object")
                if xy == "x":
                    if self.direction.x > 0 : self.hitbox.right = obj.rect.left 
                    if self.direction.x < 0 : self.hitbox.left = obj.rect.right
                else:
                    if self.direction.y > 0 : self.hitbox.bottom = obj.rect.top
                    if self.direction.y < 0 : self.hitbox.top = obj.rect.bottom
           
