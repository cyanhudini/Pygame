class Camera:
    def __init__(self, screen_size_x, screen_size_y):
        self.x = 0
        self.y = 0
        self.camera_view_x = screen_size_x
        self.camera_view_y = screen_size_y
        
    def update(self, player, map_size_x, map_size_y):
        self.x = max(0, min(player.x - self.camera_view_x // 2, map_size_x - self.camera_view_x))
        self.y = max(0, min(player.y - self.camera_view_y // 2, map_size_y - self.camera_view_y))