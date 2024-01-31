import turtle
import time
import random

delay = 0.1
score = 0
player_name = ""
game_in_progress=True

# Função para obter o nome do jogador
def get_player_name():
    global player_name
    player_name = turtle.textinput("Snake Game", "Digite seu nome:")
    if player_name is None or player_name.strip() == "":
        player_name = "Anonimo"

# Função para exibir a mensagem de Game Over
def game_over():
    global score, game_in_progress
    turtle.goto(0, 0)
    time.sleep(1)
    turtle.clear()
    answer = turtle.textinput("Snake Game", "Game Over!\nScore - {}: {}\nQuer continuar o jogo? (Sim ou Nao)".format(player_name, score)).lower()

    if answer == "sim":
        reset_game()
    else:
        game_in_progress = False

# Função para reiniciar o jogo
def reset_game():
    global score, game_in_progress
    global player_name

    # Reiniciar a pontuação
    score = 0
    score_display.clear()
    score_display.write("Score - {}: {}".format(player_name, score), align="center", font=("Courier", 20, "normal"))

    # Mover a cabeça de volta para a posição inicial
    head.goto(0, 0)
    head.direction = "Right"
    food.goto(0, 100)

    # Esconder os segmentos
    for segment in segments:
        segment.goto(1000, 1000)

    # Limpar a lista de segmentos
    segments.clear()

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=730) 
wn.tracer(0)

# Obter o nome do jogador
get_player_name()

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Right"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Snake body
segments = []

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 325)
score_display.write("Score: 0", align="center", font=("Courier", 20, "normal"))

# Dividers lines
divider_line = turtle.Turtle()
divider_line.speed(0)
divider_line.color("white")
divider_line.penup()
divider_line.goto(-300, 310)
divider_line.pendown()
divider_line.goto(300, 310)
divider_line.hideturtle()

divider_line_left = turtle.Turtle()
divider_line_left.speed(0)
divider_line_left.color("white")
divider_line_left.penup()
divider_line_left.goto(-300, 310)
divider_line_left.pendown()
divider_line_left.goto(-300, -310)
divider_line_left.hideturtle()

divider_line_right = turtle.Turtle()
divider_line_right.speed(0)
divider_line_right.color("white")
divider_line_right.penup()
divider_line_right.goto(300, 310)
divider_line_right.pendown()
divider_line_right.goto(300, -310)
divider_line_right.hideturtle()

divider_line_down = turtle.Turtle()
divider_line_down.speed(0)
divider_line_down.color("white")
divider_line_down.penup()
divider_line_down.goto(-300, -310)
divider_line_down.pendown()
divider_line_down.goto(300, -310)
divider_line_down.hideturtle()

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_up, "W")
wn.onkeypress(go_down, "S")
wn.onkeypress(go_left, "A")
wn.onkeypress(go_right, "D")

# Main game loop
while game_in_progress:
    wn.update()

    # Check for a collision with the border
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        game_over()

    # Check for a collision with the food
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Update the score
        score += 10
        score_display.clear()
        score_display.write("Score - {}: {}".format(player_name, score), align="center", font=("Courier", 20, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collisions with the body segments
    for segment in segments:
        if head.distance(segment) < 20:
            game_over()
            break

    time.sleep(delay)

# Fechar a janela quando o jogo terminar
wn.bye()
