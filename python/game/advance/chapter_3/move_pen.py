import tkinter

key = ""
koff = False

def key_press(e):
    global key, koff
    key = e.keysym
    koff = False

def key_release(e):
    global koff
    koff = True

DIR_UP = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3

ANIMATION = [0, 1, 0, 2]

pen_x = 60 * 1 + 30
pen_y = 60 * 1 + 30
pen_d = 0
pen_a = 0
tmr = 0

map_data = [
    [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
    [0, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 0],
    [0, 3, 0, 0, 3, 3, 3, 3, 0, 0, 3, 0],
    [0, 3, 1, 1, 3, 0, 0, 3, 1, 1, 3, 0],
    [0, 3, 2, 2, 3, 0, 0, 3, 2, 2, 3, 0],
    [0, 3, 0, 0, 3, 1, 1, 3, 0, 0, 3, 0],
    [0, 3, 1, 1, 3, 3, 3, 3, 1, 1, 3, 0],
    [0, 2, 3, 3, 2, 0, 0, 2, 3, 3, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
width = 12 * 60
height = 9 * 60

def draw_screen():
    canvas.delete("SCREEN")
    for y in range(9):
        for x in range(12):
            canvas.create_image(x*60 + 30, y*60 + 30, image=img_bg[map_data[y][x]], tag="SCREEN")
    canvas.create_image(pen_x, pen_y, image=img_pen[pen_a], tag="SCREEN")

def check_wall(cx, cy, di, dot):
    chk = False
    if di == DIR_UP:
        mx = int((cx-30)/60)
        my = int((cy-30-dot)/60)
        if map_data[my][mx] <= 1:
            chk = True
        mx = int((cx+29)/60)
        if map_data[my][mx] <= 1:
            chk = True
    if di == DIR_DOWN:
        mx = int((cx-30)/60)
        my = int((cy+29+dot)/60)
        if map_data[my][mx] <= 1:
            chk = True
        mx = int((cx+29)/60)
        if map_data[my][mx] <= 1:
            chk = True
    if di == DIR_LEFT:
        mx = int((cx-30-dot)/60)
        my = int((cy-30)/60)
        if map_data[my][mx] <= 1:
            chk = True
        my = int((cy+29)/60)
        if map_data[my][mx] <= 1:
            chk = True
    if di == DIR_RIGHT:
        mx = int((cx+29+dot)/60)
        my = int((cy-30)/60)
        if map_data[my][mx] <= 1:
            chk = True
        my = int((cy+29)/60)
        if map_data[my][mx] <= 1:
            chk = True
    return chk

def move_pen():
    global pen_x, pen_y, pen_d, pen_a
    if key == "Up":
        pen_d = DIR_UP
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_y -= 20
    if key == "Down":
        pen_d = DIR_DOWN
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_y += 20
    if key == "Left":
        pen_d = DIR_LEFT
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_x -= 20
    if key == "Right":
        pen_d = DIR_RIGHT
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_x += 20
    pen_a = pen_d * 3 + ANIMATION[tmr % 4]

def main():
    global key, koff, tmr
    tmr += 1
    draw_screen()
    move_pen()
    if koff == True:
        key = ""
        koff = False
    root.after(100, main)


root = tkinter.Tk()
root.title("title")
root.resizable(False, False)
root.bind("<KeyPress>", key_press)
root.bind("<KeyRelease>", key_release)
canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()
img_bg = [
    tkinter.PhotoImage(file="chip00.png"),
    tkinter.PhotoImage(file="chip01.png"),
    tkinter.PhotoImage(file="chip02.png"),
    tkinter.PhotoImage(file="chip03.png"),
]
img_pen = [
    tkinter.PhotoImage(file="pen00.png"),
    tkinter.PhotoImage(file="pen01.png"),
    tkinter.PhotoImage(file="pen02.png"),
    tkinter.PhotoImage(file="pen03.png"),
    tkinter.PhotoImage(file="pen04.png"),
    tkinter.PhotoImage(file="pen05.png"),
    tkinter.PhotoImage(file="pen06.png"),
    tkinter.PhotoImage(file="pen07.png"),
    tkinter.PhotoImage(file="pen08.png"),
    tkinter.PhotoImage(file="pen09.png"),
    tkinter.PhotoImage(file="pen10.png"),
    tkinter.PhotoImage(file="pen11.png"),   
]

main()
root.mainloop()