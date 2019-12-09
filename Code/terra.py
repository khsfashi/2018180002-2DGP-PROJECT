import game_framework
from pico2d import *

# Terra Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
JUMP_SPEED_PPS = RUN_SPEED_PPS

# Terra Action Speed
TIME_PER_ACTION = 0.25
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 3

# Terra  Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE = range(5)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}

# Terra State


class IdleState:

    @staticmethod
    def enter(terra, event):
        if event == RIGHT_DOWN:
            terra.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            terra.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            terra.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            terra.velocity += RUN_SPEED_PPS

    @staticmethod
    def exit(terra, event):
        pass

    @staticmethod
    def do(terra):
        if terra.jumping:
            terra.y += terra.acceleration
            if terra.acceleration >= -10:
                terra.acceleration -= 0.05

    @staticmethod
    def draw(terra):
        if terra.dir == 1:
            terra.image.clip_draw(terra.color * 96, 0, Terra.CHARACTER_WIDTH, Terra.CHARACTER_HEIGHT, terra.x, terra.y)
        else:
            terra.image.clip_draw(terra.color * 96, 32, Terra.CHARACTER_WIDTH, Terra.CHARACTER_HEIGHT, terra.x, terra.y)


class RunState:

    @staticmethod
    def enter(terra, event):
        if event == RIGHT_DOWN:
            terra.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            terra.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            terra.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            terra.velocity += RUN_SPEED_PPS
        terra.dir = clamp(-1, terra.velocity, 1)

    @staticmethod
    def exit(terra, event):
        pass

    @staticmethod
    def do(terra):
        terra.frame = (terra.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        terra.x += terra.velocity * game_framework.frame_time
        if terra.jumping:
            terra.y += terra.acceleration
            if terra.acceleration >= -10:
                terra.acceleration -= 0.05

    @staticmethod
    def draw(terra):
        if terra.dir == 1:
            terra.image.clip_draw(int(terra.frame) * 32 + terra.color * 96, 0, Terra.CHARACTER_WIDTH,
                                  Terra.CHARACTER_HEIGHT, terra.x, terra.y)
        else:
            terra.image.clip_draw(int(terra.frame) * 32 + terra.color * 96, 32, Terra.CHARACTER_WIDTH,
                                  Terra.CHARACTER_HEIGHT, terra.x, terra.y)

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                SPACE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
               SPACE: RunState}
}


class Terra:
    # 상수
    CHARACTER_WIDTH = 32
    CHARACTER_HEIGHT = 32

    def __init__(self):
        self.image = load_image('Resource\\Character\\Scientists2.png')
        self.x, self.y = 48, 48
        self.frame = 0
        self.dir = 0
        self.velocity = 0
        self.acceleration = 0
        self.jumping = True
        self.color = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.enter = False
        self.drink_sound = load_wav('Resource\\Sounds\\drink_Potion.wav')
        self.drink_sound.set_volume(100)
        self.super_jump_sound = load_wav('Resource\\Sounds\\JUMP1.wav')
        self.super_jump_sound.set_volume(100)
        self.jump_sound = load_wav('Resource\\Sounds\\JUMP2.wav')
        self.jump_sound.set_volume(100)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE and not self.jumping:
            self.jump_sound.play()
            self.jumping = True
            self.acceleration = 3

    def get_bb(self):
        return self.x - 10, self.y - 16, self.x + 10, self.y + 16

    def super_jump(self):
        if self.jumping:
            self.super_jump_sound.play()
        self.acceleration = 5
        self.jumping = True

    def drink_potion(self):
        self.drink_sound.play()

    def color_change(self, color):
        if self.color == 0 or self.color >= 5:
            self.color = color
        else:
            self.color = self.color + color + 2