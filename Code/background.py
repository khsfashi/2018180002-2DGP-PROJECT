from pico2d import *

class Background:
    # 상수
    MAP_WIDTH = 800
    MAP_HEIGHT = 450

    def __init__(self):
        self.image = load_image('Resource\\BackGround\\BackGround_Sheet.png')
        self.bgm = load_music('Resource\\Sounds\\Background_Music.mp3')
        self.bgm.set_volume(50)
        self.bgm.repeat_play()
        self.kind = 0

    def draw(self):
        self.image.clip_draw(self.kind * 800, 0, Background.MAP_WIDTH, Background.MAP_HEIGHT, 400, 300, 800, 600)
