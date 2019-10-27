from pico2d import *
import random
import game_framework

# state : 캐릭터의 움직임을 저장하는 전역 변수
# 0 : 아무것도 안 함, 1 : 오른쪽 움직임, -1 : 왼쪽 움직임, 2 : 문 열기
state = 0
Map_Size = [800, 450]
jump = False


class Map:
    def __init__(self):
        self.image = load_image('Resource\\BackGround\\Information_Room.png')

    def draw(self):
        self.image.clip_draw(0, 0, Map_Size[0], Map_Size[1], 400, 300, 800, 600)


class Player:
    def __init__(self):
        self.image = load_image('Resource\\Character\\Untitled1.png')
        self.x, self.y = 200, 200
        self.frame = 0
        self.dir = 0
        self.acceleration = 10

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
            if self.acceleration == -10:
                self.acceleration = 10
                jump = False
                if state != 1 and state != -1:
                    state = 0

    def draw(self):
        self.image.clip_draw(self.frame * 32, self.dir * 32, 32, 32, self.x, self.y)

def enter():
    global map, player
    map = Map()
    player = Player()
    pass


def exit():
    global map, player
    del(map)
    del(player)
    pass


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
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        # 키 누를시 캐릭터 이동
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                state = -1
            elif event.key == SDLK_RIGHT:
                state = 1
            elif event.key == SDLK_SPACE:
                jump = True
        # 키 뗄시 캐릭터 멈춤
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT and state == -1:
                state = 0
            elif event.key == SDLK_RIGHT and state == 1:
                state = 0

def update():
    player.update()
    pass


def draw():
    clear_canvas()
    map.draw()
    player.draw()
    update_canvas()
    delay(0.05)
    pass
