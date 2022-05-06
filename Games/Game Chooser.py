import turtle
import time

win_pane = turtle.Screen()
win_pane.title("Games by Bhaskar")
win_pane.bgcolor("black")
win_pane.setup(width=800, height=600)
win_pane.tracer(0)


def HvsH():
    win_pen.clear()
    win_pen.write("Playing Human vs Human", align="center", font=("Courier", 24, "normal"))
    time.sleep(1)
    win_pen.clear()
    win_pen.write("Get Ready!!!!!", align="center", font=("Courier", 24, "normal"))
    time.sleep(1)
    win_pen.clear()
    import PongHvsH


def HvsM():
    win_pen.clear()
    win_pen.write("Playing Human vs Machine", align="center", font=("Courier", 24, "normal"))
    time.sleep(1)
    win_pen.clear()
    win_pen.write("Get Ready!!!!!", font=("Courier", 24, "normal"), align="center")
    time.sleep(1)
    win_pen.clear()
    import pongHvsM
    
def Snake():
    win_pen.clear()
    win_pen.write("Playing Snake", align="center", font=("Courier", 24, "normal"))
    time.sleep(1)
    win_pen.clear()
    win_pen.write("Get Ready!!!!!", font=("Courier", 24, "normal"), align="center")
    time.sleep(1)
    win_pen.clear()
    import Snake
    
def TicTacToe():
    win_pen.clear()
    win_pen.write("Playing TicTacToe", align="center", font=("Courier", 24, "normal"))
    time.sleep(1)
    win_pen.clear()
    win_pen.write("Get Ready!!!!!", font=("Courier", 24, "normal"), align="center")
    time.sleep(1)
    win_pen.clear()
    import TicTacToe

def Pong():
    win_pen.clear()
    win_pen.write("PRESS M: To play Pong against Machine\nPRESS H: To play Pong against Human", align="center", font=("Courier", 24, "normal"))
    win_pane.listen()
    win_pane.onkeypress(HvsH, "h")
    win_pane.onkeypress(HvsM, "m")
    
    
# win_pen module
win_pen = turtle.Turtle()
win_pen.speed(0)
win_pen.color("white")
win_pen.penup()
win_pen.hideturtle()
win_pen.goto(0, 0)
win_pen.write("PRESS P: To play Pong\nPRESS S: To play Snake Game\nPRESS T: To play Tic Tac Toe", align="center", font=("Courier", 24, "normal"))
win_pane.listen()
win_pane.onkeypress(Pong, "p")
win_pane.onkeypress(Snake, "s")
win_pane.onkeypress(TicTacToe, "t")

while True:
    win_pane.update()