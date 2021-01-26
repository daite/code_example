import tkinter
import random

width = 480
height = 640

# bg pos
bg_pos = 0

# index
index = 0

# score
score = 0

# key
key = ""
koff = False

# space location
px = 240
py = 540

# enemy location
ENEMY_COUNT = 30
mx = [0] * ENEMY_COUNT
my = [0] * ENEMY_COUNT

# timer
timer = 0

def key_press(e):
    global key, koff
    key = e.keysym
    koff = True

def key_release(e):
    global koff
    koff = False

def init_enemy():
    for i in range(ENEMY_COUNT):
        mx[i] = random.randint(0, width)
        my[i] = random.randint(-height, 0)

def move_enemy():
    global index, timer
    for i in range(ENEMY_COUNT):
        my[i] = my[i] + 5 + i / 6
        if my[i] > 660:
            mx[i] =random.randint(0, width)
            my[i] = random.randint(-height, 0)
        if index == 1 and hit_check(px, py, mx[i], my[i]) == True:
            index = 2
            timer = 0
        canvas.create_image(mx[i], my[i], image=img_enemy, tag="SCREEN")

def move_player():
    global px, timer
    if key == "Left" and px > 40:
        px -= 30
    if key == "Right" and px < 440:
        px += 30
    canvas.create_image(px, py, image=img_space_ship[timer % 2], tag="SCREEN")

def hit_check(x1, y1, x2, y2):
    if ((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2)) < 36 * 36:
        return True
    return False

def game_main():
    global score, bg_pos, koff, timer, key, index
    timer += 1
    canvas.delete("SCREEN")
    bg_pos = (bg_pos + 1) % width
    canvas.create_image(bg_pos - width / 2, height / 2, image=img_bg, tag="SCREEN")
    canvas.create_image(bg_pos + width / 2, height / 2, image=img_bg, tag="SCREEN")
    if index == 0:
        canvas.create_text(width / 2, 100, text="doraneko".upper(), font=("Times New Roman", 30), fill="white", tag="SCREEN")
        canvas.create_text(width / 2, 500, text="Space to start", font=("Times New Roman", 30), fill="limegreen", tag="SCREEN")
        if key == "space":
            init_enemy()
            score = 0
            index = 1
    if index == 1:
        move_enemy()
        move_player()
        score += 1
    if index == 2:
        move_enemy()
        canvas.create_text(width / 2, timer * 6, text="game over".upper(), font=("Times New Roman", 40), fill="red", tag="SCREEN")
        if timer == 60:
            timer = 0
            score = 0
            index = 0
            key = ""
    if koff == True:
        key = ""
        koff = False
    canvas.create_text(100, 50, text="Index: {}".format(index), font=("Times New Roman", 30), fill="black", tag="SCREEN")
    canvas.create_text(370, 50, text="Score: {}".format(score), font=("Times New Roman", 30), fill="black", tag="SCREEN")
    root.after(50, game_main)

root = tkinter.Tk()
root.title("mini game")
root.resizable(False, False)

root.bind("<KeyPress>", key_press)
root.bind("<KeyRelease>", key_release)

canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()

# image
img_bg = tkinter.PhotoImage(file="building.png")
img_space_ship = [
    tkinter.PhotoImage(file="dora0.png"),
    tkinter.PhotoImage(file="dora1.png"),
]
img_enemy = tkinter.PhotoImage(file="fun.png")
game_main()
root.mainloop()
