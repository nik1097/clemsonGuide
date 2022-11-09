from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

canvas.create_text(
    1207.5, 977.0,
    text = "Frequently Asked Questions",
    fill = "#000000",
    font = ("Inter-Regular", int(72.0)))

canvas.create_text(
    1205.5, 1427.0,
)