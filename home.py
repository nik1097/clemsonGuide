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
    3283.0, -127.5,
    text = "Weather",
    fill = "#ffffff",
    font = ("Inter-Regular", int(34.0)))

canvas.create_text(
    2144.0, -414.5,
    text = "?",
    fill = "#1e1e1e",
    font = ("Inter-ExtraBold", int(72.0)))

canvas.create_text(
    2280.5, -144.5,
    text = "Police Department",
    fill = "#ffffff",
    font = ("Inter-Regular", int(34.0)))

canvas.create_text(
    2531.0, -129.5,
    text = "University",
    fill = "#ffffff",
    font = ("Inter-Regular", int(34.0)))

canvas.create_text(
    2785.0, -108.5,
    text = "City Council",
    fill = "#ffffff",
    font = ("Inter-Regular", int(34.0)))

canvas.create_text(
    3033.0, -127.5,
    text = "Sports",
    fill = "#ffffff",
    font = ("Inter-Regular", int(34.0)))

canvas.create_text(
    3033.0, 126.5,
    text = "Recreation",
    fill = "#ffffff",
    font = ("Inter-Regular", int(34.0)))

canvas.create_text(
    3283.5, 126.5,
    text = "Restaurants",
    fill = "#ffffff",
    font = ("Inter-Regular", int(34.0)))

canvas.create_text(
    2281.0, 132.5,
    text = "Directory",
    fill = "#ffffff",
    font = ("Inter-Regular", int(34.0)))

canvas.create_text(
    2281.0, 390.5,
    text = "Housing",
    fill = "#ffffff",
    font = ("Inter-Regular", int(34.0)))

canvas.create_text(
    2532.0, 394.5,
    text = "Transport",
    fill = "#ffffff",
    font = ("Inter-Regular", int(34.0)))

canvas.create_text(
    2782.0, 390.5,
    text = "Map",
    fill = "#ffffff",
    font = ("Inter-Regular", int(34.0)))

canvas.create_text(
    3030.0, 388.5,
    text = " Events",
    fill = "#ffffff",
    font = ("Inter-Regular", int(34.0)))

canvas.create_text(
    2532.0, 132.5,
    text = "Careers",
    fill = "#ffffff",
    font = ("Inter-Regular", int(34.0)))

canvas.create_text(
    2782.0, 132.5,
    text = "Calendar",
    fill = "#ffffff",
    font = ("Inter-Regular", int(34.0)))

canvas.create_text(
    3283.0, 385.5,
    text = "Contact Us",
    fill = "#ffffff",
    font = ("Inter-Regular", int(34.0)))

window.resizable(False, False)
window.mainloop()
