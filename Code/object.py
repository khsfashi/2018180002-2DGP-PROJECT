from pico2d import *
import tile

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
        self.attack_mode = False
        self.collided_Rect = [0, 0, 0, 0]
        self.collided_Rect_Height = 0
        self.collided_Rect_Width = 0
        if Object.image == None:
            Object.image = load_image('Resource\\Object\\Object_Sheet1.png')


    def draw(self):
        if self.isDraw:
            if self.kind == 0 and self.attack_mode == False:
                self.image.clip_draw(0, self.kind * 32, Object.GATE_WIDTH, Object.GATE_HEIGHT, self.x, self.y, 32, 32)
            else:
                self.image.clip_draw(self.color * 32, self.kind * 32, Object.GATE_WIDTH, Object.GATE_HEIGHT,
                                 self.x, self.y, 32, 32)

    def update(self, terra):
        if terra.color != self.color and self.kind == 2 and \
                tile.intersected_rectangle(self.collided_Rect, self.x - 16, self.y + 16, self.x + 16, self.y - 16,
                                 terra.x - 10, terra.y + 14, terra.x + 10, terra.y - 16):
            self.collided_Rect_Height = self.collided_Rect[1] - self.collided_Rect[3]
            self.collided_Rect_Width = self.collided_Rect[2] - self.collided_Rect[0]

            if self.collided_Rect_Width > self.collided_Rect_Height:
                if self.collided_Rect[1] == self.y + 16:
                    terra.y += self.collided_Rect_Height
                    terra.jumping = False
                elif self.collided_Rect[3] == self.y - 16:
                    terra.y -= self.collided_Rect_Height
                    terra.y -= 1
                    terra.acceleration = 0
            else:
                if self.collided_Rect[0] == self.x - 16:
                    terra.x -= self.collided_Rect_Width
                elif self.collided_Rect[2] == self.x + 16:
                    terra.x += self.collided_Rect_Width

    def get_bb(self):
        if self.kind:
            return self.x - 16, self.y - 16, self.x + 16, self.y - 6
        elif self.attack_mode:
            return self.x - 3, self.y - 13, self.x + 3, self.y + 13
        else:
            return self.x - 48, self.y - 16, self.x + 48, self.y + 16