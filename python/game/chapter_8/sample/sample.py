import tkinter

count = 0
width = 840
height = 472


def update_status():
    global count
    canvas.delete("PIC")
    canvas.create_image(width/2, height/2, image=photo[count], tag="PIC")
    count += 1
    if count >= len(photo):
        count = 0
    root.after(1000, update_status)

root = tkinter.Tk()
root.resizable(False, False)
root.title("digital picture")
canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()
photo = [
    tkinter.PhotoImage(file="0.png"),
    tkinter.PhotoImage(file="1.png"),
    tkinter.PhotoImage(file="2.png"),
    tkinter.PhotoImage(file="3.png"),
]
update_status()
root.mainloop()