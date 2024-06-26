import sys
import math
import os


def load_animation_sprites_walking_direction():
    enemy_sprites_base = "/".join(['enemy'])
    #files = [f for f in os.listdir(enemy_sprites_base) if f.endswith(".png")]
    # da Namen mit Zahlen beginnen kann man easy sortieren
    # lambda ist eine anonyme Funktion, nach Split für 1.png: split[0] = "1" und split[1] = "png"
    #files.sort(key = lambda x: int(x.split(".")[0]))
    folders = list(os.walk(enemy_sprites_base))[0][1]
    for folder in folders:
        
        print("sub_folder: ", folder)
            
            
if __name__ == "__main__":
    load_animation_sprites_walking_direction()