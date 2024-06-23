import pygame

# Global variables
COLOR = (167, 255, 100)
SURFACE:COLOR = ( 0, 0, 0)
WIDTH = 100
HEIGHT = 100


#OBJECT CLASS
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
       self.x = x
       self.y = y
       self.image = pygame.image.load(image_path)

    # TODO: check ob Ende der Karte erreicht
    def moveRight(self, pixels, map_size_x):
        # wenn png sprite über die Kartengrenze hinausgeht, dann setze es auf die Grenze
           self.x += pixels
    if  self.x + self.image.get_width() > map_size_x:
         self.x = map_size_x - self.image.get_width()
        
    def moveLeft(self, pixels, map_size_x):
        
        self.x -= pixels
        if self.x < 0:
            self.x = 0
            
    def moveUp(self, pixels, map_size_y):
        
        self.y -= pixels
        if self.y < 0:
            self.y = 0
        
    def moveDown(self, pixels, map_size_y):
        self.y += pixels
        if self.y + self.image.get_height() > map_size_y:
            self.y = map_size_y - self.image.get_height()
        
        
    def draw(self, screen, camera):
        screen_x = self.x - camera.x
        screen_y = self.y - camera.y
        screen.blit(self.image, (screen_x, screen_y))
        

all_sprites_list = pygame.sprite.Group()

object_ = Sprite(Red, 20, 30)
object_.rect.x = 200
object_.rect.y = 300

all_sprites_list.add(object_)

 
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

