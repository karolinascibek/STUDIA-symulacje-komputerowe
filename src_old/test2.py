import tkinter
import datetime

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()

def tick():
    t = datetime.datetime.now()
    current_time = t.strftime("%H:%M:%S.%f")[:-5]
    canvas.itemconfigure(clock, text=current_time)
    canvas.after(2000, tick)

clock = canvas.create_text(320, 240, font="arial 72")
tick()

canvas.mainloop()