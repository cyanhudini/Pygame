import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self, image_path, camera):
        super().__init__(camera)
        self.direction = pygame.math.Vector2()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

    def getInput(self):
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        if keys[pygame.K_DOWN]:
            self.direction.y = 1
        if keys[pygame.K_UP]:
            self.direction.y = -1
    
    
    # TODO: check ob Ende der Karte erreicht
    def moveRight(self, pixels, map_size_x):
        # wenn png sprite über die Kartengrenze hinausgeht, dann setze es auf die Grenze
        self.direction.x = 1
        if self.x + self.image.get_width() > map_size_x:
            self.x = map_size_x - self.image.get_width()
         
    def moveLeft(self, pixels, map_size_x):
        
        self.direction.x = -1
        if self.x < 0:
            self.x = 0
            
    def moveUp(self, pixels, map_size_y):
        
        self.direction.y = -1
        if self.y < 0:
            self.y = 0
        
    def moveDown(self, pixels, map_size_y):
        self.direction.y = 1
        if self.y + self.image.get_height() > map_size_y:
            self.y = map_size_y - self.image.get_height()
        
    def update_player(self):
        self.getInput()
        self.rect.center += self.direction * 2
        

  # all_sprites_list = pygame.sprite.Group()

  # object_ = Sprite(Red, 20, 30)
  # object_.rect.x = 200
  # object_.rect.y = 300

  # all_sprites_list.add(object_)

  #
 
  #if keys get pressed do the following
    #  keys = pygame.key.get_pressed()
    #  if keys[pygame.K_LEFT]:
    #     playerChar.moveLeft(10)
    #  if keys[pygame.K_RIGHT]:
    #     playerChar.moveRight(10)
    #  if keys[pygame.K_DOWN]:
    #     playerChar.moveBack(10)
    #  if keys[pygame.K_UP]:
    #     playerChar.moveForward(10)

  
    #  all_sprites_list.update()

