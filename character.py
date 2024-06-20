import pygame

# Global variables
COLOR = (167, 255, 100)
SURFACE:COLOR = ( 0, 0, 0)
WIDTH = 100
HEIGHT = 100

  #OBJECT CLASS
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()

        self.image =pygame.Surface([width, height])
        self.image.fill(SURFACE:COLOR)
        self.image.set__colorkey(COLOR)

        pygame.draw.rect(self.image,
                        color,
                        pygmae.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()

    def moveRight (self, pixels):
        self.rect.x += pixels
    def moveLeft (self, pixels):
        self.rect.x -= pixels
    def moveForward(self, pixels):
        self.rect.y -= pixels
    def moveBack(self, speed):
        self.rect.y += pixels


  all_sprites_list = pygame.sprite.Group()

  object_ = Sprite(Red, 20, 30)
  object_.rect.x = 200
  object_.rect.y = 300

  all_sprites_list.add(object_)

  #
 
  #if keys get pressed do the following
      keys = pygame.key.get_pressed()
      if keys[pygame.K_LEFT]:
         playerChar.moveLeft(10)
      if keys[pygame.K_RIGHT]:
         playerChar.moveRight(10)
      if keys[pygame.K_DOWN]:
         playerChar.moveBack(10)
      if keys[pygame.K_UP]:
         playerChar.moveForward(10)

  
      all_sprites_list.update()

