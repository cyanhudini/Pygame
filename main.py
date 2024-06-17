import pygame
from player import Player


def main():
  
    pygame.init()


    screen_width = 800
    screen_height = 600
    map_size_x = 800
    map_size_y = 1000
    screen = pygame.display.set_mode((screen_width, screen_height))


    pygame.display.set_caption("Player Movement")

    # assets wie Sprite PNG's müsste man in einen extra Ordner machen
    player_image_path = "player.png"  # Replace with your image path

    player_camera = Camera()
    player = Player(10, 10, player_image_path)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.moveLeft(5, map_size_x)
        if keys[pygame.K_RIGHT]:
            player.moveRight(5, map_size_x)
        if keys[pygame.K_DOWN]:
            player.moveDown(5, map_size_y)
        if keys[pygame.K_UP]:
            player.moveUp(5, map_size_y)

    
        screen.fill((255, 255, 255))  

        player.draw(screen)

        pygame.display.flip()

pygame.quit()

if __name__ == "__main__":
  main()
