

class Weapon (pygame.sprite.Sprite):
    def __init__(self, player, groups ):
        self.player = player
        self.distance = 140

    #sprite setup
    super ().__init__(groups)
    self.weapon.surf = pygame.image.load(image_path) 