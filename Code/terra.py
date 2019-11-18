from pico2d import *

class Terra:
    # 상수
    CHARACTER_WIDTH = 32
    CHARACTER_HEIGHT = 32

    def __init__(self):
        self.image = load_image('Resource\\Character\\Untitled1.png')
        self.x, self.y = 200, 200
        self.frame = 0
        self.dir = 0
        self.acceleration = 0
        self.jumping = False

    def update(self):
        # 방향 정하기
        if self.jumping:
            self.frame = 1

        # 애니메이션
        if self.dir == 1 or self.dir == -1:
            self.frame = (self.frame + 1) % 3

        # 움직임
        if self.dir == 1:
            self.x += 4
        elif self.dir == -1:
            self.x -= 4

        # 점프
        if self.jumping:
            self.y += self.acceleration
            if self.acceleration >= -10:
                self.acceleration -= 1

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame * 32, 0, Terra.CHARACTER_WIDTH, Terra.CHARACTER_HEIGHT, self.x, self.y)
        elif self.dir == -1:
            self.image.clip_draw(self.frame * 32, 32, Terra.CHARACTER_WIDTH, Terra.CHARACTER_HEIGHT, self.x, self.y)