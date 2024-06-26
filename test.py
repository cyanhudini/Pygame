import sys
import math
import os
import pygame
import spritesheet

def load_animation_sprites_walking_direction():
    enemy_sprites_base = "/".join(['enemy'])
    #files = [f for f in os.listdir(enemy_sprites_base) if f.endswith(".png")]
    # da Namen mit Zahlen beginnen kann man easy sortieren
    # lambda ist eine anonyme Funktion, nach Split für 1.png: split[0] = "1" und split[1] = "png"
    #files.sort(key = lambda x: int(x.split(".")[0]))
    spritesheet1 = spritesheet.Spritesheet()
    #spritesheet = pygame.image.load("/".join([enemy_sprites_base,"1", "franky_all.png"])).convert_alpha()
    #enemy_sprites_base = os.path("/".join(["enemy"]))
    folders = list(os.walk(enemy_sprites_base))[0][1]
    for folder in folders:
        print("folder: ", folder)
        # if folder ==
    
        for folder_path, sub_folders, files in os.walk("/".join([enemy_sprites_base, folder])):
            print("folder_path: ", folder_path)
            print("sub_folders: ", sub_folders)
            print("files: ", files)
            # print index of "down"
            #index = sub_folders.index('down')
            print("sub_folders: ", sub_folders)
            #print("files: ", files)
                #print("sub_folder: ", sub_folder)
                #print(sorted(sub_folder["down"], key = lambda name: int(name.split(".")[0]))[0])
              
            
if __name__ == "__main__":
    load_animation_sprites_walking_direction()