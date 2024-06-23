import pygame

# Global variables
SURFACE_COLOR = ( 0, 0, 0)
WIDTH = 100
HEIGHT = 100

  #OBJECT CLASS
class Sprite(pygame.sprite.Sprite):
    def __init__(self, height, width):
        super().__init__()

        self.image =pygame.Surface([width, height])
        self.image = pygame.image.load('Pygame\player\walking\down.png')
        self.image.set_colorkey((0,0,0))

        pygame.draw.rect(self.image,
                        SURFACE_COLOR,
                        pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()

    def moveRight (self, pixels):
        self.rect.x += pixels
    def moveLeft (self, pixels):
        self.rect.x -= pixels
    def moveForward(self, pixels):
        self.rect.y -= pixels
    def moveBack(self, pixels):
        self.rect.y += pixels

#Sprite Gruppe erstellen
all_sprites_list = pygame.sprite.Group()

object_ = Sprite('Pygame\player\walking\down.png', 20, 30)
object_.rect.x = 200
object_.rect.y = 300

all_sprites_list.add(object_)

  # auskommentiert, da bereits in main.py
  # #if keys get pressed do the following
#keys = pygame.key.get_pressed()
#if keys[pygame.K_LEFT]:
 #        playerChar.moveLeft(10)
#if keys[pygame.K_RIGHT]:
 #        playerChar.moveRight(10)
#if keys[pygame.K_DOWN]:
 #        playerChar.moveBack(10)
#if keys[pygame.K_UP]:
 #        playerChar.moveForward(10)
         
all_sprites_list.update()

