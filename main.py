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
    camera = Camera(800, 600)

    pygame.display.set_caption("Player Movement")

    # assets wie Sprite PNG's müsste man in einen extra Ordner machen
    player_image_path = "r.png"  # Replace with your image path

    player_camera = Camera(screen_width, screen_height)
    player = Player(player_image_path, player_camera)
    draw_test_dots(screen,map_size_x, map_size_y)

   
    test_green_dots = draw_test_dots(screen, map_size_x, map_size_y)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #player_camera.update(player, map_size_x, map_size_y)

        screen.fill((255, 255, 255))
        for dot in test_green_dots:
            dot.draw(screen)
        player_camera.update()
        # player.draw(screen, player_camera)
        player_camera.draw_player(player)

        pygame.display.flip()

pygame.quit()

if __name__ == "__main__":
  main()
