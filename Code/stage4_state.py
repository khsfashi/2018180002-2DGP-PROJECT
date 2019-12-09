import game_framework
from pico2d import *
from background import Background
from terra import Terra
from item import Item
from object import Object
import tile
import reset_state
import stage5_state

# 상수 모음
MAX_TILE_WIDTH = 25
MAX_TILE_HEIGHT = 19
TILE_WIDTH = 32
TILE_HEIGHT = 32
name = "Stage4State"

cnt = 0
potion_cnt = 0

tile_Setting = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                ['■', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                ['■', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                ['■', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                ['■', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                ['■', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                ['■', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                ['■', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                ['■', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                ['■', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                ['■', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                ['■', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                ['■', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                ['■', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
    global map, terra, background, item, object, potion_cnt, cnt
    potion_cnt = 0
    cnt = 0

    background = Background()
    background.kind = 3
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
                potion_cnt += 1
                item[i][j].setting(1, 1)
            elif tile_Setting[i][j] == 'Gp':
                potion_cnt += 1
                item[i][j].setting(2, 1)
            elif tile_Setting[i][j] == 'Bp':
                potion_cnt += 1
                item[i][j].setting(3, 1)
            elif tile_Setting[i][j] == 'Wp':
                potion_cnt += 1
                item[i][j].setting(4, 1)
            elif tile_Setting[i][j] == 'Np':
                potion_cnt += 1
                item[i][j].setting(0, 1)
            elif tile_Setting[i][j] == 'P':
                item[i][j].setting(0, 0)
            elif tile_Setting[i][j] == 'Rg':
                object[i][j].setting(1, 2)
            elif tile_Setting[i][j] == 'Gg':
                object[i][j].setting(2, 2)
            elif tile_Setting[i][j] == 'Bg':
                object[i][j].setting(3, 2)
            elif tile_Setting[i][j] == 'Yg':
                object[i][j].setting(5, 2)
            elif tile_Setting[i][j] == 'Mg':
                object[i][j].setting(6, 2)
            elif tile_Setting[i][j] == 'Cg':
                object[i][j].setting(7, 2)
            elif tile_Setting[i][j] == 'Rj':
                object[i][j].setting(1, 1)
            elif tile_Setting[i][j] == 'Gj':
                object[i][j].setting(2, 1)
                object[i][j].isDraw = True
            elif tile_Setting[i][j] == 'Bj':
                object[i][j].setting(3, 1)
            elif tile_Setting[i][j] == 'Yj':
                object[i][j].setting(5, 1)
            elif tile_Setting[i][j] == 'Mj':
                object[i][j].setting(6, 1)
            elif tile_Setting[i][j] == 'Cj':
                object[i][j].setting(7, 1)
            elif tile_Setting[i][j] == 'Rt':
                object[i][j].setting(1, 0)
            elif tile_Setting[i][j] == 'Gt':
                object[i][j].setting(2, 0)
            elif tile_Setting[i][j] == 'Bt':
                object[i][j].setting(3, 0)
            elif tile_Setting[i][j] == 'Yt':
                object[i][j].setting(5, 0)
            elif tile_Setting[i][j] == 'Mt':
                object[i][j].setting(6, 0)
            elif tile_Setting[i][j] == 'Ct':
                object[i][j].setting(7, 0)




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
    if not terra.enter and len(events) > 0:
        events.pop()
        terra.enter = True

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_r:
            game_framework.reset(4)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_q:
            game_framework.change_state(stage5_state)
        else:
            terra.handle_event(event)


def update():
    global cnt, potion_cnt
    terra.update()
    # 충돌체크
    for i in range(MAX_TILE_HEIGHT):
        for j in range(MAX_TILE_WIDTH):
            if item[i][j].isDraw:
                if collide(terra, item[i][j]):
                    terra.drink_potion()
                    item[i][j].isDraw = False
                    if item[i][j].kind == 1:
                        potion_cnt -= 1
                    elif item[i][j].kind == 0:
                        terra.save_color()
                    if item[i][j].color == 4 or item[i][j].color == 0:
                        terra.color = 0
                    else:
                        terra.color_change(item[i][j].color)
            if object[i][j].isDraw:
                object[i][j].update(terra)
                if object[i][j].kind == 1 and collide(terra, object[i][j]):
                    if terra.color == object[i][j].color:
                        terra.super_jump()

                if object[i][j].kind == 0:
                    if collide(terra, object[i][j]) and terra.color == object[i][j].color:
                        if object[i][j].attack_mode:
                            print("사망!")
                            game_framework.reset(4)
                        else:
                            object[i][j].attack_mode = True
                    else:
                        object[i][j].attack_mode = False

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

    if terra.x >= 800:
        if potion_cnt == 0:
            print("스테이지 클리어! 다음 스테이지로!")
            game_framework.change_state(stage5_state)
        else:
            game_framework.reset(4)


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
