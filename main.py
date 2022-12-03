# Import module 
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
label1 = Label(image = bg)
label1.place(x = 0, y = 0)
home_icon=PhotoImage(file="images/home/home_resize.png")
def openUrl(url):
    webbrowser.open_new(url)

def create_button(top1, filename, dimensions, url):
    image_pd_button = PhotoImage(file=filename)
    button1 = Button(top1, image = image_pd_button, command = lambda: openUrl(url))
    button1.image = image_pd_button
    if dimensions[1] == 0:
        button1.grid(row=dimensions[0]+1, column=dimensions[1]+1, padx = (45, 10), pady = 10)
    else:
        button1.grid(row=dimensions[0]+1, column=dimensions[1]+1, padx = 10, pady = 10)

def menu_window():
    top1 = Toplevel()
    top1.title("Menu window")
    top1.geometry("1000x800")


    #bg = PhotoImage(file = "bckgrnd.png")

    label1 = Label(top1, image = bg)
    label1.place(x = 0, y = 0)

    buttonfaq = Button(top1, image = faq_icon, highlightthickness=0, command = faq_window)
    #buttonfaq.image = image_pd_button
    buttonfaq.grid(row=0, column = 1, padx = 0, pady = (20, 10))

    buttonchat = Button(top1, image = home_icon, highlightthickness=0, bd=0)
    #buttonfaq.image = image_pd_button
    buttonchat.grid(row=0, column = 5, padx = 0, pady = (20, 10))

    for key, value in data['panels'].items():
        filename = value['imgFn']
        dimensions = value['dimension']
        url = value['url'] 
        create_button(top1, filename, dimensions, url)

def faq_window():
    top = Toplevel()
    top.title("FAQ window")
    top.geometry("1000x800")

    faq_head = PhotoImage(file = "images/FAQ/FAQ_header_resize.png")
    faq_body = PhotoImage(file = "images/FAQ/FAQ_body_resize.png")
    home_icon=PhotoImage(file="images/home/home_resize.png")

    label1 = Label(top, image = bg)
    label1.place(x = 0, y = 0)
    
    #buttonfaq = Button(top, image = faq_icon, highlightthickness=0, command = faq_window)
    #buttonfaq.grid(row=1, column = 1, padx = 0, pady = (20, 10))

    label2 = Label(top, image = faq_head)
    label2.image = faq_head
    label2.place(x = 80, y = 50)

    label2 = Label(top, image = faq_body)
    label2.image = faq_body
    label2.place(x = 80, y = 150)
    
    label3=Button(top,image=home_icon,highlightthickness=0,command=menu_window)
    label3.image=home_icon
    label3.place(x=375,y=700)



faq_icon = PhotoImage(file="images\\icons\\FAQ_icon_resize.png")
buttonfaq = Button(image = faq_icon, highlightthickness=0, command = faq_window)
#buttonfaq.image = image_pd_button
buttonfaq.place(x = 40, y = 40)

chat_icon = PhotoImage(file="images\\icons\\Chat_icon_resize.png")
buttonchat = Button(image = chat_icon, highlightthickness=0, bd=0)
buttonchat.place(x = 875, y = 40)

description = PhotoImage(file = "images/home/Description_resize.png")
label1 = Label(root, image = description)
label1.place(x = 100, y = 350)

clemsonHeader = PhotoImage(file = "images/home/clemsonHeader_resize.png")
hlabel = Label(root, image = clemsonHeader)
hlabel.place(x = 100, y = 200)

knowMore_icon = PhotoImage(file="images\\home\\knowMore_icon_resize.png")
buttonknowMore = Button(image = knowMore_icon, highlightthickness=0, command = menu_window)
buttonknowMore.place(x = 400, y = 500)

# Execute tkinter
root.mainloop()