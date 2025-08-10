import turtle
import winsound
import sys

# ====== SOUND FUNCTION ======
def play_sound():
    try:
        winsound.Beep(1000, 50)  # Simple beep sound (1000Hz for 50ms)
    except:
        pass  # Silently fail if sound doesn't work

# ====== SCREEN SETUP ======
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# ====== SCORE ======
score_a = 0
score_b = 0

# ====== PADDLE A ======
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# ====== PADDLE B ======
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ====== BALL ======
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# ====== SCORE DISPLAY ======
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# ====== PADDLE MOVEMENT ======
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        paddle_a.sety(y + 20)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        paddle_a.sety(y - 20)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        paddle_b.sety(y + 20)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        paddle_b.sety(y - 20)

# ====== KEY BINDINGS ======
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# ====== GAME LOOP FUNCTION ======
def game_loop():
    global score_a, score_b

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking (top/bottom)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        play_sound()

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        play_sound()

    # Right wall (score for Player A)
    if ball.xcor() > 390:
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Left wall (score for Player B)
    elif ball.xcor() < -390:
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle collisions
    if (ball.xcor() < -340 and paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
        play_sound()

    elif (ball.xcor() > 340 and paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1
        play_sound()

    # Update screen and repeat
    wn.update()
    wn.ontimer(game_loop, 10)  # Run again in 10ms

# ====== START GAME ======
game_loop()
wn.mainloop()
