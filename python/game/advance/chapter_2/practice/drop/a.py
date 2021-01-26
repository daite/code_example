import tkinter
import random
import copy

index = 0
timer = 0
score = 0
tsugi = 0

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0

hisc = 1000
difficulty = 0

width = 918
height = 768

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e):
    global mouse_c
    mouse_c = 1

neko = [[0]*8 for _ in range(10)]
check = [[0]*8 for _ in range(10)]

def draw_neko():
    cvs.delete("NEKO")
    for y in range(10):
        for x in range(8):
            if neko[y][x] > 0:
                cvs.create_image(72*x + 60, 72*y + 60, image=neko_img[neko[y][x]], tag="NEKO")

def check_neko():
    check = copy.deepcopy(neko)
    #가로
    for y in range(10):
        for x in range(1, 7):
            if check[y][x] > 0:
                if (check[y][x-1] == check[y][x]) and (check[y][x+1] == check[y][x]):
                    neko[y][x-1] = 7
                    neko[y][x] = 7
                    neko[y][x+1] = 7
    #세로
    for y in range(1, 9):
        for x in range(8):
            if check[y][x] > 0:
                if (check[y-1][x] == check[y][x]) and (check[y+1][x] == check[y][x]):
                    neko[y-1][x] = 7
                    neko[y][x] = 7
                    neko[y+1][x] = 7
    #대각선
    for y in range(1, 9):
        for x in range(1, 7):
            if check[y][x] > 0:
                if (check[y-1][x+1] == check[y][x]) and (check[y+1][x-1] == check[y][x]):
                    neko[y-1][x+1] = 7
                    neko[y][x] = 7
                    neko[y+1][x-1] = 7
                if (check[y-1][x-1] == check[y][x]) and (check[y+1][x+1] == check[y][x]):
                    neko[y-1][x-1] = 7
                    neko[y][x] = 7
                    neko[y+1][x+1] = 7

def sweep_neko():
    num = 0
    for y in range(10):
        for x in range(8):
            if neko[y][x] == 7:
                neko[y][x] = 0
                num += 1
    return num

def drop_neko():
    flag = False
    for y in range(8, -1, -1):
        for x in range(8):
            if neko[y+1][x] == 0 and neko[y][x] > 0:
                neko[y+1][x] = neko[y][x]
                neko[y][x] = 0
                flag = True
    return flag


def over_neko():
    for x in range(8):
            if neko[0][x] > 0:
                return True
    return False

def set_neko():
    for x in range(8):
        neko[0][x] = random.randint(0, difficulty)

def draw_txt(text, x, y, font_size, color, tag):
    fnt = ("Times New Roman", font_size, "bold")
    cvs.create_text(x + 2, y + 2, text=text, fill="black", font=fnt, tag=tag)
    cvs.create_text(x, y, text=text, fill=color, font=fnt, tag=tag)

def game_main():
    global index, timer, score, tsugi
    global cursor_x, cursor_y, mouse_c
    global hisc, difficulty

    if index == 0:
        draw_txt("야옹야옹", 312, 240, 100, "violet", "TITLE")
        cvs.create_rectangle(168, 384, 456, 456, fill="skyblue", width=0, tag="TITLE")
        draw_txt("Easy", 312, 420, 40, "white", "TITLE")
        cvs.create_rectangle(168, 528, 456, 600, fill="lightgreen", width=0, tag="TITLE")
        draw_txt("Normal", 312, 564, 40, "white", "TITLE")
        cvs.create_rectangle(168, 672, 456, 744, fill="orange", width=0, tag="TITLE")
        draw_txt("Hard", 312, 708, 40, "white", "TITLE")
        index = 1
        cursor_c = 0
    elif index == 1:
        difficulty = 0
        if mouse_c == 1:
            if 168 < mouse_x < 456 and 384 < mouse_y < 456:
                difficulty = 4
            if 168 < mouse_x < 456 and 528 < mouse_y < 600:
                difficulty = 5
            if 168 < mouse_x < 456 and 672 < mouse_y < 744:
                difficulty = 6
            if difficulty > 0:
                print(difficulty)           
                for y in range(10):
                    for x in range(8):
                        neko[y][x] = 0
                mouse_c = 0
                tsugi = 0
                score = 0
                cursor_x = 0
                cursor_y = 0
                set_neko()
                draw_neko()
                cvs.delete("TITLE")
                index = 2
    elif index == 2:
        if drop_neko() == False:
            index = 3
        draw_neko()
    elif index == 3:
        check_neko()
        draw_neko()
        index = 4
    elif index == 4:
        n = sweep_neko()
        score = score + n * difficulty * 2
        if score > hisc:
            hisc = score
        if n > 0:
            index = 2
        else:
            if over_neko() == False:
                tsugi = random.randint(1, difficulty)
                index = 5
            else:
                index = 6
                timer = 0
    elif index == 5:
        if (mouse_x >=24 and mouse_x < 72*8 + 24) and (mouse_y >= 24 and mouse_y < 72*10 + 24):
            cursor_x = int((mouse_x - 24) / 72)
            cursor_y = int((mouse_y - 24) / 72)
            if mouse_c == 1:
                mouse_c = 0
                set_neko()
                neko[cursor_y][cursor_x] = tsugi
                tsugi = 0
                index = 2
        cvs.delete("CURSOR")
        cvs.create_image(cursor_x * 72 + 60, cursor_y * 72 + 60, image=cursor, tag="CURSOR")
        draw_neko()
    elif index == 6:
        timer += 1
        if timer == 1:
            draw_txt("GAME OVER", 312, 348, 60, "red", tag="OVER")
        if timer == 50:
            cvs.delete("OVER")
            index = 0
    cvs.delete("INFO")
    draw_txt("SCORE: " + str(score), 160, 60, 32, "blue", tag="INFO")
    draw_txt("HISC: " + str(hisc), 450, 60, 32, "yellow", tag="INFO")
    if tsugi > 0:
        cvs.create_image(752, 128, image=neko_img[tsugi], tag="INFO")
    root.after(100, game_main)

root = tkinter.Tk()
root.title("game")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)

cvs = tkinter.Canvas(root, width=width, height=height)
bg = tkinter.PhotoImage(file="neko_bg.png")
cvs.create_image(width/2, height/2, image=bg, tag="BG")
cvs.pack()

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
cursor = tkinter.PhotoImage(file="neko_cursor.png")
game_main()
root.mainloop()