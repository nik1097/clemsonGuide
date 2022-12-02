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
faq_head = PhotoImage(file = "images/FAQ/FAQ_header_resize.png")
faq_body = PhotoImage(file = "images/FAQ/FAQ_body_resize.png")
  
# Show image using label
label1 = Label(root, image = bg)
label1.place(x = 0, y = 0)

def faq_window():
    top = Toplevel()
    top.title("FAQ window")
    top.geometry("1000x800")
    #bg = PhotoImage(file = "bckgrnd.png")
    label1 = Label(top, image = bg)
    label1.place(x = 0, y = 0)

    label2 = Label(top, image = faq_head)
    label2.place(x = 80, y = 30)

    label2 = Label(top, image = faq_body)
    label2.place(x = 80, y = 130)
    #lab = Label(top, text="This is second window!")
    #lab.pack(pady=20)

def openUrl(url):
    webbrowser.open_new(url)

image_pd_button = PhotoImage(file="images\icons\FAQ_icon.png")
buttonfaq = Button(image = image_pd_button, border=0, command = faq_window)
buttonfaq.image = image_pd_button
buttonfaq.grid(row=0, column=5)

def create_button(filename, dimensions, url):
    image_pd_button = PhotoImage(file=filename)
    button1 = Button(image = image_pd_button, command = lambda: openUrl(url))
    button1.image = image_pd_button
    button1.grid(row=dimensions[0]+1, column=dimensions[1]+1, padx = 10, pady = 10)

for key, value in data['panels'].items():
    filename = value['imgFn']
    dimensions = value['dimension']
    url = value['url']
    
    create_button(filename, dimensions, url)

#button1.place(relwidth=0.09, relheight=0.13, relx=0.089, rely=0.176)

# Execute tkinter
root.mainloop()