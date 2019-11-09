import game_framework
from pico2d import *
import random


# state : 캐릭터의 움직임을 저장하는 전역 변수
# 0 : 아무것도 안 함, 1 : 오른쪽 움직임, -1 : 왼쪽 움직임, 2 : 문 열기
state = 0
Map_Size = [800, 450]
Tile_Size = [32, 32]
Character_Size = [32, 32]
jump = True
cnt = 0
name = "Stage1State"
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

def IntersectRect(interRect, rect1_left, rect1_top, rect1_right, rect1_bottom, rect2_left, rect2_top, rect2_right, rect2_bottom):
    vertical = False
    horizontal = False
    global jump

    if rect1_left <= rect2_right and rect1_right >= rect2_left:
        horizontal = True
        interRect[0] = max(rect1_left, rect2_left)
        interRect[2] = min(rect1_right, rect2_right)

    if rect1_top >= rect2_bottom and rect1_bottom <= rect2_top:
        vertical = True
        interRect[1] = min(rect1_top, rect2_top)
        interRect[3] = max(rect1_bottom, rect2_bottom)

    if vertical and horizontal:
        return True
    else:
        return False


class Map:
    def __init__(self):
        self.image = load_image('Resource\\BackGround\\Information_Room.png')

    def draw(self):
        self.image.clip_draw(0, 0, Map_Size[0], Map_Size[1], 400, 300, 800, 600)


class Tile:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        self.interRect = [0, 0, 0, 0]
        self.isDraw = False
        self.InterH = 0
        self.InterW = 0
        if Tile.image == None:
            Tile.image = load_image('Resource\\TileSet\\Lab_Tile.png')

    def draw(self):
        if self.isDraw:
            self.image.clip_draw(0, 0, Tile_Size[0], Tile_Size[1], self.x, self.y, 32, 32)

    def intersect(self):
        global jump
        if IntersectRect(self.interRect, self.x - 16, self.y + 16, self.x + 16, self.y - 16,
                         player.x - 10, player.y + 16, player.x + 10, player.y - 16):
            self.InterH = self.interRect[1] - self.interRect[3]
            self.InterW = self.interRect[2] - self.interRect[0]
            if self.InterW > self.InterH:
                if self.interRect[1] == self.y + 16:
                    player.y += self.InterH
                    jump = False
                elif self.interRect[3] == self.y - 16:
                    player.y -= self.InterH
            else:
                if self.interRect[0] == self.x - 16:
                    player.x -= self.InterW
                elif self.interRect[2] == self.x + 16:
                    player.x += self.InterW


class Player:
    def __init__(self):
        self.image = load_image('Resource\\Character\\Untitled1.png')
        self.x, self.y = 200, 200
        self.frame = 0
        self.dir = 0
        self.acceleration = 0

    def update(self):
        global state
        global jump
        # 방향 정하기
        if state == 0:
            self.frame = 0
        elif state == 1:
            self.dir = 0
        elif state == -1:
            self.dir = 1
        if jump == True:
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
        if jump == True:
            self.y += self.acceleration
            self.acceleration -= 1

    def draw(self):
        self.image.clip_draw(self.frame * 32, self.dir * 32, 32, 32, self.x, self.y)


def enter():
    global map, player, background
    background = Map()
    player = Player()
    map = [[Tile() for j in range(0, 25)] for i in range(0, 19)]
    for i in range(0, 19):
        for j in range(0, 25):
            map[i][j].x = j * 32 + 16
            map[i][j].y = (18 - i) * 32 + 16
            if tile_Setting[i][j] == '■':
                map[i][j].isDraw = True


def exit():
    global map, player, background
    del(background)
    del(player)
    del(map)


def pause():
    pass


def resume():
    pass


def handle_events():
    global running
    global state
    global jump

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
                jump = True
                player.acceleration = 10
        # 키 뗄시 캐릭터 멈춤
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT and state == -1:
                state = 0
            elif event.key == SDLK_RIGHT and state == 1:
                state = 0


def update():
    global jump
    global cnt
    player.update()
    # 충돌체크
    for i in range(0, 19):
        for j in range(0, 25):
            if map[i][j].isDraw == True:
                map[i][j].intersect()
                if IntersectRect(map[i][j].interRect, map[i][j].x - 16, map[i][j].y + 16, map[i][j].x + 16,
                                 map[i][j].y - 16, player.x - 10, player.y + 16, player.x + 10, player.y - 16):
                    cnt = 1
    if cnt == 0:
        if jump == False:
            player.acceleration = 0
        jump = True
    else:
        cnt = 0

def draw():
    clear_canvas()
    background.draw()
    for i in range(0, 19):
        for j in range(0, 25):
            map[i][j].draw()
    player.draw()
    update_canvas()
    delay(0.05)
