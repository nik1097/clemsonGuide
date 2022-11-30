# Import module 
from tkinter import *
  
# Create object 
root = Tk()
  
# Adjust size 
root.geometry("1150x800")
  
# Add image file
bg = PhotoImage(file = "bckgrnd_1.png")
  
# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)
  

  
# Create Frame
frame1 = Frame(root)
frame1.pack(pady = 20 )
  
# Add buttons
button1 = Button(frame1,text="Know More")
button1.grid(row=100,column=100)

  

# Execute tkinter
root.mainloop()