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
    1209.0, -205.5,
    text = "Welcome to the City of Clemson",
    fill = "#ffffff",
    font = ("Inter-Bold", int(78.0)))

canvas.create_text(
    1206.0, 313.0,
    text = "Know More",
    fill = "#ffffff",
    font = ("Inter-Bold", int(42.0)))

canvas.create_text(
    1786.0, 369.5,
    text = "SOS",
    fill = "#ffffff",
    font = ("Inter-SemiBold", int(42.0)))

canvas.create_text(
    1209.0, 107.0,
    text = "Clemson is a city in Pickens and Anderson counties in the U.S. state of South Carolina. Clemson is home to Clemson University; in 2015, the Princeton Review cited the town of Clemson as ranking #1 in the United States for town-and-gown relations with its resident university.",
    fill = "#1e1e1e",
    font = ("Inter-Bold", int(24.0)))

canvas.create_text(
    595.0, -408.5,
    text = "?",
    fill = "#1e1e1e",
    font = ("Inter-ExtraBold", int(72.0)))

window.resizable(False, False)
window.mainloop()
