import pygame

class Upgrade(pygame.sprite.Sprite):
    def __init__(self, groups, pos, upgrade_type, sprite_paths):
        super().__init__(groups)
        # self.rect = pygame.Rect(400, 400, 30, 100)
        self.card_position = (pos[0], pos[1])
        self.image =  pygame.image.load(sprite_paths[upgrade_type]).convert_alpha()
        self.rect = self.image.get_rect(center=self.card_position)
        self.upgrade_type = upgrade_type
        
        
        
    def update(self, time):
        pass

    def is_clicked(self, player ):
        match self.upgrade_type:
            case "health":
                player.current_health += 10
            case "defense":
                player.defense_mutliplier += 0.1
            case "dmg":
                player.damage_multiplier += 0.1
            