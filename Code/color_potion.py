from pico2d import *

# 1 == Red, 2 == Green, 3 == Blue, 0 == Black, 4 == White

class Potion:
    POTION_WIDTH = 32
    POTION_HEIGHT = 32

    def __init__(self):
        self.x = 0
        self.y = 0
        self.isDraw = False
        self.color = 0
        self.image_N = load_image('Resource\\Object\\Potion_Black.png')
        self.image_R = load_image('Resource\\Object\\Potion_Red.png')
        self.image_G = load_image('Resource\\Object\\Potion_Green.png')
        self.image_B = load_image('Resource\\Object\\Potion_Blue.png')
        self.image_W = load_image('Resource\\Object\\Potion_White.png')

    def draw(self):
        if self.isDraw:
            if self.color == 0:
                self.image_N.clip_draw(0, 0, Potion.POTION_WIDTH, Potion.POTION_HEIGHT, self.x, self.y, 32, 32)
            elif self.color == 1:
                self.image_R.clip_draw(0, 0, Potion.POTION_WIDTH, Potion.POTION_HEIGHT, self.x, self.y, 32, 32)
            elif self.color == 2:
                self.image_G.clip_draw(0, 0, Potion.POTION_WIDTH, Potion.POTION_HEIGHT, self.x, self.y, 32, 32)
            elif self.color == 3:
                self.image_B.clip_draw(0, 0, Potion.POTION_WIDTH, Potion.POTION_HEIGHT, self.x, self.y, 32, 32)
            elif self.color == 4:
                self.image_W.clip_draw(0, 0, Potion.POTION_WIDTH, Potion.POTION_HEIGHT, self.x, self.y, 32, 32)
