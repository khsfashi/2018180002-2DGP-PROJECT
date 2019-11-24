import game_framework
from pico2d import *
from background import Background
from terra import Terra
from color_potion import Potion
import tile
import random

# 상수 모음
MAX_TILE_WIDTH = 25
MAX_TILE_HEIGHT = 19
TILE_WIDTH = 32
TILE_HEIGHT = 32
name = "Stage1State"

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
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'W', 0, 0, 0, 0, 0, 0, 0, '■', '■', '■', 0, 0, 0, 0],
                [0, '■', 0, 0, 0, 'N', 0, 0, 0, 0, 0, '■', '■', '■', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, '■', 0, 0, 0, '■', '■', '■', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, '■', 'R', 0, 0, 0, 0, 'G', 0, 0, 0, 0, 'B', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def enter():
    global map, terra, background, potion
    background = Background()
    terra = Terra()
    map = [[tile.Tile() for j in range(MAX_TILE_WIDTH)] for i in range(MAX_TILE_HEIGHT)]
    potion = [[Potion() for j in range(MAX_TILE_WIDTH)] for i in range(MAX_TILE_HEIGHT)]
    for i in range(MAX_TILE_HEIGHT):
        for j in range(MAX_TILE_WIDTH):
            map[i][j].x = j * TILE_WIDTH + (TILE_WIDTH / 2)
            map[i][j].y = (18 - i) * TILE_HEIGHT + (TILE_HEIGHT / 2)
            potion[i][j].x = j * TILE_WIDTH + (TILE_WIDTH / 2)
            potion[i][j].y = (18 - i) * TILE_HEIGHT + (TILE_HEIGHT / 2)
            if tile_Setting[i][j] == '■':
                map[i][j].isDraw = True
            if tile_Setting[i][j] == 'R':
                potion[i][j].color = 1
                potion[i][j].isDraw = True
            elif tile_Setting[i][j] == 'G':
                potion[i][j].color = 2
                potion[i][j].isDraw = True
            elif tile_Setting[i][j] == 'B':
                potion[i][j].color = 3
                potion[i][j].isDraw = True
            elif tile_Setting[i][j] == 'W':
                potion[i][j].color = 4
                potion[i][j].isDraw = True
            elif tile_Setting[i][j] == 'N':
                potion[i][j].color = 0
                potion[i][j].isDraw = True


def exit():
    global map, terra, background, potion
    del(terra)
    del(map)
    del(background)
    del(potion)

def pause():
    pass


def resume():
    pass


def handle_events():
    global running

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            terra.handle_event(event)


def update():
    global cnt
    terra.update()
    # 충돌체크
    for i in range(MAX_TILE_HEIGHT):
        for j in range(MAX_TILE_WIDTH):
            if potion[i][j].isDraw:
                if collide(terra, potion[i][j]):
                    potion[i][j].isDraw = False
                    if potion[i][j].color == 4:
                        terra.color = 0
                    else:
                        terra.color = potion[i][j].color

            if map[i][j].isDraw:
                map[i][j].update(terra)
                if tile.intersected_rectangle(map[i][j].collided_Rect, map[i][j].x - 16, map[i][j].y + 16, map[i][j].x + 16,
                                 map[i][j].y - 16, terra.x - 10, terra.y + 16, terra.x + 10, terra.y - 16):
                    cnt = 1
    if cnt == 0:
        if not terra.jumping:
            terra.acceleration = 0
        terra.jumping = True
    else:
        cnt = 0

def draw():
    clear_canvas()
    background.draw()
    for i in range(MAX_TILE_HEIGHT):
        for j in range(MAX_TILE_WIDTH):
            map[i][j].draw()
            potion[i][j].draw()
    terra.draw()
    update_canvas()
