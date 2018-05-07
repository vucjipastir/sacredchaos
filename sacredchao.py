import random
import Tkinter 
from PIL import ImageTk, Image

#This creates the main window of an application
window = Tkinter.Tk('Sacred Chaos')
window.title("Sacred Chaos")
window.geometry("800x500")
window.configure(background='black')

def new_img():
    # Pick a new number
    number = random.randint(0,223)
    # Add '.jpg' to number
    myimg = str(number)+'.jpg'
    # Return the image name
    return myimg
	
	
def newa_img():
    # Pick a new number
    number = random.randint(0,223)
    # Add '.jpg' to number
    myimga = str(number)+'.jpg'
    # Return the image name
    return myimga
	
	
def newo__img():
    # Pick a new number
    number = random.randint(0,223)
    # Add '.jpg' to number
    myimga = str(number)+'.jpg'
    # Return the image name
    return myimgo

def update_the_picture():
    num=random.randint(0, 223)
    w.configure(image = images[num])
	 

def update_the_pictures():
    num=random.randint(0, 223)
    q.configure(image = images[num])
	
	
def update_the_picturesa():
    num=random.randint(0, 223)
    z.configure(image = images[num])
	
	

images=[]
for fname in range(0,223):
    img = ImageTk.PhotoImage(Image.open("%d.jpg" % (fname)))
    images.append(img)

w = Tkinter.Label(window, image = img)
q = Tkinter.Label(window, image = img)
z = Tkinter.Label(window, image = img)
w.pack(side = "left", fill = "none", expand = "no")
q.pack(side = "right", fill = "none", expand = "no")
z.pack(side = "bottom", fill = "none", expand = "no")

b = Tkinter.Button(window, background='red', text="Randomize I", command = update_the_picture).pack(side = 'left', expand = 'yes')
b = Tkinter.Button(window, background='red', text="Randomize III", command = update_the_pictures).pack(side = 'right', expand = 'yes')
b = Tkinter.Button(window, background='red', text="Randomize II", command = update_the_picturesa).pack(side = 'bottom', expand = 'yes')

update_the_picture()
update_the_pictures()
update_the_picturesa()

window.mainloop()
