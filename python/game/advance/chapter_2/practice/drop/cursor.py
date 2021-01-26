import tkinter

width = 918
height = 768

mouse_x = 0
mouse_y = 0

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def game_main():
    canvas.delete("CURSOR")
    #text = "({},{})".format(mouse_x, mouse_y)
    if (mouse_x >= 24 and mouse_x < 72*8 + 24) and (mouse_y >= 24 and mouse_y < 72*8 + 24):
        x = int((mouse_x - 24) / 72)
        y = int((mouse_y - 24) / 72)
        canvas.create_image(72*x + 60, 72*y + 60, image=cursor, tags="CURSOR")
    #canvas.create_text(width/2, height/2, text=text, font=("Times New Roman", 40), tags="TEXT")
    root.after(100, game_main)

root = tkinter.Tk()
root.title("title")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)

canvas = tkinter.Canvas(root, width=width, height=height)
canvas.pack()

bg_img = tkinter.PhotoImage(file="neko_bg.png")
canvas.create_image(width/2, height/2, image=bg_img, tags="BG")

cursor = tkinter.PhotoImage(file="neko_cursor.png")
game_main()
root.mainloop()
