from pico2d import *

# 1 == Red, 2 == Green, 3 == Blue, 0 == Black, 4 == White
# 1 == potion, 0 = pipette

class Item:
    POTION_WIDTH = 32
    POTION_HEIGHT = 32
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        self.isDraw = False
        self.color = 0
        self.kind = 0
        if Item.image == None:
            Item.image = load_image('Resource\\Object\\Item_Sheet.png')

    def draw(self):
        if self.isDraw:
            self.image.clip_draw(self.color * 32, self.kind * 32, Item.POTION_WIDTH, Item.POTION_HEIGHT,
                                 self.x, self.y, 32, 32)

    def get_bb(self):
        return self.x - 10, self.y - 16, self.x + 10, self.y + 16