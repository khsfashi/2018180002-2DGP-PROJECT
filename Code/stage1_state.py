import game_framework
from pico2d import *
from background import Background
import random

# 상수 모음
MAX_TILE_WIDTH = 25
MAX_TILE_HEIGHT = 19
TILE_WIDTH = 32
TILE_HEIGHT = 32
CHARACTER_WIDTH = 32
CHARACTER_HEIGHT = 32
name = "Stage1State"

# state : 캐릭터의 움직임을 저장하는 전역 변수
# 0 : 아무것도 안 함, 1 : 오른쪽 움직임, -1 : 왼쪽 움직임, 2 : 문 열기
state = 0

jumping = True
cnt = 0

tile_Setting = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '■', '■', '■', 0, 0, 0, 0],
                [0, '■', 0, 0, 0, 0, 0, 0, 0, 0, 0, '■', '■', '■', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, '■', 0, 0, 0, '■', '■', '■', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, '■', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]

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
    image = None

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
            self.image.clip_draw(0, 0, TILE_WIDTH, TILE_HEIGHT, self.x, self.y, 32, 32)

    def update(self, terra):
        global jumping
        if intersected_rectangle(self.collided_Rect, self.x - 16, self.y + 16, self.x + 16, self.y - 16,
                                 terra.x - 10, terra.y + 16, terra.x + 10, terra.y - 16):
            self.collided_Rect_Height = self.collided_Rect[1] - self.collided_Rect[3]
            self.collided_Rect_Width = self.collided_Rect[2] - self.collided_Rect[0]

            if self.collided_Rect_Width > self.collided_Rect_Height:
                if self.collided_Rect[1] == self.y + 16:
                    terra.y += self.collided_Rect_Height
                    jumping = False
                elif self.collided_Rect[3] == self.y - 16:
                    terra.y -= self.collided_Rect_Height
            else:
                if self.collided_Rect[0] == self.x - 16:
                    terra.x -= self.collided_Rect_Width
                elif self.collided_Rect[2] == self.x + 16:
                    terra.x += self.collided_Rect_Width


class Terra:
    def __init__(self):
        self.image = load_image('Resource\\Character\\Untitled1.png')
        self.x, self.y = 200, 200
        self.frame = 0
        self.dir = 0
        self.acceleration = 0

    def update(self):
        global state
        global jumping
        # 방향 정하기
        if state == 0:
            self.frame = 0
        elif state == 1:
            self.dir = 0
        elif state == -1:
            self.dir = 1
        if jumping == True:
            self.frame = 1

        # 애니메이션
        if state == 1 or state == -1:
            self.frame = (self.frame + 1) % 3

        # 움직임
        if state == 1 or state == -1:
            if self.dir == 0:
                self.x += 4
            elif self.dir == 1:
                self.x -= 4

        # 점프
        if jumping == True:
            self.y += self.acceleration
            self.acceleration -= 1

    def draw(self):
        self.image.clip_draw(self.frame * 32, self.dir * 32, CHARACTER_WIDTH, CHARACTER_HEIGHT, self.x, self.y)


def enter():
    global map, terra, background
    background = Background()
    terra = Terra()
    map = [[Tile() for j in range(MAX_TILE_WIDTH)] for i in range(MAX_TILE_HEIGHT)]
    for i in range(MAX_TILE_HEIGHT):
        for j in range(MAX_TILE_WIDTH):
            map[i][j].x = j * TILE_WIDTH + (TILE_WIDTH / 2)
            map[i][j].y = (18 - i) * TILE_HEIGHT + (TILE_HEIGHT / 2)
            if tile_Setting[i][j] == '■':
                map[i][j].isDraw = True


def exit():
    global map, terra, background
    del(terra)
    del(map)
    del(background)

def pause():
    pass


def resume():
    pass


def handle_events():
    global running
    global state
    global jumping

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        # 키 누를시 캐릭터 이동
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                state = -1
            elif event.key == SDLK_RIGHT:
                state = 1
            elif event.key == SDLK_SPACE:
                jumping = True
                terra.acceleration = 10
        # 키 뗄시 캐릭터 멈춤
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT and state == -1:
                state = 0
            elif event.key == SDLK_RIGHT and state == 1:
                state = 0


def update():
    global jumping
    global cnt
    terra.update()
    # 충돌체크
    for i in range(MAX_TILE_HEIGHT):
        for j in range(MAX_TILE_WIDTH):
            if map[i][j].isDraw == True:
                map[i][j].update(terra)
                if intersected_rectangle(map[i][j].collided_Rect, map[i][j].x - 16, map[i][j].y + 16, map[i][j].x + 16,
                                 map[i][j].y - 16, terra.x - 10, terra.y + 16, terra.x + 10, terra.y - 16):
                    cnt = 1
    if cnt == 0:
        if jumping == False:
            terra.acceleration = 0
        jumping = True
    else:
        cnt = 0

def draw():
    clear_canvas()
    background.draw()
    for i in range(MAX_TILE_HEIGHT):
        for j in range(MAX_TILE_WIDTH):
            map[i][j].draw()
    terra.draw()
    update_canvas()
    delay(0.05)
