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

          self.image =pygmae.Surface([width, height])
          self.image.fill(SURFACE:COLOR)
          self.image.set__colorkey(COLOR)

          pygame.draw.rect(self.image,
                           color,
                           pygmae.Rect(0, 0, width, height))
          self.rect = self.image.get_rect()
# Moving
    def moveRight (self, pixels):
        self.rect.x += pixels

    def moveLeft (self, pixels):
        self.rect.x += pixels
    def moveForward(self, pixels):
        self.rect.y -= speed * speed/10
    def moveBack(self, speed):
        self.rect.y -= speed * speed/10

  pygame.init()

  RED = (255, 0, 0)

  size = (WIDTH, HEIGHT)
  screen = pygame.display.set_mode(size)
  pygmae.display.set_caption("Creating Sprite")

  all_sprites_list = pygame.sprite.Group()

  object_ = Sprite(Red, 20, 30)
  object_.rect.x = 200
  object_.rect.y = 300

  all_sprites_list.add(object_)

  exit = True
  clock = pygame.time.Clock()

  while exit:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              exit = False
          elif event.type == pygame.Keydown:
              if event.key == pygame.K_x:
                 exit = False
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
      screen.fill(SURFACE_COLOR)
      all_sprites_list.draw(screen)
      pygame.display.flip()
      clock.tick(60)
  pygame.quit()

