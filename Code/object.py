from pico2d import *

# 1 == Red, 2 == Green, 3 == Blue, 5 == Red + Green, 6 == Red + Blue, 7 == Green + Blue
# 2 == gate, 1 == jump, 0 == turret

class Object:
    GATE_WIDTH = 32
    GATE_HEIGHT = 32
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        self.isDraw = False
        self.color = 0
        self.kind = 0
        if Object.image == None:
            Object.image = load_image('Resource\\Object\\Object_Sheet.png')


    def draw(self):
        if self.isDraw:
            self.image.clip_draw(self.color * 32, self.kind * 32, Object.GATE_WIDTH, Object.GATE_HEIGHT,
                                 self.x, self.y, 32, 32)