import pygame
import random
from player import Player
from greendots import GreenDot
from camera import Camera

def draw_test_dots(screen, map_size_x, map_size_y):
    
    radius = 5
    num_dots = 1000
    draw_dots = []
    for _ in range(num_dots):
        coord_x = random.randint(0, map_size_x -1)
        coord_y = random.randint(0, map_size_y -1)
        draw_dots.append(GreenDot(coord_x, coord_y, radius))
    return draw_dots
    

def main():
    pygame.init()

    screen_width = 800
    screen_height = 600
    map_size_x = 10000
    map_size_y = 10000
    screen = pygame.display.set_mode((screen_width, screen_height))


    pygame.display.set_caption("Player Movement")

    # assets wie Sprite PNG's müsste man in einen extra Ordner machen
    player_image_path = "player.png"  # Replace with your image path

    player_camera = Camera(screen_width, screen_height)
    player = Player(10, 10, player_image_path)
    draw_test_dots(screen,map_size_x, map_size_y)

    canvas = pygame.Surface((map_size_x, map_size_y))
    canvas.fill((0, 0, 255))
    rect = canvas.get_rect()
    test_green_dots = draw_test_dots(screen, map_size_x, map_size_y)
    
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
        player_camera.update(player, map_size_x, map_size_y)
        canvas.fill((0, 0, 255))
        screen.fill((255, 255, 255))
        screen.blit(canvas, (screen_width, screen_height))
        for dot in test_green_dots:
            dot.draw(screen)

        player.draw(screen, player_camera)

        pygame.display.flip()

pygame.quit()

if __name__ == "__main__":
  main()
