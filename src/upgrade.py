import pygame

class Upgrade(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        # self.rect = pygame.Rect(400, 400, 30, 100)
        self.card_position = (pos[0], pos[1])
        self.image =  pygame.image.load("/".join(["player", "upgrade", "upgrade_dmg.png"]))
        self.rect = self.image.get_rect(center=self.card_position)

        self.possible_upgrades = {
            "dmg": 0.1,
            "defense": 0.1,
            "health": 10
        }
        
    def update(self, time):
        pass
    def is_upgrade_chosen(self):
        
        pass
    
    