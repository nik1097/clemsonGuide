# Import module 
import tkinter
from tkinter import *
import webbrowser
import yaml

with open('clemsonGuide.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Create object 
root = Tk()
  
# Adjust size 
root.geometry("1000x800")
  
# Add image file
bg = PhotoImage(file = "bckgrnd.png")
  
# Show image using label
label1 = Label(root, image = bg)
label1.place(x = 0, y = 0)

def openUrl(url):
    webbrowser.open_new(url)

def create_button(filename, dimensions, url):
    image_pd_button = PhotoImage(file=filename)
    button1 = Button(image = image_pd_button, command = lambda: openUrl(url))
    button1.image = image_pd_button
    button1.grid(row=dimensions[0], column=dimensions[1], padx = 10, pady = 10)

for key, value in data['panels'].items():
    filename = value['imgFn']
    dimensions = value['dimension']
    url = value['url']
    
    create_button(filename, dimensions, url)

#button1.place(relwidth=0.09, relheight=0.13, relx=0.089, rely=0.176)

# Execute tkinter
root.mainloop()