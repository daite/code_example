import tkinter

width = 800
height = 600
index = 0

def game_main():
    global index
    canvas.delete("NEKO")
    if index == 4:
        index = 0
    canvas.create_image(width/2, height/2, image=images[index], tags="NEKO")
    index += 1
    root.after(1000, game_main)
    

root = tkinter.Tk()
root.title("images")
canvas = tkinter.Canvas(root, width=width, height=height)
canvas.pack()

images = [
    tkinter.PhotoImage(file="cat00.png"),
    tkinter.PhotoImage(file="cat01.png"),
    tkinter.PhotoImage(file="cat02.png"),
    tkinter.PhotoImage(file="cat03.png"),
]

game_main()
root.mainloop()
