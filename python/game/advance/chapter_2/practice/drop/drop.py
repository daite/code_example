import tkinter


width = 800
height = 600

mouse_x = 0
mouse_y = 0
mouse_c = 0

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

def game_main():
    cvs.delete("TEXT")
    text = "({},{}){}".format(mouse_x, mouse_y, mouse_c)
    cvs.create_text(width/2, height/2, text=text, font=("Times New Roman", 40), tags="TEXT")
    root.after(100, game_main)

root = tkinter.Tk()
root.title("hello")
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)
root.bind("<ButtonRelease>", mouse_release)
cvs = tkinter.Canvas(root, width=width, height=height)
cvs.pack()
game_main()
root.mainloop()