from pico2d import *

def intersected_rectangle(collided_Rect, rect1_left, rect1_top, rect1_right, rect1_bottom,
                          rect2_left, rect2_top, rect2_right, rect2_bottom):
    vertical = False
    horizontal = False
    global jumping

    if rect1_left <= rect2_right and rect1_right >= rect2_left:
        horizontal = True
        collided_Rect[0] = max(rect1_left, rect2_left)
        collided_Rect[2] = min(rect1_right, rect2_right)

    if rect1_top >= rect2_bottom and rect1_bottom <= rect2_top:
        vertical = True
        collided_Rect[1] = min(rect1_top, rect2_top)
        collided_Rect[3] = max(rect1_bottom, rect2_bottom)

    if vertical and horizontal:
        return True
    else:
        return False

class Tile:
    # 상수
    image = None
    TILE_WIDTH = 32
    TILE_HEIGHT = 32

    def __init__(self):
        self.x = 0
        self.y = 0
        self.collided_Rect = [0, 0, 0, 0]
        self.isDraw = False
        self.collided_Rect_Height = 0
        self.collided_Rect_Width = 0
        if Tile.image == None:
            Tile.image = load_image('Resource\\TileSet\\Lab_Tile.png')

    def draw(self):
        if self.isDraw:
            self.image.clip_draw(0, 0, Tile.TILE_WIDTH, Tile.TILE_HEIGHT, self.x, self.y, 32, 32)

    def update(self, terra):
        if intersected_rectangle(self.collided_Rect, self.x - 16, self.y + 16, self.x + 16, self.y - 16,
                                 terra.x - 10, terra.y + 16, terra.x + 10, terra.y - 16):
            self.collided_Rect_Height = self.collided_Rect[1] - self.collided_Rect[3]
            self.collided_Rect_Width = self.collided_Rect[2] - self.collided_Rect[0]

            if self.collided_Rect_Width > self.collided_Rect_Height:
                if self.collided_Rect[1] == self.y + 16:
                    terra.y += self.collided_Rect_Height
                    terra.jumping = False
                elif self.collided_Rect[3] == self.y - 16:
                    terra.y -= self.collided_Rect_Height
            else:
                if self.collided_Rect[0] == self.x - 16:
                    terra.x -= self.collided_Rect_Width
                elif self.collided_Rect[2] == self.x + 16:
                    terra.x += self.collided_Rect_Width