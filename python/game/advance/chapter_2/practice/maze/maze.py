import tkinter
import tkinter.messagebox

# maze data: randomize
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
]

key = ""
width = 80 * 8
height = 80 * 10

cx = 1
cy = 1
count = 0

def key_press(e):
    global key 
    key = e.keysym

def key_release(e):
    global key
    key = ""

def game_main():
    global cx, cy, count
    canvas.delete("CHAR")
    if key == "Shift_L" and count > 1:
        canvas.delete("PINK")
        for y in range(10):
            for x in range(8):
                if maze[y][x] == 2:
                    maze[y][x] = 0
        cx = 1
        cy = 1
        count = 0
    if key == "Up":
        if maze[cy-1][cx] == 0:
            cy -= 1
    if key == "Down":
        if maze[cy+1][cx] == 0:
            cy += 1
    if key == "Left":
        if maze[cy][cx-1] == 0:
            cx -= 1
    if key == "Right":
        if maze[cy][cx+1] == 0:
            cx += 1
    if maze[cy][cx] == 0:
        maze[cy][cx] = 2
        count += 1
    canvas.create_rectangle(80*cx, 80*cy, 80*cx + 79, 80*cy + 79, fill="pink", width=0, tags="PINK")
    canvas.create_image(80*cx + 40, 80*cy + 40, image=character, tags="CHAR")
    if count == 22:
        canvas.update()
        tkinter.messagebox.showinfo("INFO", "COMPLETED!")
    else:
        root.after(100, game_main)
    

root = tkinter.Tk()
root.title("root")
root.bind("<KeyPress>", key_press)
root.bind("<KeyRelease>", key_release)

canvas = tkinter.Canvas(root, width=width, height=height)
canvas.pack()
for y in range(10):
    for x in range(8):
        if maze[y][x] != 0:
            canvas.create_rectangle(80*x, 80*y, 80*x + 79, 80*y + 79, fill="skyblue", width=0)
character = tkinter.PhotoImage(file="mimi_s.png")
canvas.create_image(80*cx + 40, 80*cy + 40, image=character, tags="CHAR")
game_main()
root.mainloop()
