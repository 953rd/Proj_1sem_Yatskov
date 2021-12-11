import pgzrun
import random

TITLE = "Arkanoid"
WIDTH = 800
HEIGHT = 600
score = 0

paddle = Actor("paddle.png")
paddle.x = 400
paddle.y = 585

ball = Actor("ball.png")
ball.x = 400
ball.y = 545.5


ball_x_speed = 3
ball_y_speed = 3

bars_list = []


def draw():
    screen.blit("background.png", (0, 0))
    paddle.draw()
    ball.draw()
    for bar in bars_list:
        bar.draw()


def place_bars(x, y, image):
    bar_x = x
    bar_y = y
    for i in range(9):
        bar = Actor(image)
        bar.x = bar_x
        bar.y = bar_y
        bar_x += 70
        bars_list.append(bar)


def place_bars1(x, y, image):
    bar_x = x
    bar_y = y
    for i in range(4):
        bar = Actor(image)
        bar.x = bar_x - 70
        bar.y = bar_y - 40
        bar_x += 70
        bar_y += 40
        bars_list.append(bar)
    for i in range(4):
        bar = Actor(image)
        bar.x = bar_x + 350
        bar.y = bar_y - 200
        bar_x -= 70
        bar_y += 40
        bars_list.append(bar)


def place_bars2(x, y, image):
    bar_x = x
    bar_y = y
    for i in range(2):
        bar = Actor(image)
        bar.x = bar_x + 245
        bar.y = bar_y - 120
        bar_x += 70
        bars_list.append(bar)

'''def handle_mouse_event(self, type, pos):
    if type == pygame.MOUSEMOTION:
        self.handle_mouse_move(pos)
    elif type == pygame.MOUSEBUTTONDOWN:
        self.handle_mouse_down(pos)
    elif type == pygame.MOUSEBUTTONUP:
        self.handle_mouse_up(pos)'''


def update():
    global ball_x_speed, ball_y_speed, score
    if keyboard.left:
        paddle.x = paddle.x - 5
    if keyboard.right:
        paddle.x = paddle.x + 5

    update_ball()
    for bar in bars_list:
        if ball.colliderect(bar):
            bars_list.remove(bar)
            ball_y_speed *= -1
            score += 1
            print("Очки:", score)

    if paddle.colliderect(ball):
        ball_y_speed *= -1
        rand = random.randint(0,1)
        if rand:
            ball_x_speed *= -1

    if paddle.x >= WIDTH - 40:
        paddle.x = paddle.x - 5
    if paddle.x <= 40:
        paddle.x = paddle.x + 5

def update_ball():
    global ball_x_speed, ball_y_speed
    ball.x -= ball_x_speed
    ball.y -= ball_y_speed
    if (ball.x >= WIDTH - 15) or (ball.x <= 15):
        ball_x_speed *= -1
    if (ball.y <= 15):
        ball_y_speed *= -1
    if (ball.y >= paddle.y):
            ball.x = 400
            ball.y = 545.5
            paddle.x = 400
            paddle.y = 585
            '''x = 120
            y = 100
            bars_list.clear()
            for i in range(3):
                place_bars(x, y, coloured_box_list[i])
                y += 50'''

coloured_box_list = ["red_grey_brick.png", "purple_brick",
                     "g_g_brick.png"]

coloured_box_list1 = ["green_brick.png",
                      "red_purple_brick.png", "red_brick.png"]

coloured_box_list2 = ["red_grey_brick.png"]

x = 120
y = 40
for coloured_box in coloured_box_list:
     place_bars(x, y, coloured_box)
     y += 40

for coloured_box in coloured_box_list1:
    place_bars1(x, y, coloured_box)
    y += 40

k = 0
while k<=4:
    for coloured_box in coloured_box_list2:
        place_bars2(x, y, coloured_box)
        y += 40
        k += 1


pgzrun.go()