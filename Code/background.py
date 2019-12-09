from pico2d import *

class Background:
    # 상수
    MAP_WIDTH = 800
    MAP_HEIGHT = 450

    def __init__(self):
        self.image = load_image('Resource\\BackGround\\Information_Room.png')
        self.bgm = load_music('Resource\\Sounds\\Background_Music.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def draw(self):
        self.image.clip_draw(0, 0, Background.MAP_WIDTH, Background.MAP_HEIGHT, 400, 300, 800, 600)
