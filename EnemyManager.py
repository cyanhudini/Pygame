import pygame
import random
from enemy import Enemy

RED = (255, 0, 0)
WIDTH = 800
HEIGHT = 600

# ENEMY_SPAWN_TIME = 3000  # Zeit in Millisekunden, bis ein neuer Gegner erscheint -- in die main datei hinzufügen
class EnemyManager:
    def __init__(self, spawn_time, all_sprites_list):
        self.spawn_time = spawn_time
        self.all_sprites_list = all_sprites_list
        pygame.time.set_timer(pygame.USEREVENT, self.spawn_time)

    def spawn_enemy(self):
        enemyChar = Enemy(RED, 50, 50)
        enemyChar.rect.x = random.randint(0, WIDTH - 50)
        enemyChar.rect.y = random.randint(0, HEIGHT - 50)
        self.all_sprites_list.add(enemyChar)
