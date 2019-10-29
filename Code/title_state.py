import game_framework
from pico2d import *
import stage1_state


name = "TitleState"
image = None
image2 = None
logo_time = 0.0
logo_draw = False


def enter():
    global image, image2
    image = load_image('Resource\\BackGround\\Title_1.png')
    image2 = load_image('Resource\\BackGround\\Title_2.png')


def exit():
    global image, image2
    del(image2)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(stage1_state)


def draw():
    clear_canvas()
    if logo_draw == True:
        image.draw(400, 300)
    else:
        image2.draw(400, 300)
    update_canvas()







def update():
    global logo_time, logo_draw
    if logo_time > 0.3:
        logo_time = 0
        if logo_draw == True:
            logo_draw = False
        else:
            logo_draw = True
    delay(0.01)
    logo_time += 0.01


def pause():
    pass


def resume():
    pass

