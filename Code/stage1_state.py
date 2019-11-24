import game_framework
from pico2d import *
from background import Background
from terra import Terra
from item import Item
from object import Object
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
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Wp', 0, 0, 0, 0, 0, 0, 0, '■', '■', '■', 0, 0, 0, 0],
                [0, '■', 0, 0, 0, 0, 0, 0, 0, 0, 0, '■', '■', '■', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, '■', 0, 0, 0, '■', '■', '■', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, '■', 'Rp', 0, 0, 'Rg', 0, 'Gp', 0, 0, 0, 0, 'Bp', 0, 0, 0, 0, 0, 0, 0, 0, 'Gj', 0, 0, 0],
                ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']
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
    global map, terra, background, item, object
    background = Background()
    terra = Terra()
    map = [[tile.Tile() for j in range(MAX_TILE_WIDTH)] for i in range(MAX_TILE_HEIGHT)]
    item = [[Item() for j in range(MAX_TILE_WIDTH)] for i in range(MAX_TILE_HEIGHT)]
    object = [[Object() for j in range(MAX_TILE_WIDTH)] for i in range(MAX_TILE_HEIGHT)]
    for i in range(MAX_TILE_HEIGHT):
        for j in range(MAX_TILE_WIDTH):
            map[i][j].x = j * TILE_WIDTH + (TILE_WIDTH / 2)
            map[i][j].y = (18 - i) * TILE_HEIGHT + (TILE_HEIGHT / 2)
            item[i][j].x = j * TILE_WIDTH + (TILE_WIDTH / 2)
            item[i][j].y = (18 - i) * TILE_HEIGHT + (TILE_HEIGHT / 2)
            object[i][j].x = j * TILE_WIDTH + (TILE_WIDTH / 2)
            object[i][j].y = (18 - i) * TILE_HEIGHT + (TILE_HEIGHT / 2)
            if tile_Setting[i][j] == 0:
                tile_Setting[i][j] = 0
            elif tile_Setting[i][j] == '■':
                map[i][j].isDraw = True
            elif tile_Setting[i][j] == 'Rp':
                item[i][j].color = 1
                item[i][j].kind = 1
                item[i][j].isDraw = True
            elif tile_Setting[i][j] == 'Gp':
                item[i][j].color = 2
                item[i][j].kind = 1
                item[i][j].isDraw = True
            elif tile_Setting[i][j] == 'Bp':
                item[i][j].color = 3
                item[i][j].kind = 1
                item[i][j].isDraw = True
            elif tile_Setting[i][j] == 'Wp':
                item[i][j].color = 4
                item[i][j].kind = 1
                item[i][j].isDraw = True
            elif tile_Setting[i][j] == 'Np':
                item[i][j].color = 0
                item[i][j].kind = 1
                item[i][j].isDraw = True
            elif tile_Setting[i][j] == 'Rg':
                object[i][j].color = 1
                object[i][j].kind = 2
                object[i][j].isDraw = True
            elif tile_Setting[i][j] == 'Gg':
                object[i][j].color = 2
                object[i][j].kind = 2
                object[i][j].isDraw = True
            elif tile_Setting[i][j] == 'Bg':
                object[i][j].color = 3
                object[i][j].kind = 2
                object[i][j].isDraw = True
            elif tile_Setting[i][j] == 'Yg':
                object[i][j].color = 5
                object[i][j].kind = 2
                object[i][j].isDraw = True
            elif tile_Setting[i][j] == 'Cg':
                object[i][j].color = 6
                object[i][j].kind = 2
                object[i][j].isDraw = True
            elif tile_Setting[i][j] == 'Mg':
                object[i][j].color = 7
                object[i][j].kind = 2
                object[i][j].isDraw = True
            elif tile_Setting[i][j] == 'Rj':
                object[i][j].color = 1
                object[i][j].kind = 1
                object[i][j].isDraw = True
            elif tile_Setting[i][j] == 'Gj':
                object[i][j].color = 2
                object[i][j].kind = 1
                object[i][j].isDraw = True
            elif tile_Setting[i][j] == 'Bj':
                object[i][j].color = 3
                object[i][j].kind = 1
                object[i][j].isDraw = True
            elif tile_Setting[i][j] == 'Yj':
                object[i][j].color = 5
                object[i][j].kind = 1
                object[i][j].isDraw = True
            elif tile_Setting[i][j] == 'Cj':
                object[i][j].color = 6
                object[i][j].kind = 1
                object[i][j].isDraw = True
            elif tile_Setting[i][j] == 'Mj':
                object[i][j].color = 7
                object[i][j].kind = 1
                object[i][j].isDraw = True



def exit():
    global map, terra, background, item, object
    del(terra)
    del(map)
    del(background)
    del(item)
    del(object)

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
            if item[i][j].isDraw:
                if collide(terra, item[i][j]):
                    item[i][j].isDraw = False
                    if item[i][j].color == 4:
                        terra.color = 0
                    else:
                        terra.color = item[i][j].color
            if object[i][j].isDraw:
                object[i][j].update(terra)
                if object[i][j].kind == 1 and collide(terra, object[i][j]):
                    if terra.color == object[i][j].color:
                        terra.super_jump()

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
            item[i][j].draw()
            object[i][j].draw()
    terra.draw()
    update_canvas()
