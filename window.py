from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1002x700")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 700,
    width = 1002,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

canvas.create_text(
    42.0, 10.0,
    text = "Offside Detection",
    fill = "#fad195",
    font = ("ZCOOLKuaiLe-Regular", int(36.0)))

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 55, y = 85,
    width = 282,
    height = 54)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    
    x = 55, y = 149,
    width = 137,
    height = 46)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 201, y = 149,
    width = 128,
    height = 46)

window.resizable(False, False)
window.mainloop()
