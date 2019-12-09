import game_framework
import stage1_state
import stage2_state


name = "ResetState"
now_stage = 0


def enter():
    if now_stage == 1:
        game_framework.change_state(stage1_state)
    elif now_stage == 2:
        game_framework.change_state(stage2_state)


def exit():
    pass


def handle_events():
    pass


def draw():
    pass


def update():
    pass


def pause():
    pass


def resume():
    pass

