import tkinter
import pprint
import random
import copy

width = 918
height = 768

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0

neko = [[0]*8 for _ in range(10)]


def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e):
    global mouse_c 
    mouse_c = 1

def mouse_release(e):
    global mouse_c
    mouse_c = 0

def drop_neko():
    for y in range(8, -1, -1):
        for x in range(8):
            if neko[y+1][x] == 0:
                neko[y+1][x] = neko[y][x]
                neko[y][x] = 0

def draw_neko():
    for y in range(10):
        for x in range(8):
                canvas.create_image(72*x + 60, 72*y + 60, image=neko_img[neko[y][x]], tags="NEKO")
                
def sweep_foot_print():
    for y in range(10):
        for x in range(8):
            if neko[y][x] == 7:
                neko[y][x] = 0
def judge():
    global neko
    check_list = copy.deepcopy(neko)
    #가로
    for y in range(10):
        for x in range(1, 7):
            if neko[y][x] != 0:
                if (neko[y][x-1] == neko[y][x]) and (neko[y][x+1] == neko[y][x]):
                    check_list[y][x-1] = 7
                    check_list[y][x] = 7
                    check_list[y][x+1] = 7
    #세로
    for y in range(1, 9):
        for x in range(8):
            if neko[y][x] != 0:
                if (neko[y-1][x] == neko[y][x]) and (neko[y+1][x] == neko[y][x]):
                    check_list[y-1][x] = 7
                    check_list[y][x] = 7
                    check_list[y+1][x] = 7
    #대각선
    for y in range(1, 9):
        for x in range(1, 7):
            if neko[y][x] != 0:
                if (neko[y-1][x+1] == neko[y][x]) and (neko[y+1][x-1] == neko[y][x]):
                    check_list[y-1][x+1] = 7
                    check_list[y][x] = 7
                    check_list[y+1][x-1] = 7            
                if (neko[y-1][x-1] == neko[y][x]) and (neko[y+1][x+1] == neko[y][x]):
                    check_list[y-1][x-1] = 7
                    check_list[y][x] = 7
                    check_list[y+1][x+1] = 7
    neko = copy.deepcopy(check_list)

def game_main():
    global mouse_c, cursor_x, cursor_y
    drop_neko() # -- drop completed
    canvas.delete("CURSOR")
    if (mouse_x >=24 and mouse_x < 72*8 + 24) and (mouse_y >=24 and mouse_y < 72*10 + 24):
        cursor_x = int((mouse_x - 24) / 72)
        cursor_y = int((mouse_y - 24) / 72)
        canvas.create_image(72*cursor_x + 60, 72*cursor_y + 60, image=cursor, tags="CURSOR")
        if mouse_c == 1:
            target = random.randint(1, 6)
            neko[cursor_y][cursor_x] = target
            mouse_c = 0
    canvas.delete("NEKO")
    judge()
    draw_neko()
    sweep_foot_print()
    root.after(100, game_main)

root = tkinter.Tk()
root.title("title")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)
root.bind("<ButtonRelease>", mouse_release)

canvas = tkinter.Canvas(root, width=width, height=height)
canvas.pack()

bg_img = tkinter.PhotoImage(file="neko_bg.png")
canvas.create_image(width/2, height/2, image=bg_img, tags="BG")
cursor = tkinter.PhotoImage(file="neko_cursor.png")

neko_img = [
    None,
    tkinter.PhotoImage(file="neko1.png"),
    tkinter.PhotoImage(file="neko2.png"),
    tkinter.PhotoImage(file="neko3.png"),
    tkinter.PhotoImage(file="neko4.png"),
    tkinter.PhotoImage(file="neko5.png"),
    tkinter.PhotoImage(file="neko6.png"),
    tkinter.PhotoImage(file="neko_niku.png"),
]
game_main()
root.mainloop()