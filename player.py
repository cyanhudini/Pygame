import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self, image_path, groups, pos):
        # mit superklasse übernimmt Player auch die Methode von Sprite
        # wie z.B. update()
        
        super().__init__(groups)
        self.direction = pygame.math.Vector2()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=pos)
        self.speed = 200

    def getInput(self):
        
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
    
        
    def update(self, time):
        self.getInput()
        self.rect.center += self.direction * self.speed * time
        #print("update_player")  
        

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

