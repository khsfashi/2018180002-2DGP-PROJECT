from pico2d import *

# 1 == Red, 2 == Green, 3 == Blue, 5 == Red + Green, 6 == Red + Blue, 7 == Green + Blue

class Gate:
    GATE_WIDTH = 32
    GATE_HEIGHT = 32

    def __init__(self):
        self.x = 0
        self.y = 0
        self.isDraw = False
        self.color = 0
        self.image_R = load_image('Resource\\Object\\Gate_Red.png')
        self.image_G = load_image('Resource\\Object\\Gate_Green.png')
        self.image_B = load_image('Resource\\Object\\Gate_Blue.png')
        self.image_Y = load_image('Resource\\Object\\Gate_Red+Green.png')
        self.image_C = load_image('Resource\\Object\\Gate_Red+Blue.png')
        self.image_M = load_image('Resource\\Object\\Gate_Green+Blue.png')

    def draw(self):
        if self.isDraw:
            if self.color == 1:
                self.image_R.clip_draw(0, 0, Gate.GATE_WIDTH, Gate.GATE_HEIGHT, self.x, self.y, 32, 32)
            elif self.color == 2:
                self.image_G.clip_draw(0, 0, Gate.GATE_WIDTH, Gate.GATE_HEIGHT, self.x, self.y, 32, 32)
            elif self.color == 3:
                self.image_B.clip_draw(0, 0, Gate.GATE_WIDTH, Gate.GATE_HEIGHT, self.x, self.y, 32, 32)
            elif self.color == 5:
                self.image_Y.clip_draw(0, 0, Gate.GATE_WIDTH, Gate.GATE_HEIGHT, self.x, self.y, 32, 32)
            elif self.color == 6:
                self.image_C.clip_draw(0, 0, Gate.GATE_WIDTH, Gate.GATE_HEIGHT, self.x, self.y, 32, 32)
            elif self.color == 7:
                self.image_M.clip_draw(0, 0, Gate.GATE_WIDTH, Gate.GATE_HEIGHT, self.x, self.y, 32, 32)